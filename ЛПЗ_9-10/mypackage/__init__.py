"""
mypackage - пакет для работы с данными о студентах и внешними API.
Этот пакет предоставляет:
- Модели данных (Student, Group)
- Утилиты для валидации и форматирования
- Клиент для работы с внешними API
Пример использования:
    from mypackage.models import Student
    from mypackage.api import APIClient
    student = Student("Иван", "Петров", 19)
    client = APIClient()
    data = client.get_posts()
"""
# Версия пакета
__version__ = "1.0.0"

# Импортируем основные классы и функции для удобного доступа
from mypackage.models.student import Student
from mypackage.models.group import Group
from mypackage.utils.validators import validate_email, validate_age
from mypackage.utils.formatters import format_student_info, format_grades, format_group_report, print_colored
from mypackage.api.client import APIClient

# Что импортировать при "from mypackage import *"
__all__ = [
    'Student',
    'Group',
    'APIClient',
    'validate_email',
    'validate_age',
    'format_student_info',
    'format_grades',
    'format_group_report',
    'print_colored'
]
print(f"📦 Пакет mypackage версии {__version__} загружен")