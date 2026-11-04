"""Task 05 — Product, taxes, discounts and validation."""


class Product:
    tax_rate = 0.12

    def __init__(self, name, price, quantity):
        if not self.is_valid_price(price):
            raise ValueError("Price must be a finite non-negative number")
        if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer")
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

    def apply_discount(self, percent):
        if not isinstance(percent, (int, float)) or not 0 <= percent <= 100:
            raise ValueError("Discount must be between 0 and 100")
        self.price *= 1 - percent / 100
        return self.price

    def price_with_tax(self):
        return self.price * (1 + self.tax_rate)

    @classmethod
    def change_tax_rate(cls, rate):
        if (isinstance(rate, bool) or not isinstance(rate, (int, float))
                or not 0 <= rate < float("inf")):
            raise ValueError("Tax rate must be a finite non-negative number")
        cls.tax_rate = rate

    @staticmethod
    def is_valid_price(price):
        return (not isinstance(price, bool)
                and isinstance(price, (int, float))
                and 0 <= price < float("inf"))


def demo():
    products = [
        Product("Laptop", 1000, 2),
        Product("Mouse", 50, 5),
        Product("Keyboard", 100, 3),
    ]
    products[0].apply_discount(10)
    Product.change_tax_rate(0.15)
    for product in products:
        print(product.name, product.total_price(), product.price_with_tax())
    Product.change_tax_rate(0.12)


if __name__ == "__main__":
    demo()
