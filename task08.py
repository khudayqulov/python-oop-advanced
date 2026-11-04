"""Task 08 — Vehicle hierarchy, speed changes and validation."""


class Vehicle:
    def __init__(self, brand, model, speed=0):
        if speed < 0:
            raise ValueError("Speed cannot be negative")
        self.brand = brand
        self.model = model
        self.speed = speed
        self.is_running = False

    def start(self):
        self.is_running = True
        return "Vehicle started"

    def stop(self):
        self.is_running = False
        self.speed = 0
        return "Vehicle stopped"

    def accelerate(self, amount):
        if amount <= 0:
            raise ValueError("Acceleration must be positive")
        if not self.is_running:
            raise RuntimeError("Start the vehicle first")
        self.speed += amount
        return self.speed

    def brake(self, amount):
        if amount <= 0:
            raise ValueError("Brake amount must be positive")
        self.speed = max(0, self.speed - amount)
        return self.speed

    def get_info(self):
        return f"{self.brand} {self.model}, speed: {self.speed} km/h"


class Car(Vehicle):
    def __init__(self, brand, model, number_of_doors, speed=0):
        super().__init__(brand, model, speed)
        if (isinstance(number_of_doors, bool)
                or not isinstance(number_of_doors, int)
                or number_of_doors <= 0):
            raise ValueError("Number of doors must be positive")
        self.number_of_doors = number_of_doors

    def get_info(self):
        return f"{super().get_info()}, doors: {self.number_of_doors}"


class Motorcycle(Vehicle):
    def __init__(self, brand, model, has_sidecar=False, speed=0):
        super().__init__(brand, model, speed)
        if not isinstance(has_sidecar, bool):
            raise ValueError("has_sidecar must be boolean")
        self.has_sidecar = has_sidecar

    def get_info(self):
        return f"{super().get_info()}, sidecar: {self.has_sidecar}"


class Truck(Vehicle):
    def __init__(self, brand, model, load_capacity, speed=0):
        super().__init__(brand, model, speed)
        if load_capacity <= 0:
            raise ValueError("Load capacity must be positive")
        self.load_capacity = load_capacity

    def get_info(self):
        return f"{super().get_info()}, capacity: {self.load_capacity} tons"


def demo():
    vehicles = [
        Car("BMW", "320i", 4),
        Motorcycle("Kawasaki", "Ninja 500", False),
        Truck("Volvo", "FH", 18),
    ]
    for vehicle in vehicles:
        vehicle.start()
        vehicle.accelerate(50)
        vehicle.brake(15)
        print(vehicle.get_info())
        vehicle.stop()


if __name__ == "__main__":
    demo()
