from abc import ABC, abstractmethod

# Абстрактний клас
class Car(ABC):
    def __init__(self, brand):
        self.__brand = brand  # Закритий атрибут

    @abstractmethod
    def start_engine(self):
        pass  # Абстрактний метод (обов'язковий для реалізації)

    def info(self):
        return f"This is a {self.__brand} car."  # Метод з імплементацією

    def get_brand(self):
        return self.__brand  # Геттер для закритого атрибута

# Похідний клас "Електромобіль"
class ElectricCar(Car):
    def start_engine(self):
        print(f"{self.get_brand()}: Starting silently...")

# Похідний клас "Бензинове авто"
class GasCar(Car):
    def start_engine(self):
        print(f"{self.get_brand()}: Vroom! Engine roaring...")

# Створюємо колекцію авто
cars = [ElectricCar("Tesla"), GasCar("BMW"), ElectricCar("Nissan"), GasCar("Ford")]

# Викликаємо метод start_engine() для кожного авто
for car in cars:
    car.start_engine()