"""
Подпакет utils - содержит вспомогательные функции.
"""
from mypackage.utils.validators import validate_email, validate_age, validate_grade
from mypackage.utils.formatters import format_student_info, format_grades, format_group_report, print_colored

__all__ = [
    'validate_email',
    'validate_age',
    'validate_grade',
    'format_student_info',
    'format_grades',
    'format_group_report',
    'print_colored'
]
print("🛠️ Подпакет utils загружен")