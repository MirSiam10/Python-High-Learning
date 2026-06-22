class BankAccount :
    interest_rate = 0.05
    total_accounts = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        BankAccount.total_accounts += 1
    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts
    
    @classmethod
    def set_interest_rate(cls, new_rate):
        if not 0 < new_rate < 1 :
            raise ValueError("Enter a postive number between 0 to 1: ")
        cls.interest_rate = new_rate

    #Factory Method
    @classmethod
    def new_string(cls, obj_string):
        owner, balance = obj_string.split(":")
        return cls(owner, float(balance))
    
acc1 = BankAccount("Arslan", 30000)
acc2 = BankAccount("Afsan", 50000)
acc3 = BankAccount("Ariyan", 25000)

print(BankAccount.get_total_accounts())
    
BankAccount.set_interest_rate(0.08)
print(BankAccount.interest_rate)

acc4 = BankAccount.new_string("Sam:20000")
print(acc4.owner)
print(acc4.balance)

