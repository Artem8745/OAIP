"""
Основная программа для демонстрации безопасного чтения файлов.
"""

from safe_file_reader import FileReader
import os

def analyze_student_data(reader):
    """Анализирует данные студентов из JSON."""
    print("\n" + "=" * 60)
    print("АНАЛИЗ ДАННЫХ СТУДЕНТОВ (JSON)")
    print("=" * 60)

    # Пробуем прочитать файл
    data, success = reader.read_json_file("students.json")

    if not success:
        print("Не удалось прочитать файл студентов")
        return

    # Анализируем данные
    students = data.get("students", [])
    teachers = data.get("teachers", [])

    print(f"\nНайдено студентов: {len(students)}")
    print(f"Найдено преподавателей: {len(teachers)}")

    # Статистика по студентам
    if students:
        print("\n--- СТУДЕНТЫ ---")
        total_age = 0
        all_grades = []

        for student in students:
            name = student.get("name", "Неизвестно")
            age = student.get("age", 0)
            group = student.get("group", "Не указана")
            grades = student.get("grades", [])

            total_age += age
            all_grades.extend(grades)

            avg_grade = sum(grades) / len(grades) if grades else 0
            print(f"  {name} ({group}): {age} лет, средний балл: {avg_grade:.2f}")

        # Общая статистика
        avg_age = total_age / len(students)
        avg_total = sum(all_grades) / len(all_grades) if all_grades else 0

        print(f"\n  Средний возраст студентов: {avg_age:.1f} лет")
        print(f"  Общий средний балл: {avg_total:.2f}")

def analyze_grades_data(reader):
    """Анализирует данные оценок из CSV."""
    print("\n" + "=" * 60)
    print("АНАЛИЗ ОЦЕНОК СТУДЕНТОВ (CSV)")
    print("=" * 60)

    # Пробуем прочитать файл
    headers, data, success = reader.read_csv_file("grades.csv")

    if not success:
        print("Не удалось прочитать файл с оценками")
        return

    print(f"\nЗаголовки: {headers}")
    print(f"Найдено записей: {len(data)}")

    if not data:
        return

    # Анализируем данные
    print("\n--- ДАННЫЕ СТУДЕНТОВ ---")

    # Индексы столбцов
    name_idx = 0
    group_idx = 1

    # Собираем оценки по предметам
    subjects = headers[2:] if headers else ["Python", "Математика", "Физика"]
    grades_by_subject = {subject: [] for subject in subjects}

    for row in data:
        name = row[name_idx] if len(row) > name_idx else "Неизвестно"
        group = row[group_idx] if len(row) > group_idx else "Не указана"

        print(f"\n  {name} ({group}):")

        for i, subject in enumerate(subjects):
            grade_idx = i + 2  # Пропускаем ФИО и Группу

            if len(row) > grade_idx:
                try:
                    grade = int(row[grade_idx])
                    grades_by_subject[subject].append(grade)
                    print(f"    {subject}: {grade}")
                except ValueError:
                    print(f"    {subject}: Некорректные данные")

    # Статистика по предметам
    print("\n--- СТАТИСТИКА ПО ПРЕДМЕТАМ ---")
    for subject, grades in grades_by_subject.items():
        if grades:
            avg = sum(grades) / len(grades)
            max_grade = max(grades)
            min_grade = min(grades)
            print(f"\n  {subject}:")
            print(f"    Средний: {avg:.2f}")
            print(f"    Максимум: {max_grade}")
            print(f"    Минимум: {min_grade}")

def demonstrate_error_handling(reader):
    """Демонстрирует обработку различных ошибок."""
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ОБРАБОТКИ ОШИБОК")
    print("=" * 60)

    # 1. Файл не существует
    print("\n1. Попытка чтения несуществующего файла:")
    data, success = reader.read_json_file("ne_sushestvuet.json")

    # 2. Некорректный JSON
    print("\n2. Попытка чтения битого JSON:")
    data, success = reader.read_json_file("broken.json")

    # 3. Попытка записи в защищенную директорию (на Windows эта ошибка может не возникнуть, если нет диска C:\system)
    print("\n3. Попытка записи в системную директорию:")
    success = reader.write_json_file("/system/test.json", {"test": "data"})

    # 4. Чтение файла не того формата
    print("\n4. Попытка прочитать JSON как CSV:")
    headers, data, success = reader.read_csv_file("students.json")

    # 5. Создание нового файла
    print("\n5. Создание нового JSON файла:")
    new_data = {
        "test": "Это тестовые данные",
        "number": 42,
        "list": [1, 2, 3]
    }
    reader.write_json_file("test_output.json", new_data)

    # 6. Создание нового CSV файла
    print("\n6. Создание нового CSV файла:")
    csv_data = [
        ["Иван", 25, "Москва"],
        ["Анна", 23, "СПб"],
        ["Петр", 30, "Казань"]
    ]
    headers = ["Имя", "Возраст", "Город"]
    reader.write_csv_file("test_output.csv", csv_data, headers)

def main():
    """Основная функция программы."""
    print("=" * 60)
    print("ПРОГРАММА ДЛЯ БЕЗОПАСНОГО ЧТЕНИЯ ФАЙЛОВ")
    print("=" * 60)

    # Создаем читатель файлов
    reader = FileReader()

    # Демонстрируем анализ данных
    analyze_student_data(reader)
    analyze_grades_data(reader)

    # Демонстрируем обработку ошибок
    demonstrate_error_handling(reader)

    # Показываем статистику
    reader.display_statistics()

    # Управление из консоли
    interactive_mode(reader)

    print("\n" + "=" * 60)
    print("Проверьте файл file_operations.log для просмотра логов")
    print("=" * 60)

def interactive_mode(reader):
    """Интерактивный режим работы с файлами."""
    while True:
        print("\n" + "=" * 50)
        print("ИНТЕРАКТИВНЫЙ РЕЖИМ")
        print("=" * 50)
        print("1. Прочитать JSON файл")
        print("2. Прочитать CSV файл")
        print("3. Записать данные в JSON")
        print("4. Записать данные в CSV")
        print("5. Показать статистику")
        print("0. Выйти")

        choice = input("\nВыберите действие: ").strip()

        if choice == "0":
            break
        elif choice == "1":
            filename = input("Введите имя JSON файла: ").strip()
            data, success = reader.read_json_file(filename)
            if success:
                print(f"Прочитано {len(data)} записей")
                print(data)
        elif choice == "2":
            filename = input("Введите имя CSV файла: ").strip()
            delim = input("Разделитель (по умолчанию ,): ").strip() or ","
            headers, data, success = reader.read_csv_file(filename, delim)
            if success:
                print(f"Заголовки: {headers}")
                print(f"Данных: {len(data)}")
                for row in data[:5]:  # Первые 5 строк
                    print(row)
        elif choice == "3":
            filename = input("Имя файла для сохранения: ").strip()
            data = input("Введите данные в формате JSON: ").strip()
            try:
                import json
                data_obj = json.loads(data)
                reader.write_json_file(filename, data_obj)
            except json.JSONDecodeError as e:
                print(f"❌ Ошибка в JSON: {e}")
        elif choice == "4":
            filename = input("Имя файла для сохранения: ").strip()
            print("Введите данные построчно (пустая строка - конец):")
            headers = input("Заголовки (через запятую): ").strip().split(",")
            data = []
            while True:
                row = input("Строка данных: ").strip()
                if not row:
                    break
                data.append(row.split(","))
            reader.write_csv_file(filename, data, headers)
        elif choice == "5":
            reader.display_statistics()

if __name__ == "__main__":
    main()