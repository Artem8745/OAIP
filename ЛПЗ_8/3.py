class Notifier:
    """Базовый класс уведомителя"""
    def send(self, message):
        return f"Отправка: {message}"


class EmailNotifier(Notifier):
    """Email уведомитель"""
    def __init__(self, email_address):
        self.email_address = email_address
    
    def send(self, message):
        # Полиморфизм: метод send работает по-своему для каждого класса
        return f"Email на {self.email_address}: {message}"


class SMSNotifier(Notifier):
    """SMS уведомитель"""
    def __init__(self, phone_number):
        self.phone_number = phone_number
    
    def send(self, message):
        # Полиморфизм: метод send работает по-своему для каждого класса
        return f"SMS на {self.phone_number}: {message}"


class PushNotifier(Notifier):
    """Push уведомитель"""
    def __init__(self, device_token):
        self.device_token = device_token
    
    def send(self, message):
        # Полиморфизм: метод send работает по-своему для каждого класса
        return f"Push на устройство {self.device_token}: {message}"


# Полиморфная функция - принимает любые объекты, у которых есть метод send()
def notify_all(notifiers, message):
    """
    Полиморфизм: функция работает с любыми объектами,
    которые реализуют метод send()
    """
    print(f"\nОтправка: '{message}'")
    print("-" * 40)
    
    for notifier in notifiers:
        # Полиморфизм: один и тот же вызов метода send()
        # дает разный результат в зависимости от типа объекта
        result = notifier.send(message)
        print(result)


# Демонстрация полиморфизма
print("=== Демонстрация полиморфизма ===\n")

# Создаем список разных уведомителей
notifiers = [
    EmailNotifier("userI@example.com"),
    SMSNotifier("+7 (999) 123-45-67"),
    PushNotifier("device_telephon"),
    EmailNotifier("admin@company.com"),  # Еще один email
    SMSNotifier("+7 (888) 765-43-21")    # Еще один SMS
]

# Полиморфизм: одна и та же функция работает с разными типами объектов
print("1. Полиморфизм в действии:")
notify_all(notifiers, "Добро пожаловать!")

print("\n2. Еще один пример полиморфизма:")
notify_all(notifiers, "У вас новое сообщение")

print("\n3. Полиморфизм с разными сообщениями:")
notify_all(notifiers, "Срочное обновление системы!")

# Дополнительная демонстрация полиморфизма
print("\n" + "=" * 40)
print("Полиморфизм в цикле:")
print("=" * 40)

# Создаем список из разных типов уведомителей
different_notifiers = [
    EmailNotifier("test1@mail.com"),
    SMSNotifier("+7 999 111-22-33"),
    PushNotifier("token_xyz789")
]

# Полиморфизм: одинаковый код работает с разными объектами
for notifier in different_notifiers:
    # Один и тот же вызов send() дает разный результат
    print(notifier.send("Тестовое сообщение"))
    print(f"Тип объекта: {type(notifier).__name__}\n")

print("=== Ключевые моменты полиморфизма ===")
print("✓ Один интерфейс (метод send())")
print("✓ Разные реализации (Email, SMS, Push)")
print("✓ Функция notify_all() работает с любыми уведомителями")
print("✓ Легко добавить новый тип уведомителя без изменения существующего кода")