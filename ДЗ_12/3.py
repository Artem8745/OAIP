import random
import time
from typing import List, Dict

# Создаем список студентов
def generate_students(count: int = 10000) -> List[Dict]:
    """Генерирует список студентов со случайными данными"""
    names = ["Алексей", "Мария", "Дмитрий", "Екатерина", "Иван", "Анна", 
             "Сергей", "Ольга", "Павел", "Наталья", "Артем", "Елена",
             "Максим", "Татьяна", "Андрей", "Юлия", "Николай", "Анастасия",
             "Владимир", "Ксения"]
    
    groups = ["ИС-101", "ИС-102", "ПМ-201", "ПМ-202", "ИВТ-301", "ИВТ-302",
              "БИ-101", "БИ-102", "ЭК-201", "ЭК-202"]
    
    students = []
    for _ in range(count):
        student = {
            "имя": random.choice(names),
            "группа": random.choice(groups),
            "средний_балл": round(random.uniform(3.0, 5.0), 2)
        }
        students.append(student)
    
    return students

# Линейный поиск по имени
def linear_search_by_name(students: List[Dict], name: str) -> List[Dict]:
    """Линейный поиск студентов по имени"""
    results = []
    for student in students:
        if student["имя"] == name:
            results.append(student)
    return results

# Бинарный поиск по среднему баллу
def binary_search_by_grade(students: List[Dict], target_grade: float) -> List[Dict]:
    """Бинарный поиск студентов с заданным средним баллом"""
    # Сортируем по среднему баллу
    sorted_students = sorted(students, key=lambda x: x["средний_балл"])
    
    results = []
    left, right = 0, len(sorted_students) - 1
    
    # Сначала находим одного студента с нужным баллом
    found_index = -1
    while left <= right:
        mid = (left + right) // 2
        mid_grade = sorted_students[mid]["средний_балл"]
        
        if abs(mid_grade - target_grade) < 0.001:  # Сравниваем с погрешностью
            found_index = mid
            break
        elif mid_grade < target_grade:
            left = mid + 1
        else:
            right = mid - 1
    
    # Если нашли, ищем всех с таким же баллом слева и справа
    if found_index != -1:
        # Ищем влево
        i = found_index
        while i >= 0 and abs(sorted_students[i]["средний_балл"] - target_grade) < 0.001:
            results.append(sorted_students[i])
            i -= 1
        
        # Ищем вправо (начиная со следующего)
        i = found_index + 1
        while i < len(sorted_students) and abs(sorted_students[i]["средний_балл"] - target_grade) < 0.001:
            results.append(sorted_students[i])
            i += 1
    
    return results

# Основная программа
print("Создание списка из 10 000 студентов...")
students = generate_students(10000)

# Выводим первых 5 студентов для примера
print("\nПримеры студентов:")
for student in students[:5]:
    print(f"  {student['имя']}, группа {student['группа']}, средний балл: {student['средний_балл']}")

# Поиск по имени (линейный)
search_name = random.choice(students)["имя"]
print(f"\n1. Поиск студентов с именем '{search_name}' (линейный поиск)")

start_time = time.time()
found_by_name = linear_search_by_name(students, search_name)
linear_time = time.time() - start_time

print(f"   Найдено студентов: {len(found_by_name)}")
print(f"   Время поиска: {linear_time:.6f} секунд")
if found_by_name:
    print(f"   Пример: {found_by_name[0]['имя']}, группа {found_by_name[0]['группа']}, балл: {found_by_name[0]['средний_балл']}")

# Поиск по среднему баллу (бинарный)
search_grade = random.choice(students)["средний_балл"]
print(f"\n2. Поиск студентов со средним баллом {search_grade} (бинарный поиск)")

# Замеряем время с учетом сортировки
start_time = time.time()
found_by_grade = binary_search_by_grade(students, search_grade)
binary_time = time.time() - start_time

print(f"   Найдено студентов: {len(found_by_grade)}")
print(f"   Время поиска (включая сортировку): {binary_time:.4f} секунд")
if found_by_grade:
    print(f"   Пример: {found_by_grade[0]['имя']}, группа {found_by_grade[0]['группа']}, балл: {found_by_grade[0]['средний_балл']}")

# Если нужно продемонстрировать бинарный поиск без учета сортировки
# (отдельно замеряем только поиск в уже отсортированном массиве)
sorted_students = sorted(students, key=lambda x: x["средний_балл"])
start_time = time.time()
# Используем тот же алгоритм, но на уже отсортированном массиве
results = []
left, right = 0, len(sorted_students) - 1
found_index = -1
while left <= right:
    mid = (left + right) // 2
    if abs(sorted_students[mid]["средний_балл"] - search_grade) < 0.001:
        found_index = mid
        break
    elif sorted_students[mid]["средний_балл"] < search_grade:
        left = mid + 1
    else:
        right = mid - 1

if found_index != -1:
    i = found_index
    while i >= 0 and abs(sorted_students[i]["средний_балл"] - search_grade) < 0.001:
        results.append(sorted_students[i])
        i -= 1
    i = found_index + 1
    while i < len(sorted_students) and abs(sorted_students[i]["средний_балл"] - search_grade) < 0.001:
        results.append(sorted_students[i])
        i += 1

binary_only_time = time.time() - start_time

# Сравнение
print(f"\n{'='*50}")
print(f"Сравнение времени выполнения:")
print(f"  Линейный поиск по имени: {linear_time:.6f} сек")
print(f"  Бинарный поиск по баллу (с сортировкой): {binary_time:.4f} сек")
print(f"  Бинарный поиск по баллу (без сортировки): {binary_only_time:.6f} сек")