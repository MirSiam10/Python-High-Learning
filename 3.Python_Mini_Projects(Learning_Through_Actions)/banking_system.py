from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class Transaction:
    transaction_type: str
    amount: float
    timestamp: str = field(
        default_factory=lambda: datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    )


class Account(ABC):
    _account_counter = 1000

    def __init__(self, owner: str, initial_balance: float = 0.0):
        if not owner.strip():
            raise ValueError("Owner name cannot be empty.")

        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self._owner = owner
        self._balance = initial_balance
        self._transactions: list[Transaction] = []

        self._account_number = Account._account_counter
        Account._account_counter += 1


    @property
    def owner(self) -> str:
        return self._owner

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def account_number(self) -> int:
        return self._account_number


    @abstractmethod
    def withdraw(self, amount: float) -> float:
        pass

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self._balance += amount
        self._log(Transaction("deposit", amount))
        return self._balance

    def _log(self, transaction: Transaction) -> None:
        if not isinstance(transaction, Transaction):
            raise TypeError("Must be a Transaction object.")

        self._transactions.append(transaction)

    def get_statement(self) -> str:
        lines = [
            f"Account #{self.account_number} — {self.owner} ({self.__class__.__name__})",
            f"Balance: ${self.balance:,.2f}",
            "Transactions:"
        ]

        if not self._transactions:
            lines.append("No transactions yet.")

        for t in self._transactions[-5:]:
            lines.append(
                f"{t.timestamp} | {t.transaction_type:<12} | ${t.amount:,.2f}"
            )

        return "\n".join(lines)


    def __eq__(self, other):
        if not isinstance(other, Account):
            return NotImplemented

        return self.account_number == other.account_number

    def __str__(self):
        return (
            f"{self.__class__.__name__}"
            f"(#{self.account_number}, {self.owner}, ${self.balance:,.2f})"
        )



class SavingsAccount(Account):

    def __init__(
        self,
        owner: str,
        initial_balance: float = 0.0,
        interest_rate: float = 0.02
    ):
        super().__init__(owner, initial_balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self._balance:
            raise ValueError(
                "Insufficient funds. Savings accounts do not allow overdrafts."
            )

        self._balance -= amount
        self._log(Transaction("withdraw", amount))
        return self._balance

    def apply_interest(self) -> float:
        interest = self._balance * self.interest_rate

        self._balance += interest
        self._log(Transaction("interest", interest))

        return self._balance


# Alias for compatibility
SavingAccount = SavingsAccount



class CheckingAccount(Account):

    def __init__(
        self,
        owner: str,
        initial_balance: float = 0.0,
        overdraft_limit: float = 500.0
    ):
        super().__init__(owner, initial_balance)
        self._overdraft_limit = overdraft_limit

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > (self._balance + self._overdraft_limit):
            raise ValueError("Withdrawal exceeds overdraft limit.")

        self._balance -= amount
        self._log(Transaction("withdraw", amount))

        return self._balance



class FixedDepositAccount(Account):

    def __init__(
        self,
        owner: str,
        initial_balance: float = 0.0,
        interest_rate: float = 0.05,
        maturity_period: int = 12
    ):
        super().__init__(owner, initial_balance)

        self.interest_rate = interest_rate
        self.maturity_period = maturity_period
        self._months_elapsed = 0

    def advance_month(self) -> None:
        self._months_elapsed += 1

        interest = self._balance * (self.interest_rate / 12)

        self._balance += interest
        self._log(Transaction("interest", interest))

    def withdraw(self, amount: float) -> float:
        if self._months_elapsed < self.maturity_period:
            raise ValueError(
                f"Account not matured yet "
                f"({self._months_elapsed}/{self.maturity_period} months)."
            )

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self._balance:
            raise ValueError("Insufficient funds.")

        self._balance -= amount
        self._log(Transaction("withdraw", amount))

        return self._balance

    def __str__(self):
        status = (
            "matured"
            if self._months_elapsed >= self.maturity_period
            else f"{self._months_elapsed}/{self.maturity_period} months"
        )

        return (
            f"FixedDepositAccount("
            f"#{self.account_number}, "
            f"{self.owner}, "
            f"${self.balance:,.2f}, "
            f"{status})"
        )



class Bank:

    def __init__(self, name: str):
        self.name = name
        self._accounts: dict[int, Account] = {}

    def open_account(self, account: Account) -> int:
        self._accounts[account.account_number] = account
        return account.account_number

    def find_account(self, account_number: int):
        return self._accounts.get(account_number)

    def transfer(
        self,
        from_acc_num: int,
        to_acc_num: int,
        amount: float
    ) -> str:

        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")

        from_acc = self.find_account(from_acc_num)
        to_acc = self.find_account(to_acc_num)

        if not from_acc or not to_acc:
            raise ValueError("One or both accounts not found.")

        from_acc.withdraw(amount)

        from_acc._transactions.pop()

        from_acc._log(Transaction("transfer_out", amount))

        # Deposit manually (avoid duplicate logs)
        to_acc._balance += amount
        to_acc._log(Transaction("transfer_in", amount))

        return (
            f"Transferred ${amount:,.2f} "
            f"from #{from_acc_num} to #{to_acc_num}"
        )

    def total_assets(self) -> float:
        return sum(acc.balance for acc in self._accounts.values())

    def get_richest_customer(self):

        totals = {}

        for acc in self._accounts.values():
            totals[acc.owner] = totals.get(acc.owner, 0) + acc.balance

        if not totals:
            return None

        return max(totals, key=totals.get)

    def __len__(self):
        return len(self._accounts)

    def summary(self) -> str:

        lines = [
            "=" * 60,
            f"{self.name} — Bank Summary",
            "=" * 60,
            f"Total Accounts : {len(self)}",
            f"Total Assets   : ${self.total_assets():,.2f}",
            f"Richest Customer: {self.get_richest_customer()}",
            "=" * 60,
        ]

        for acc in self._accounts.values():
            lines.append(acc.get_statement())
            lines.append("-" * 60)

        return "\n".join(lines)




if __name__ == "__main__":

    bank = Bank("Python National Bank")

    savings = SavingsAccount(
        "Alice",
        initial_balance=1000,
        interest_rate=0.03
    )

    checking = CheckingAccount(
        "Bob",
        initial_balance=500,
        overdraft_limit=300
    )

    fixed = FixedDepositAccount(
        "Alice",
        initial_balance=5000,
        interest_rate=0.06,
        maturity_period=3
    )

    bank.open_account(savings)
    bank.open_account(checking)
    bank.open_account(fixed)

    print(f"Opened {len(bank)} accounts.\n")

    savings.deposit(200)
    savings.withdraw(150)
    savings.apply_interest()

    checking.deposit(100)
    checking.withdraw(800)

    print(
        bank.transfer(
            savings.account_number,
            checking.account_number,
            300
        )
    )

    print("\nAttempting early withdrawal:")
    try:
        fixed.withdraw(1000)
    except ValueError as e:
        print("Caught:", e)

    for _ in range(3):
        fixed.advance_month()

    print("\nWithdrawal after maturity:")
    print(f"Remaining Balance: ${fixed.withdraw(1000):,.2f}")

    print("\nEquality Test:")
    print(savings == savings)
    print(savings == SavingsAccount("Charlie", 500))

    print("\nRichest Customer:")
    print(bank.get_richest_customer())

    print()
    print(bank.summary())