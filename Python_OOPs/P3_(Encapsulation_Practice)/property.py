class BankAccount:
    def __init__(self, owner , balance):
        self.owner = owner
        self._balance = balance


    # ── GETTER — called when you READ balance ────────

    @property
    def balance(self):
        return self._balance
    
        # ── SETTER — called when you WRITE balance ───────
    @balance.setter
    def balance(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Value mus be a number")
        if amount < 0:
            raise ValueError("Value must be a positive Number")
        
        self._balance = amount

    # ── DELETER — called when you DELETE balance ─────
    @balance.deleter
    def balance(self):
        raise AttributeError("Balance cannot be deleted")
    
acc = BankAccount("Ashin", 1500)

print(acc.balance)

acc.balance = 2000
print(acc.balance)

try:
    acc.balance = -2
except ValueError as e:
    print(e)


try:
    acc.balance = "Two Thousand Taka"
except TypeError as e:
    print(e)

try:
    del acc.balance      
except AttributeError as e:
    print(e)             


    