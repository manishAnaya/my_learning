from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print("Credit Card Payment Successful.")
        print(f"Amount Paid : Rs.{amount}")

class UPIPayment(Payment):
    def process_payment(self, amount):
        print("UPI Payment Successful.")
        print(f"Amount Paid : Rs.{amount}")

credit = CreditCardPayment()
upi = UPIPayment()

credit.process_payment(5000)
upi.process_payment(2500)