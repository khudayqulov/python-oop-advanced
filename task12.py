"""Task 12 — Abstract Shape and polymorphic area calculation."""

from abc import ABC, abstractmethod
from math import pi


def positive_dimension(value):
    if (isinstance(value, bool)
            or not isinstance(value, (int, float))
            or not 0 < value < float("inf")):
        raise ValueError("All dimensions must be positive and finite")


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        """Calculate the shape's area."""


class Circle(Shape):
    def __init__(self, radius):
        positive_dimension(radius)
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        positive_dimension(width)
        positive_dimension(height)
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        positive_dimension(base)
        positive_dimension(height)
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.base * self.height / 2


def demo():
    shapes = [Circle(3), Rectangle(4, 5), Triangle(6, 8)]
    for shape in shapes:
        print(type(shape).__name__, "area:", round(shape.calculate_area(), 2))


if __name__ == "__main__":
    demo()
