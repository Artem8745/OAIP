"""
Тестирование новых функций самостоятельной работы
"""
from mypackage.models import Student
from mypackage.utils import validate_student_name, print_colored

print_colored("\n" + "="*60, "blue")
print_colored("ТЕСТИРОВАНИЕ НОВЫХ ФУНКЦИЙ", "blue")
print_colored("="*60, "blue")

# Тест 1: add_multiple_grades
print_colored("\n📝 Тест 1: Метод add_multiple_grades", "yellow")
student = Student("Анна", "Иванова", 20)
print(f"Студент: {student.get_full_name()}")

# Добавляем несколько оценок сразу
count = student.add_multiple_grades([
    {"grade": 5, "subject": "Python"},
    {"grade": 4, "subject": "SQL"},
    {"grade": 5, "subject": "Git"}
])
print(f"✅ Добавлено оценок: {count}")
print(f"📊 Средний балл: {student.get_average_grade():.2f}")

# Тест 2: validate_student_name
print_colored("\n📝 Тест 2: Функция validate_student_name", "yellow")
test_cases = [
    ("Анна", "Иванова"),
    ("анна", "Иванова"),
    ("Анна-Мария", "Сидорова-Петрова"),
    ("Анна123", "Иванова"),
    ("", "Иванова")
]

for first, last in test_cases:
    valid, msg = validate_student_name(first, last)
    if valid:
        print_colored(f"✅ {first} {last}: {msg}", "green")
    else:
        print_colored(f"❌ {first} {last}: {msg}", "red")

print_colored("\n" + "="*60, "blue")
print_colored("✅ ТЕСТИРОВАНИЕ ЗАВЕРШЕНО!", "green")
print_colored("="*60, "blue")