from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    """Abstract Contract that all Payment Methods must follow"""

    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

    def validate_amount(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")


class CreditCardProcessor(PaymentProcessor):
    def __init__(self, card_number):
        self.card_number = card_number

    def process_payment(self, amount):
        self.validate_amount(amount)
        return f"Charged ${amount:.2f} to card ending in {self.card_number[-4:]}"

    def refund(self, amount):
        self.validate_amount(amount)
        return f"Refunded ${amount:.2f} to card ending in {self.card_number[-4:]}"


class PaypalProcessor(PaymentProcessor):
    def __init__(self, email):
        self.email = email

    def process_payment(self, amount):
        self.validate_amount(amount)
        return f"Charged ${amount:.2f} via paypal account {self.email}"

    def refund(self, amount):
        self.validate_amount(amount)
        return f"Refunded ${amount:.2f} via paypal account {self.email}"


def checkout(processor: PaymentProcessor, amount):
    return processor.process_payment(amount)


cc = CreditCardProcessor("122345676543567")
pp = PaypalProcessor("mir10siam@gmail.com")

print(checkout(cc, 200))
print(checkout(pp, 400))