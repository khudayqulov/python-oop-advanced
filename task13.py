"""Task 13 — Small e-commerce domain using composition and polymorphism.

This is a local simulation: payment methods do not charge real money.
"""

from abc import ABC, abstractmethod


def non_negative_money(amount):
    return (not isinstance(amount, bool)
            and isinstance(amount, (int, float))
            and 0 <= amount < float("inf"))


def positive_quantity(quantity):
    return (isinstance(quantity, int)
            and not isinstance(quantity, bool)
            and quantity > 0)


class User:
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name cannot be empty")
        self.name = name.strip()


class Product:
    def __init__(self, name, price, quantity):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name cannot be empty")
        if not non_negative_money(price):
            raise ValueError("Product price cannot be negative")
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity < 0:
            raise ValueError("Stock must be a non-negative integer")
        self.name = name
        self.price = price
        self.quantity = quantity


class ShoppingCart:
    def __init__(self):
        self.items = {}  # Product object -> integer quantity
        self.discount_percent = 0

    def add(self, product, quantity=1):
        if not isinstance(product, Product):
            raise TypeError("Only a Product can be added")
        if not positive_quantity(quantity):
            raise ValueError("Cart quantity must be a positive integer")
        self.items[product] = self.items.get(product, 0) + quantity

    def remove(self, product):
        if product not in self.items:
            raise ValueError("Product is not in the cart")
        del self.items[product]

    def apply_discount(self, percent):
        if (isinstance(percent, bool)
                or not isinstance(percent, (int, float))
                or not 0 <= percent <= 100):
            raise ValueError("Discount must be between 0 and 100")
        self.discount_percent = percent

    def total_price(self):
        subtotal = sum(
            product.price * quantity
            for product, quantity in self.items.items()
        )
        return subtotal * (1 - self.discount_percent / 100)

    def clear(self):
        self.items.clear()
        self.discount_percent = 0


class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.unit_price = product.price  # Snapshot of the price at checkout.

    def subtotal(self):
        return self.unit_price * self.quantity


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        """Simulate a payment and return a receipt."""

    @staticmethod
    def _check_amount(amount):
        if not non_negative_money(amount):
            raise ValueError("Payment amount cannot be negative")


class CardPayment(Payment):
    def pay(self, amount):
        self._check_amount(amount)
        return f"Paid {amount:.2f} with card"


class CashPayment(Payment):
    def pay(self, amount):
        self._check_amount(amount)
        return f"Paid {amount:.2f} in cash"


class Order:
    ALLOWED_TRANSITIONS = {
        "PAID": {"SHIPPED", "CANCELLED"},
        "SHIPPED": {"COMPLETED"},
        "COMPLETED": set(),
        "CANCELLED": set(),
    }

    def __init__(self, customer, items, discount_percent, receipt):
        self.customer = customer
        self.items = items
        self.discount_percent = discount_percent
        self.receipt = receipt
        self.status = "PAID"
        self.total = sum(item.subtotal() for item in items)
        self.total *= 1 - discount_percent / 100

    def set_status(self, new_status):
        if new_status not in self.ALLOWED_TRANSITIONS[self.status]:
            raise ValueError(
                f"Invalid order transition: {self.status} -> {new_status}"
            )
        if new_status == "CANCELLED":
            for item in self.items:
                item.product.quantity += item.quantity
        self.status = new_status

    def cancel(self):
        self.set_status("CANCELLED")


class Customer(User):
    def __init__(self, name):
        super().__init__(name)
        self.cart = ShoppingCart()
        self.orders = []

    def checkout(self, payment):
        if not isinstance(payment, Payment):
            raise TypeError("A Payment object is required")
        if not self.cart.items:
            raise ValueError("Cannot checkout an empty cart")

        for product, quantity in self.cart.items.items():
            if product.quantity < quantity:
                raise ValueError(f"Not enough stock for {product.name}")

        order_items = [
            OrderItem(product, quantity)
            for product, quantity in self.cart.items.items()
        ]
        discount = self.cart.discount_percent
        total = self.cart.total_price()

        for item in order_items:
            item.product.quantity -= item.quantity
        try:
            receipt = payment.pay(total)
        except Exception:
            for item in order_items:
                item.product.quantity += item.quantity
            raise

        order = Order(self, order_items, discount, receipt)
        self.orders.append(order)
        self.cart.clear()
        return order


class Admin(User):
    def add_product(self, product, catalog):
        if not isinstance(product, Product):
            raise TypeError("Only Product objects can be added")
        if product in catalog:
            raise ValueError("Product already exists")
        catalog.append(product)

    def remove_product(self, product, catalog):
        if product not in catalog:
            raise ValueError("Product does not exist")
        catalog.remove(product)


def demo():
    products = [
        Product("Laptop", 1000, 3),
        Product("Mouse", 50, 20),
        Product("Keyboard", 100, 8),
    ]
    admin = Admin("Admin")
    catalog = []
    for product in products:
        admin.add_product(product, catalog)

    customers = [Customer("Ali"), Customer("Vali"), Customer("Sardor")]
    payments = [CardPayment(), CashPayment(), CardPayment()]
    for customer, product, payment in zip(customers, products, payments):
        customer.cart.add(product, 1)
        customer.cart.apply_discount(10)
        order = customer.checkout(payment)
        print(customer.name, order.total, order.receipt, order.status)
    customers[0].orders[0].cancel()
    print("Restored Laptop stock:", products[0].quantity)


if __name__ == "__main__":
    demo()
