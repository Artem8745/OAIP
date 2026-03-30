class Employee:
    """Базовый класс - родитель для всех сотрудников"""
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def work(self):
        return f"{self.name} работает"
    
    def get_info(self):
        return f"Сотрудник: {self.name}, Зарплата: {self.salary} руб."


class Developer(Employee):
    """Класс Developer наследует Employee"""
    def __init__(self, name, salary, programming_language):
        # Наследование: вызываем конструктор родителя через super()
        super().__init__(name, salary)
        self.programming_language = programming_language
    
    def write_code(self):
        return f"{self.name} пишет код на {self.programming_language}"
    
    def work(self):
        # Наследование: переопределяем метод родителя
        return f"{self.name} разрабатывает на {self.programming_language}"
    
    def get_info(self):
        # Наследование: расширяем метод родителя
        parent_info = super().get_info()
        return f"{parent_info}, Язык: {self.programming_language}"


class Designer(Employee):
    """Класс Designer наследует Employee"""
    def __init__(self, name, salary, software):
        # Наследование: вызываем конструктор родителя
        super().__init__(name, salary)
        self.software = software
    
    def design(self):
        return f"{self.name} создает дизайн в {self.software}"
    
    def work(self):
        # Наследование: переопределяем метод родителя
        return f"{self.name} создает дизайн в {self.software}"
    
    def get_info(self):
        # Наследование: расширяем метод родителя
        parent_info = super().get_info()
        return f"{parent_info}, Софт: {self.software}"


class Manager(Employee):
    """Класс Manager наследует Employee"""
    def __init__(self, name, salary, team_size):
        # Наследование: вызываем конструктор родителя
        super().__init__(name, salary)
        self.team_size = team_size
    
    def manage(self):
        return f"{self.name} управляет командой из {self.team_size} человек"
    
    def work(self):
        # Наследование: переопределяем метод родителя
        return f"{self.name} управляет командой"
    
    def get_info(self):
        # Наследование: расширяем метод родителя
        parent_info = super().get_info()
        return f"{parent_info}, Команда: {self.team_size} чел."


# Демонстрация наследования
print("=== Демонстрация наследования ===\n")

# Создаем объекты дочерних классов
dev = Developer("Иван", 1000000000000000000000, "Python")
designer = Designer("Анна", 8006666666, "Figma")
manager = Manager("Сергей", 1234567777, 5)

# Проверяем, что все объекты являются наследниками Employee
print("Проверка наследования через isinstance():")
print(f"dev - это Employee? {isinstance(dev, Employee)}")  # True
print(f"designer - это Employee? {isinstance(designer, Employee)}")  # True
print(f"manager - это Employee? {isinstance(manager, Employee)}")  # True

print("\nВызов методов:")
# Дочерние классы имеют доступ к методам родителя
print(dev.get_info())  # Вызван расширенный метод
print(designer.get_info())
print(manager.get_info())

print("\nПереопределенные методы work():")
# Каждый класс переопределил метод work() по-своему
print(dev.work())
print(designer.work())
print(manager.work())

print("\nСпецифические методы дочерних классов:")
print(dev.write_code())
print(designer.design())
print(manager.manage())