"""Task 15 — Ride sharing, Strategy pricing and strict status transitions.

All payments and rides are simulated. No live booking or charging occurs.
"""

from abc import ABC, abstractmethod


def positive_distance(distance):
    return (not isinstance(distance, bool)
            and isinstance(distance, (int, float))
            and 0 < distance < float("inf"))


class User:
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name cannot be empty")
        self.name = name.strip()


class FareStrategy(ABC):
    @abstractmethod
    def calculate(self, distance_km):
        """Return fare for the given distance."""


class EconomyPricing(FareStrategy):
    def calculate(self, distance_km):
        return 5000 + 2000 * distance_km


class ComfortPricing(FareStrategy):
    def calculate(self, distance_km):
        return 8000 + 3000 * distance_km


class BusinessPricing(FareStrategy):
    def calculate(self, distance_km):
        return 15000 + 5000 * distance_km


class Vehicle:
    def __init__(self, model, pricing):
        if not isinstance(pricing, FareStrategy):
            raise TypeError("Pricing must be a FareStrategy")
        self.model = model
        self.pricing = pricing

    def calculate_fare(self, distance_km):
        if not positive_distance(distance_km):
            raise ValueError("Distance must be positive")
        return self.pricing.calculate(distance_km)


class EconomyCar(Vehicle):
    def __init__(self, model):
        super().__init__(model, EconomyPricing())


class ComfortCar(Vehicle):
    def __init__(self, model):
        super().__init__(model, ComfortPricing())


class BusinessCar(Vehicle):
    def __init__(self, model):
        super().__init__(model, BusinessPricing())


class Driver(User):
    def __init__(self, name):
        super().__init__(name)
        self.active_ride = None

    @property
    def is_available(self):
        return self.active_ride is None

    def accept_ride(self, ride):
        if not isinstance(ride, Ride):
            raise TypeError("Expected a Ride")
        if not self.is_available:
            raise ValueError("Driver already has an active ride")
        if ride.status != "PENDING":
            raise ValueError("Only pending rides can be accepted")
        ride.driver = self
        ride.status = "ACCEPTED"
        self.active_ride = ride


class Passenger(User):
    def __init__(self, name):
        super().__init__(name)
        self.rides = []

    def request_ride(self, vehicle, distance_km):
        ride = Ride(self, vehicle, distance_km)
        self.rides.append(ride)
        return ride


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        """Simulate payment and return a confirmation."""

    @staticmethod
    def _validate(amount):
        if (isinstance(amount, bool)
                or not isinstance(amount, (int, float))
                or not 0 < amount < float("inf")):
            raise ValueError("Fare must be positive")


class CardPayment(Payment):
    def pay(self, amount):
        self._validate(amount)
        return f"Card charged {amount:.0f} UZS (demo)"


class CashPayment(Payment):
    def pay(self, amount):
        self._validate(amount)
        return f"Cash received {amount:.0f} UZS (demo)"


class Ride:
    def __init__(self, passenger, vehicle, distance_km):
        if not isinstance(passenger, Passenger):
            raise TypeError("Passenger must be a Passenger object")
        if not isinstance(vehicle, Vehicle):
            raise TypeError("Vehicle must be a Vehicle object")
        self.passenger = passenger
        self.vehicle = vehicle
        self.distance_km = distance_km
        self.fare = vehicle.calculate_fare(distance_km)
        self.driver = None
        self.status = "PENDING"
        self.payment_receipt = None

    def start(self):
        if self.status != "ACCEPTED":
            raise ValueError("Ride must first be accepted")
        self.status = "IN_PROGRESS"

    def complete(self, payment):
        if self.status != "IN_PROGRESS":
            raise ValueError("Only an in-progress ride can be completed")
        if not isinstance(payment, Payment):
            raise TypeError("Payment must be a Payment object")
        receipt = payment.pay(self.fare)
        self.payment_receipt = receipt
        self.status = "COMPLETED"
        self.driver.active_ride = None
        return receipt

    def cancel(self):
        if self.status not in {"PENDING", "ACCEPTED"}:
            raise ValueError("Ride cannot be cancelled at this stage")
        self.status = "CANCELLED"
        if self.driver is not None:
            self.driver.active_ride = None


def demo():
    passengers = [Passenger("Ali"), Passenger("Vali"), Passenger("Sardor")]
    drivers = [Driver("Driver A"), Driver("Driver B"), Driver("Driver C")]
    vehicles = [
        EconomyCar("Cobalt"),
        ComfortCar("Malibu"),
        BusinessCar("Mercedes"),
    ]
    payments = [CardPayment(), CashPayment(), CardPayment()]

    for passenger, driver, vehicle, payment in zip(
        passengers, drivers, vehicles, payments
    ):
        ride = passenger.request_ride(vehicle, 5)
        driver.accept_ride(ride)
        ride.start()
        print(passenger.name, ride.complete(payment), ride.status)


if __name__ == "__main__":
    demo()
