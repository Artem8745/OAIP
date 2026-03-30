class Animal:
    """Базовый класс - родитель для всех животных"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        return f"{self.name} издает звук"
    
    def move(self):
        return f"{self.name} двигается"
    
    def get_info(self):
        return f"{self.name}, возраст: {self.age} лет"


class Mammal(Animal):
    """Класс Mammal наследует Animal"""
    def __init__(self, name, age, hair_color):
        # Наследование: вызываем конструктор родителя
        super().__init__(name, age)
        self.hair_color = hair_color
    
    def feed_milk(self):
        return f"{self.name} кормит молоком"
    
    def make_sound(self):
        # Наследование: переопределяем метод родителя
        return f"{self.name} бебекает"
    
    def move(self):
        # Наследование: переопределяем метод родителя
        return f"{self.name} ходит по земле"


class Bird(Animal):
    """Класс Bird наследует Animal"""
    def __init__(self, name, age, wing_span):
        # Наследование: вызываем конструктор родителя
        super().__init__(name, age)
        self.wing_span = wing_span
    
    def fly(self):
        return f"{self.name} летит (размах крыльев: {self.wing_span} м)"
    
    def make_sound(self):
        # Наследование: переопределяем метод родителя
        return f"{self.name} кудахчет"
    
    def move(self):
        # Наследование: переопределяем метод родителя
        return f"{self.name} летает"


class Fish(Animal):
    """Класс Fish наследует Animal"""
    def __init__(self, name, age, water_type):
        # Наследование: вызываем конструктор родителя
        super().__init__(name, age)
        self.water_type = water_type
    
    def swim(self):
        return f"{self.name} плавает в {self.water_type} воде"
    
    def make_sound(self):
        # Наследование: переопределяем метод родителя
        return f"{self.name} булькает"
    
    def move(self):
        # Наследование: переопределяем метод родителя
        return f"{self.name} плавает"


# Демонстрация наследования
print("=== Демонстрация наследования ===\n")

# Создаем объекты дочерних классов
lion = Mammal("Козлик", 50, "белый")
eagle = Bird("Курица", 0.3, 25.9)
salmon = Fish("Лосось", 2, "соленой")

# Проверяем наследование
print("Проверка наследования через isinstance():")
print(f"Козлик - это Animal? {isinstance(lion, Animal)}")  # True
print(f"Курица - это Animal? {isinstance(eagle, Animal)}")  # True
print(f"Лосось - это Animal? {isinstance(salmon, Animal)}")  # True

print("\nДочерние классы имеют доступ к методам родителя:")
# Все дочерние классы могут вызвать метод get_info() от родителя
print(lion.get_info())
print(eagle.get_info())
print(salmon.get_info())

print("\nПереопределенные методы make_sound():")
# Каждый дочерний класс переопределил метод по-своему
print(lion.make_sound())
print(eagle.make_sound())
print(salmon.make_sound())

print("\nПереопределенные методы move():")
print(lion.move())
print(eagle.move())
print(salmon.move())

print("\nСпецифические методы дочерних классов:")
print(lion.feed_milk())
print(eagle.fly())
print(salmon.swim())

print("\nДемонстрация иерархии наследования:")
# Показываем цепочку наследования
print(f"Mammal наследует Animal: {issubclass(Mammal, Animal)}")  # True
print(f"Bird наследует Animal: {issubclass(Bird, Animal)}")  # True
print(f"Fish наследует Animal: {issubclass(Fish, Animal)}")  # True