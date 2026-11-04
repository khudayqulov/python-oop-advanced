"""Task 04 — Static methods for temperature conversion."""


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return self.celsius_to_fahrenheit(self.celsius)

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9 / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9


def demo():
    temperatures = [Temperature(25), Temperature(0), Temperature(100)]
    for temperature in temperatures:
        print(temperature.celsius, "°C =", temperature.to_fahrenheit(), "°F")
    print("86 °F =", Temperature.fahrenheit_to_celsius(86), "°C")


if __name__ == "__main__":
    demo()
