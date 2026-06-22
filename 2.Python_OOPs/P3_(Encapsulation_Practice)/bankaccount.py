class BankAccount:
    """
    A bank account with full encapsulation.
    Public API: owner, balance, deposit(), withdraw(), get_statement()
    Internal:   _transactions, _validate_amount()
    Private:    __pin
    """

    _interest_rate = 0.03

    def __init__(self, owner, initial_balance=0.0, pin = "0000" ):
        self.owner = owner
        self._balance = float(initial_balance)
        self._transactions = []

        self.__pin = pin

    @property
    def balance(self):
        return self._balance

    @property
    def owner(self):
        return self._owner
    
    
    @owner.setter
    def owner(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Owner must be a non empty string")
        self._owner = name.strip()

    def deposit(self, amount):
        #pass
        self._validate_amount(amount)
        self._balance += amount
        self._transactions.append(f"Deposit : +${amount:,.2f}")
        return self._balance
    
    def withdraw(self, amount, pin):
        #pass
        self._validate_amount(amount)
        if not self._check_pin(pin):
            raise PermissionError("Incorrect Pin")
        if self._balance < amount:
            raise ValueError("Insufficient Balance")
        self._balance -= amount
        self._transactions.append(f"Withdrawal : -${amount:,.2f}")
        return self._balance    
    

    def get_statements(self):
        lines = [
            f"Account owner : {self.owner}",
            f"Balance : ${self._balance:,.2f}",
            "Transactions :"
        ]
        lines += self._transactions or ["  No transactions yet."]
        return "\n".join(lines)
    
    def change_pin(self, new_pin, old_pin):
        if not self._check_pin(old_pin):
            raise PermissionError("Wrong Pin")
        if len(str(new_pin)) != 4:
            raise TypeError("Pin must be 4 digits")
        self.__pin = new_pin

    def _validate_amount(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Value must be a number")
        if amount <= 0:
            raise ValueError("Amount must be Positive")

    def _check_pin(self, pin):
        return str(pin) == str(self.__pin)
    
    @classmethod
    def get_interest_rate(cls):
        return cls._interest_rate
    

acc = BankAccount("Arslan", 1000, pin="7426")

acc.deposit(500)
acc.withdraw(200, pin="7426")

print(acc.balance)
print(acc.get_statements())

try: 
    acc.balance = 9999

except AttributeError as e:
    print(f"Blocked: {e}")

try:
    acc.withdraw(100, pin=8888)
except PermissionError as e:
    print(f"Blocked:{e}")

try:
    acc.owner = ""

except ValueError as e:
    print(f"Blocked: {e}")






    
