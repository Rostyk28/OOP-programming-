import copy

# Базовий клас Prototype
class Prototype:
    def clone(self):
        return copy.deepcopy(self)

# Клас Car успадковує Prototype
class Car(Prototype):
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def display(self):
        print(f"Марка: {self.brand}, Модель: {self.model}, Колір: {self.color}")


def main():
    # Створюємо оригінальний об'єкт
    original_car = Car("Toyota", "Corolla", "Синій")
    print("Оригінальна машина:")
    original_car.display()

    # Клонуємо об'єкт
    cloned_car = original_car.clone()
    cloned_car.color = "Червоний"  # Змінюємо деякі параметри
    print("\nКлонована машина з новим кольором:")
    cloned_car.display()

    # Ще один клон
    another_clone = original_car.clone()
    another_clone.model = "Camry"
    print("\nЩе один клон з іншою моделлю:")
    another_clone.display()

if __name__ == "__main__":
    main()
