"""
Тестирование импорта пакета mypackage.
"""
print("=" * 50)
print("ТЕСТИРОВАНИЕ ИМПОРТА ПАКЕТА")
print("=" * 50)

# Тест 1: Импорт всего пакета
print("\n1. Импорт пакета:")
import mypackage
print(f"   Версия: {mypackage.__version__}")
print(f"   Доступные компоненты: {mypackage.__all__}")

# Тест 2: Импорт подпакетов
print("\n2. Импорт подпакетов:")
from mypackage import models
from mypackage import utils
from mypackage import api

# Тест 3: Импорт конкретных классов
print("\n3. Импорт классов:")
from mypackage.models import Student, Group
from mypackage.utils import validate_email, format_student_info
from mypackage.api import APIClient

print("\n✅ Все импорты выполнены успешно!")