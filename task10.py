"""Task 10 — Payment polymorphism through one pay() interface."""


def validate_amount(amount):
    if (isinstance(amount, bool)
            or not isinstance(amount, (int, float))
            or not 0 < amount < float("inf")):
        raise ValueError("Payment amount must be positive and finite")


class Payment:
    def pay(self, amount):
        raise NotImplementedError("Subclass must implement pay()")


class CreditCardPayment(Payment):
    def pay(self, amount):
        validate_amount(amount)
        return f"Card payment: {amount:.2f}"


class PayPalPayment(Payment):
    def pay(self, amount):
        validate_amount(amount)
        return f"PayPal payment: {amount:.2f}"


class CashPayment(Payment):
    def pay(self, amount):
        validate_amount(amount)
        return f"Cash payment: {amount:.2f}"


def demo():
    payments = [CreditCardPayment(), PayPalPayment(), CashPayment()]
    for payment in payments:
        print(payment.pay(100))


if __name__ == "__main__":
    demo()
