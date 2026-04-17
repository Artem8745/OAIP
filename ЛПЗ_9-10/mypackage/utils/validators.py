"""
Модуль validators - функции для валидации данных.
"""
import re

def validate_email(email):
    """
    Проверяет корректность email адреса.
    Args:
        email (str): Email для проверки
    Returns:
        tuple: (is_valid, error_message)
    """
    if not email:
        return False, "Email не может быть пустым"
    
    # Простая проверка формата email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True, "Email корректен"
    else:
        return False, "Некорректный формат email"

def validate_age(age):
    """
    Проверяет корректность возраста.
    Args:
        age: Возраст для проверки
    Returns:
        tuple: (is_valid, error_message)
    """
    if not isinstance(age, (int, float)):
        return False, "Возраст должен быть числом"
    if age < 16:
        return False, "Студент должен быть старше 16 лет"
    if age > 100:
        return False, "Некорректный возраст"
    
    return True, "Возраст корректен"

def validate_grade(grade):
    """
    Проверяет корректность оценки.
    Args:
        grade: Оценка для проверки
    Returns:
        tuple: (is_valid, error_message)
    """
    if not isinstance(grade, (int, float)):
        return False, "Оценка должна быть числом"
    if grade < 2 or grade > 5:
        return False, "Оценка должна быть от 2 до 5"
    return True, "Оценка корректна"

def validate_name(name):
    """
    Проверяет корректность имени/фамилии.
    Args:
        name (str): Имя для проверки
    Returns:
        tuple: (is_valid, error_message)
    """
    if not name or not isinstance(name, str):
        return False, "Имя не может быть пустым"
    if len(name) < 2:
        return False, "Имя должно содержать минимум 2 символа"
    if not name.replace('-', '').replace(' ', '').isalpha():
        return False, "Имя должно содержать только буквы"
    return True, "Имя корректно"

def validate_student_name(first_name, last_name):
    """
    Проверяет корректность имени и фамилии студента.
    Args:
        first_name (str): Имя студента
        last_name (str): Фамилия студента
    Returns:
        tuple: (is_valid, error_message)
    """
    # Проверка на пустоту
    if not first_name or not last_name:
        return False, "Имя и фамилия не могут быть пустыми"
    
    # Проверка на заглавную букву
    if not first_name[0].isupper():
        return False, f"Имя '{first_name}' должно начинаться с заглавной буквы"
    if not last_name[0].isupper():
        return False, f"Фамилия '{last_name}' должна начинаться с заглавной буквы"
    
    # Проверка на буквы (разрешаем дефис)
    def is_valid_name_part(name):
        # Убираем дефисы для проверки
        name_without_hyphen = name.replace('-', '')
        return name_without_hyphen.isalpha()
    
    if not is_valid_name_part(first_name):
        return False, f"Имя '{first_name}' должно содержать только буквы (дефис разрешен)"
    
    if not is_valid_name_part(last_name):
        return False, f"Фамилия '{last_name}' должна содержать только буквы (дефис разрешен)"
    
    return True, f"Имя '{first_name}' и фамилия '{last_name}' корректны"

# Тестирование валидаторов
if __name__ == "__main__":
    # Тест email
    test_emails = ["test@example.com", "invalid-email", "user@domain", "a@b.c"]
    for email in test_emails:
        valid, msg = validate_email(email)
        print(f"Email '{email}': {msg}")
    
    # Тест имени студента
    print("\n" + "="*50)
    test_names = [
        ("Иван", "Петров"),
        ("иван", "Петров"),
        ("Иван", "петров"),
        ("Анна-Мария", "Сидорова"),
        ("Иван123", "Петров"),
        ("", "Петров")
    ]
    
    for first, last in test_names:
        valid, msg = validate_student_name(first, last)
        status = "✅" if valid else "❌"
        print(f"{status} {first} {last}: {msg}")