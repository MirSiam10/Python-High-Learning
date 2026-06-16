class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive.")
        self._radius = value

    # ── READ-ONLY property — no setter defined ───────
    @property
    def area(self):
        return 3.14159 * self._radius ** 2

    @property
    def circumference(self):
        return 2 * 3.14159 * self._radius

    # ── Computed property — derived from other data ──
    @property
    def diameter(self):
        return self._radius * 2


c = Circle(5)
print(c.radius)           # 5    — readable
print(c.area)             # 78.53... — computed on the fly
print(c.diameter)         # 10   — computed

c.radius = 10             # ✅ Setter works
print(c.area)             # 314.159... — recomputed automatically!

try:
    c.area = 999          # ❌ No setter defined
except AttributeError as e:
    print(e)              # can't set attribute