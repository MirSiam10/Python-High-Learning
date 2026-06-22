from abc import ABC, abstractmethod
from dataclasses import dataclass

# ── STRATEGY PATTERN: swappable discount algorithms ──────────
#
# Design decision: apply(self, cart) instead of apply(self, total)
#
# The original apply(self, total) assumed discounts only ever need a dollar
# amount. BulkDiscount broke that assumption — it needs item count too.
#
# Option A: keep apply(self, total), give BulkDiscount extra state at
#   construction time. Problem: whoever builds the strategy must know the
#   cart's contents upfront, which defeats reusability. The strategy becomes
#   a one-shot object tied to a specific cart state.
#
# Option B: change to apply(self, cart), let each strategy pull what it needs.
#   Cost: strategies are now coupled to Cart's public interface (subtotal,
#   __len__). Benefit: strategies remain stateless, composable, and correct
#   at runtime regardless of when they were instantiated.
#
# Option B is the clearly better tradeoff here. The coupling is explicit and
# intentional — discounts ARE inherently about the cart. The alternative hides
# the dependency and introduces subtle bugs when a strategy is reused.

@dataclass
class Item:
    name: str
    price: float
    quantity: int = 1

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative.")
        if self.quantity <= 0:
            raise ValueError("Quantity must be positive.")

    @property
    def subtotal(self):
        return self.price * self.quantity

    # Two items are equal if name and price match, regardless of quantity.
    def __eq__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return self.name == other.name and self.price == other.price

    def __hash__(self):
        # Required when __eq__ is defined so Items can be used in sets/dicts.
        return hash((self.name, self.price))



class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, cart) -> float:
        """Return the final total after applying this discount to cart."""

    @abstractmethod
    def description(self) -> str:
        pass


class NoDiscount(DiscountStrategy):
    def apply(self, cart):
        return cart.subtotal

    def description(self):
        return "No discount"


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent):
        if not 0 <= percent <= 100:
            raise ValueError("Percent must be between 0 and 100.")
        self.percent = percent

    def apply(self, cart):
        return cart.subtotal * (1 - self.percent / 100)

    def description(self):
        return f"{self.percent}% off"


class FlatDiscount(DiscountStrategy):
    def __init__(self, amount):
        self.amount = amount

    def apply(self, cart):
        return max(0, cart.subtotal - self.amount)  # never go negative

    def description(self):
        return f"${self.amount:,.2f} off"


class BulkDiscount(DiscountStrategy):
    """Applies a percentage discount when the cart exceeds a quantity threshold."""

    def __init__(self, threshold=10, percent=10):
        self.threshold = threshold
        self.percent = percent

    def apply(self, cart):
        # Now correctly uses len(cart) because we receive the whole cart.
        if len(cart) > self.threshold:
            return cart.subtotal * (1 - self.percent / 100)
        return cart.subtotal

    def description(self):
        return f"{self.percent}% off orders of {self.threshold}+ items"


class StackedDiscount(DiscountStrategy):
    """Applies a sequence of discount strategies one after another.

    Each strategy receives a temporary proxy cart whose subtotal reflects
    the running total after prior discounts, while preserving item count
    so quantity-based strategies (like BulkDiscount) still work correctly.
    """

    def __init__(self, strategies: list):
        self.strategies = strategies

    def apply(self, cart):
        running_total = cart.subtotal
        for strategy in self.strategies:
            # Build a lightweight proxy so each strategy can still call
            # cart.subtotal and len(cart) as expected by the interface.
            proxy = _CartProxy(running_total, len(cart))
            running_total = strategy.apply(proxy)
        return running_total

    def description(self):
        parts = " → ".join(s.description() for s in self.strategies)
        return f"Stacked: {parts}"


class _CartProxy:
    """Minimal read-only proxy passed to each strategy in a StackedDiscount.

    Strategies call cart.subtotal and len(cart); nothing else is needed.
    Using a proxy instead of mutating the real cart keeps Cart unmodified
    and makes the stacking logic easy to reason about.
    """

    def __init__(self, subtotal: float, item_count: int):
        self._subtotal = subtotal
        self._item_count = item_count

    @property
    def subtotal(self):
        return self._subtotal

    def __len__(self):
        return self._item_count


# ── THE CART ─────────────────────────────────────────────────

class Cart:
    def __init__(self, discount_strategy: DiscountStrategy = None):
        self._items = []
        self.discount_strategy = discount_strategy or NoDiscount()

    def add(self, item: Item):
        self._items.append(item)

    def remove(self, item_name: str):
        """Remove the first item whose name matches item_name.

        Raises ValueError if no such item is found.
        """
        for i, item in enumerate(self._items):
            if item.name == item_name:
                del self._items[i]
                return
        raise ValueError(f"Item '{item_name}' not found in cart.")

    def __len__(self):
        return sum(item.quantity for item in self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __contains__(self, item_name):
        return any(item.name == item_name for item in self._items)

    def __iadd__(self, item: Item):
        """Enables: cart += Item(...)  — mutates cart in place, returns self.

        __iadd__ is the right choice here rather than __add__ because:
          - += on a cart should modify the cart, not create a new one.
          - __add__ would imply cart + item returns a *new* Cart (like string
            concatenation), which is confusing and not what callers expect.
        """
        self.add(item)
        return self

    @property
    def subtotal(self):
        return sum(item.subtotal for item in self._items)

    def checkout(self):
        return self.discount_strategy.apply(self)

    def __str__(self):
        lines = [f"Cart ({len(self)} items):"]
        for item in self._items:
            lines.append(f"  {item.name} x{item.quantity} — ${item.subtotal:,.2f}")
        lines.append(f"Subtotal: ${self.subtotal:,.2f}")
        lines.append(f"Discount: {self.discount_strategy.description()}")
        lines.append(f"Total:    ${self.checkout():,.2f}")
        return "\n".join(lines)


# ── TESTS ─────────────────────────────────────────────────────

def separator(title):
    print(f"\n{'─' * 50}")
    print(f"  {title}")
    print('─' * 50)


if __name__ == "__main__":
    # Items used across tests
    laptop   = Item("Laptop",    999.99, quantity=1)
    mouse    = Item("Mouse",      29.99, quantity=3)
    keyboard = Item("Keyboard",   79.99, quantity=2)
    monitor  = Item("Monitor",   349.99, quantity=1)
    usb_hub  = Item("USB Hub",    19.99, quantity=4)

    def build_cart(strategy):
        c = Cart(discount_strategy=strategy)
        c.add(laptop)
        c.add(mouse)
        c.add(keyboard)
        c.add(monitor)
        c.add(usb_hub)
        return c

    # Total quantity: 1+3+2+1+4 = 11 → exceeds BulkDiscount threshold of 10

    separator("NoDiscount")
    print(build_cart(NoDiscount()))

    separator("PercentageDiscount (15% off)")
    print(build_cart(PercentageDiscount(15)))

    separator("FlatDiscount ($50 off)")
    print(build_cart(FlatDiscount(50)))

    separator("BulkDiscount (10% off for 10+ items) — 11 items, triggers")
    print(build_cart(BulkDiscount(threshold=10, percent=10)))

    separator("StackedDiscount ($50 flat off, then 5% off remainder)")
    stacked = StackedDiscount([FlatDiscount(50), PercentageDiscount(5)])
    print(build_cart(stacked))

    separator("cart += Item(...) directly")
    cart = Cart(discount_strategy=PercentageDiscount(10))
    cart += Item("Webcam", 89.99, quantity=2)
    cart += Item("Headset", 149.99, quantity=1)
    print(cart)

    separator("Item.__eq__ — same name+price, different quantity")
    a = Item("Mouse", 29.99, quantity=1)
    b = Item("Mouse", 29.99, quantity=5)
    c = Item("Mouse", 39.99, quantity=1)
    print(f"  Item('Mouse', 29.99, qty=1) == Item('Mouse', 29.99, qty=5): {a == b}")  # True
    print(f"  Item('Mouse', 29.99, qty=1) == Item('Mouse', 39.99, qty=1): {a == c}")  # False

    separator("Cart.remove — removes first match, raises on missing")
    r = Cart()
    r.add(Item("Pen", 1.99, quantity=2))
    r.add(Item("Notepad", 4.99, quantity=1))
    r.add(Item("Pen", 1.99, quantity=3))  # second Pen entry
    print(f"  Before remove: {len(r._items)} line items")
    r.remove("Pen")
    print(f"  After remove('Pen'): {len(r._items)} line items (first Pen removed)")
    try:
        r.remove("Stapler")
    except ValueError as e:
        print(f"  remove('Stapler') raised ValueError: {e}")

    separator("BulkDiscount — below threshold, no discount")
    small_cart = Cart(discount_strategy=BulkDiscount(threshold=10, percent=10))
    small_cart.add(Item("Pen", 1.99, quantity=3))  # only 3 items
    print(small_cart)