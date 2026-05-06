"""Session 2 exercise: Factory pattern for shapes."""
from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side * self.side

def shape_factory(name: str, size: float) -> Shape:
    name = name.lower()
    if name == "circle":
        return Circle(size)
    if name == "square":
        return Square(size)
    raise ValueError("Unknown shape")

if __name__ == "__main__":
    c = shape_factory("circle", 2)
    s = shape_factory("square", 3)
    print("Circle area", c.area())
    print("Square area", s.area())
