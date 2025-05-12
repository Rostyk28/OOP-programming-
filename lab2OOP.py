import math
from abc import ABC, abstractmethod

# OCP: Базовий інтерфейс для всіх фігур
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# SRP: Клас відповідає лише за прямокутник
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# SRP: Клас відповідає лише за коло
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# SRP: Клас відповідає лише за виведення
class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    def calculate_areas(self):
        for shape in self.shapes:
            print(f"Площа: {shape.area():.2f}")

# Основна частина програми
def main():
    shapes = [
        Rectangle(4, 5),
        Circle(3)
    ]
    calculator = AreaCalculator(shapes)
    calculator.calculate_areas()

if __name__ == "__main__":
    main()
