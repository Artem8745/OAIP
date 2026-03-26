class SpaceSection:
    """
    Класс, представляющий космический отсек с инкапсулированными параметрами.
    """
    def __init__(self, name, oxygen, temperature, access_code):
        """
        Инициализация отсека.
        
        Аргументы:
            name (str): Название отсека
            oxygen (int): Уровень кислорода (0-100)
            temperature (int): Температура (-50..+50)
            access_code (str): Код доступа (строка из 4 цифр)
        """
        self.name = name  # Публичное поле (не защищено)
        self.__oxygen_level = oxygen      # Приватное поле
        self.__temperature = temperature  # Приватное поле
        self.__access_code = access_code  # Приватное поле
        self.__captain_password = "admin123"  # Секретный пароль капитана (приватный)

    # ---------------------- ГЕТТЕРЫ ----------------------
    def get_oxygen(self):
        """Возвращает уровень кислорода в отсеке."""
        return f"Уровень кислорода в {self.name}: {self.__oxygen_level}%"

    def get_temperature(self):
        """Возвращает температуру в отсеке."""
        return f"Температура в {self.name}: {self.__temperature}°C"

    def get_access_code(self, password):
        """
        Возвращает код доступа только при правильном пароле капитана.
        
        Аргументы:
            password (str): Пароль капитана для проверки
            
        Возвращает:
            str: Код доступа или сообщение об ошибке
        """
        if password == self.__captain_password:
            return f"Код доступа к {self.name}: {self.__access_code}"
        else:
            return "✖ Доступ запрещен! Неверный пароль капитана!"

    # ---------------------- СЕТТЕРЫ ----------------------
    def set_oxygen(self, level):
        """
        Устанавливает уровень кислорода с проверкой диапазона (0-100).
        
        Аргументы:
            level (int): Новый уровень кислорода
        """
        if 0 <= level <= 100:
            self.__oxygen_level = level
            print(f"✔ Уровень кислорода в {self.name} изменен на {level}%")
        else:
            print("✖ Ошибка! Уровень кислорода должен быть от 0 до 100")

    def set_temperature(self, temp):
        """
        Устанавливает температуру с проверкой диапазона (-50..+50).
        
        Аргументы:
            temp (int): Новая температура
        """
        if -50 <= temp <= 50:
            self.__temperature = temp
            print(f"✔ Температура в {self.name} изменена на {temp}°C")
        else:
            print("✖ Ошибка! Температура должна быть от -50 до +50")

    def set_access_code(self, old_code, new_code):
        """
        Меняет код доступа после проверки старого кода и валидации нового.
        
        Аргументы:
            old_code (str): Текущий код доступа
            new_code (str): Новый код доступа (строка из 4 цифр)
        """
        if old_code == self.__access_code:
            # Проверяем, что новый код состоит из 4 цифр
            if len(str(new_code)) == 4 and str(new_code).isdigit():
                self.__access_code = str(new_code)
                print(f"✔ Код доступа к {self.name} успешно изменен")
            else:
                print("✖ Новый код должен состоять из 4 цифр!")
        else:
            print("✖ Неверный текущий код доступа!")

    # ---------------------- СПЕЦИАЛЬНЫЙ МЕТОД ----------------------
    def emergency_report(self, password):
        """
        Выводит все параметры отсека только при правильном пароле капитана.
        
        Аргументы:
            password (str): Пароль капитана
        """
        if password == self.__captain_password:
            print("\n" + "=" * 40)
            print(f"⚠ АВАРИЙНЫЙ ОТЧЕТ: {self.name}")
            print(f"Кислород: {self.__oxygen_level}%")
            print(f"Температура: {self.__temperature}°C")
            print(f"Код доступа: {self.__access_code}")
            print("=" * 40)
        else:
            print("❌ Только капитан может просматривать аварийные отчеты!")


# ---------------------- ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ: ДОБАВЛЕНИЕ ПАРАМЕТРА ДАВЛЕНИЯ ----------------------
# Создаем расширенный класс с полем __pressure и его валидацией
class AdvancedSpaceSection(SpaceSection):
    """
    Расширенная версия SpaceSection с добавлением параметра давления.
    """
    def __init__(self, name, oxygen, temperature, access_code, pressure):
        """
        Инициализация расширенного отсека.
        
        Аргументы:
            name (str): Название отсека
            oxygen (int): Уровень кислорода (0-100)
            temperature (int): Температура (-50..+50)
            access_code (str): Код доступа (4 цифры)
            pressure (float): Давление (допустимый диапазон 0.8 - 1.2 атмосферы)
        """
        super().__init__(name, oxygen, temperature, access_code)
        self.__pressure = pressure  # Добавляем новое приватное поле

    # Геттер для давления
    def get_pressure(self):
        """Возвращает давление в отсеке."""
        return f"Давление в {self.name}: {self.__pressure} атм"

    # Сеттер для давления с валидацией
    def set_pressure(self, pressure):
        """
        Устанавливает давление с проверкой диапазона (0.8 - 1.2 атм).
        
        Аргументы:
            pressure (float): Новое давление
        """
        if 0.8 <= pressure <= 1.2:
            self.__pressure = pressure
            print(f"✔ Давление в {self.name} изменено на {pressure} атм")
        else:
            print("✖ Ошибка! Давление должно быть в диапазоне 0.8-1.2 атмосферы")

    # Переопределяем аварийный отчет, чтобы включить давление
    def emergency_report(self, password):
        """
        Выводит все параметры (включая давление) при правильном пароле.
        """
        if password == self._SpaceSection__captain_password:  # Доступ к приватному полю родителя
            print("\n" + "=" * 40)
            print(f"⚠ АВАРИЙНЫЙ ОТЧЕТ: {self.name}")
            print(f"Кислород: {self._SpaceSection__oxygen_level}%")
            print(f"Температура: {self._SpaceSection__temperature}°C")
            print(f"Давление: {self.__pressure} атм")
            print(f"Код доступа: {self._SpaceSection__access_code}")
            print("=" * 40)
        else:
            print("❌ Только капитан может просматривать аварийные отчеты!")


# ---------------------- ДИАЛОГОВАЯ СИСТЕМА (С ИСПОЛЬЗОВАНИЕМ input()) ----------------------
def interactive_system():
    """
    Создает диалоговую систему для взаимодействия с пользователем.
    Позволяет управлять отсеком через консоль.
    """
    print("\n" + "=" * 50)
    print("🚀 ДОБРО ПОЖАЛОВАТЬ В СИСТЕМУ УПРАВЛЕНИЯ КОСМИЧЕСКИМ КОРАБЛЕМ")
    print("=" * 50)

    # Создаем отсек для управления
    section = AdvancedSpaceSection(
        name="Командный отсек",
        oxygen=80,
        temperature=21,
        access_code="4321",
        pressure=1.0
    )

    print(f"\n✅ Создан отсек: {section.name}")
    print("Доступные команды:")
    print("  1 - Показать уровень кислорода")
    print("  2 - Показать температуру")
    print("  3 - Показать давление")
    print("  4 - Изменить уровень кислорода")
    print("  5 - Изменить температуру")
    print("  6 - Изменить давление")
    print("  7 - Показать код доступа (требуется пароль капитана)")
    print("  8 - Сменить код доступа")
    print("  9 - Аварийный отчет (требуется пароль капитана)")
    print("  0 - Выход")

    while True:
        print("\n" + "-" * 30)
        choice = input("Выберите команду (0-9): ").strip()

        if choice == "0":
            print("👋 Выход из системы. Берегите себя!")
            break

        elif choice == "1":
            print(section.get_oxygen())

        elif choice == "2":
            print(section.get_temperature())

        elif choice == "3":
            print(section.get_pressure())

        elif choice == "4":
            try:
                val = int(input("Введите новый уровень кислорода (0-100): "))
                section.set_oxygen(val)
            except ValueError:
                print("✖ Ошибка: введите целое число!")

        elif choice == "5":
            try:
                val = int(input("Введите новую температуру (-50..+50): "))
                section.set_temperature(val)
            except ValueError:
                print("✖ Ошибка: введите целое число!")

        elif choice == "6":
            try:
                val = float(input("Введите новое давление (0.8-1.2): "))
                section.set_pressure(val)
            except ValueError:
                print("✖ Ошибка: введите число!")

        elif choice == "7":
            pwd = input("Введите пароль капитана: ")
            print(section.get_access_code(pwd))

        elif choice == "8":
            old = input("Введите текущий код доступа: ")
            new = input("Введите новый код доступа (4 цифры): ")
            section.set_access_code(old, new)

        elif choice == "9":
            pwd = input("Введите пароль капитана: ")
            section.emergency_report(pwd)

        else:
            print("✖ Неизвестная команда. Попробуйте снова.")


# ---------------------- ОСНОВНАЯ ЧАСТЬ (ДЕМОНСТРАЦИЯ) ----------------------
if __name__ == "__main__":
    print("🚀 ЗАПУСК СИСТЕМЫ КОСМИЧЕСКОГО КОРАБЛЯ")
    print("=" * 50)

    # 1. Создаем отсек и демонстрируем работу базового класса
    command_section = SpaceSection("Командный отсек", 80, 21, "4321")

    print("\n📊 НАЧАЛЬНОЕ СОСТОЯНИЕ:")
    print(command_section.get_oxygen())
    print(command_section.get_temperature())

    print("\n🔐 ПРОВЕРКА ДОСТУПА:")
    print(command_section.get_access_code("wrong_password"))
    print(command_section.get_access_code("admin123"))

    print("\n⚙️ ИЗМЕНЕНИЕ ПАРАМЕТРОВ:")
    command_section.set_oxygen(95)
    command_section.set_temperature(100)  # Ошибка!

    print("\n🔑 СМЕНА КОДА ДОСТУПА:")
    command_section.set_access_code("4321", "9999")  # Правильно
    command_section.set_access_code("9999", "777")   # Ошибка (не 4 цифры)

    print("\n📡 АВАРИЙНЫЙ ОТЧЕТ:")
    command_section.emergency_report("user123")
    command_section.emergency_report("admin123")

    # 2. Демонстрация расширенного класса с давлением
    print("\n" + "=" * 50)
    print("🔄 ДЕМОНСТРАЦИЯ РАСШИРЕННОГО КЛАССА (с давлением)")
    print("=" * 50)

    engine_section = AdvancedSpaceSection(
        name="Двигательный отсек",
        oxygen=85,
        temperature=150,  # Некорректное значение, но при инициализации не проверяется
        access_code="5678",
        pressure=1.1
    )

    print(engine_section.get_oxygen())
    print(engine_section.get_temperature())
    print(engine_section.get_pressure())

    # Показываем, что сеттер температуры все равно сработает и отловит ошибку
    engine_section.set_temperature(150)  # Ошибка: температура вне диапазона

    # 3. Запуск диалоговой системы (раскомментируйте, если хотите взаимодействовать)
    # interactive_system()
    
    print("\n✅ Программа завершена. Для интерактивного режима вызовите interactive_system()")