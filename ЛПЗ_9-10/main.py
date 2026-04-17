"""
Главная программа для демонстрации работы с пакетом mypackage.
"""
import json
from datetime import datetime

# Импортируем из нашего пакета
from mypackage import (
    Student,
    Group,
    APIClient,
    validate_email,
    validate_age,
    format_student_info,
    format_group_report,
    print_colored
)

def demo_package_usage():
    """Демонстрация работы с пакетом mypackage."""
    print_colored("\n" + "=" * 60, "blue")
    print_colored("ДЕМОНСТРАЦИЯ РАБОТЫ ПАКЕТА mypackage", "blue")
    print_colored("=" * 60, "blue")
    
    # ========== 1. Создание студентов ==========
    print_colored("\n1. СОЗДАНИЕ СТУДЕНТОВ", "yellow")
    
    students_data = [
        ("Иван", "Петров", 19, "ivan.petrov@example.com"),
        ("Анна", "Сидорова", 20, "anna.s@example.com"),
        ("Петр", "Иванов", 18, "petr.ivanov"),
        ("Мария", "Кузнецова", 21, "maria@example.com"),
        ("Алексей", "Смирнов", 19, "alexey@domain.ru")
    ]
    
    students = []
    for first, last, age, email in students_data:
        # Валидируем данные
        valid, msg = validate_email(email)
        if not valid:
            print(f"⚠️ {msg} для {email}")
            email = None
        
        valid, msg = validate_age(age)
        if not valid:
            print(f"⚠️ {msg} для {first} {last}")
            age = 18  # Значение по умолчанию
        
        student = Student(first, last, age, email)
        students.append(student)
        print(f"✅ Создан: {student}")
    
    # ========== 2. Добавление оценок ==========
    print_colored("\n2. ДОБАВЛЕНИЕ ОЦЕНОК", "yellow")
    
    grades_data = [
        (0, 5, "Python"),
        (0, 4, "Математика"),
        (0, 5, "Физика"),
        (1, 5, "Python"),
        (1, 5, "Математика"),
        (1, 4, "Физика"),
        (2, 3, "Python"),
        (2, 4, "Математика"),
        (2, 3, "Физика"),
        (3, 5, "Python"),
        (3, 5, "Математика"),
        (3, 5, "Физика"),
        (4, 4, "Python"),
        (4, 4, "Математика"),
        (4, 5, "Физика")
    ]
    
    for student_idx, grade, subject in grades_data:
        if student_idx < len(students):
            students[student_idx].add_grade(grade, subject)
    
    # ========== 3. Создание группы ==========
    print_colored("\n3. СОЗДАНИЕ ГРУППЫ", "yellow")
    
    group = Group("ПИН-231", curator="Иванова М.А.")
    for student in students:
        group.add_student(student)
    
    # Выводим отчет по группе
    print(format_group_report(group))
    
    # ========== 4. Работа с внешним API ==========
    print_colored("\n4. РАБОТА С ВНЕШНИМ API", "yellow")
    
    client = APIClient()
    
    # Получаем посты
    print_colored("\n📡 Получение постов с API...", "blue")
    posts = client.get_posts(5)
    
    if posts:
        print_colored("\nПоследние посты:", "green")
        for i, post in enumerate(posts, 1):
            print(f"   {i}. {post['title'][:60]}...")
            print(f"      Автор ID: {post['userId']}")
        print()
    
    # Получаем цитату
    print_colored("📖 Получение случайной цитаты...", "blue")
    quote = client.get_random_quote()
    if quote:
        print_colored(f"\n\"{quote['text']}\"", "yellow")
        print_colored(f" — {quote['author']}\n", "green")
    
    # ========== 5. Форматирование вывода ==========
    print_colored("\n5. ФОРМАТИРОВАНИЕ ВЫВОДА", "yellow")
    
    for student in students[:2]:  # Показываем первых двух студентов
        print(format_student_info(student))
    
    # ========== 6. Сохранение данных ==========
    print_colored("\n6. СОХРАНЕНИЕ ДАННЫХ", "yellow")
    
    # Сохраняем информацию о группе в JSON
    group_data = group.to_dict()
    with open("mypackage/data/group_data.json", "w", encoding="utf-8") as f:
        json.dump(group_data, f, ensure_ascii=False, indent=2)
    print_colored("✅ Данные группы сохранены в mypackage/data/group_data.json", "green")
    
    # Сохраняем информацию об API запросах
    api_stats = client.get_statistics()
    with open("mypackage/data/api_stats.json", "w", encoding="utf-8") as f:
        json.dump(api_stats, f, ensure_ascii=False, indent=2)
    print_colored("✅ Статистика API сохранена в mypackage/data/api_stats.json", "green")
    
    # ========== Итог ==========
    print_colored("\n" + "=" * 60, "blue")
    print_colored("РАБОТА ЗАВЕРШЕНА УСПЕШНО!", "green")
    print_colored("=" * 60, "blue")
    print(f"\n📊 Статистика:")
    print(f"   • Всего студентов: {len(students)}")
    print(f"   • Средний балл группы: {group.get_group_average():.2f}")
    print(f"   • Всего API запросов: {api_stats['total_requests']}")
    print(f"   • Базовый URL API: {api_stats['base_url']}")

def interactive_mode():
    """Интерактивный режим работы."""
    print_colored("\n" + "=" * 50, "blue")
    print_colored("ИНТЕРАКТИВНЫЙ РЕЖИМ", "blue")
    print_colored("=" * 50, "blue")
    
    client = APIClient()
    
    while True:
        print("\nВыберите действие:")
        print("1. Получить посты")
        print("2. Получить пользователей")
        print("3. Получить случайную цитату")
        print("4. Показать статистику запросов")
        print("5. Показать случайную цитату (новая)")  # НОВЫЙ ПУНКТ
        print("0. Выход")
        
        choice = input("\nВаш выбор: ").strip()
        
        if choice == "0":
            print_colored("До свидания!", "green")
            break
        elif choice == "1":
            try:
                limit = int(input("Количество постов (по умолчанию 5): ") or "5")
                posts = client.get_posts(limit)
                if posts:
                    print_colored(f"\n--- ПОСТЫ ({len(posts)}) ---", "yellow")
                    for post in posts:
                        print(f"\n📌 {post['title']}")
                        print(f"   {post['body'][:100]}...")
            except ValueError:
                print("❌ Некорректный ввод")
        elif choice == "2":
            users = client.get_users()
            if users:
                print_colored(f"\n--- ПОЛЬЗОВАТЕЛИ ({len(users)}) ---", "yellow")
                for user in users:
                    print(f"\n👤 {user['name']}")
                    print(f"   📧 {user['email']}")
                    print(f"   🏙️ {user['address']['city']}")
        elif choice == "3" or choice == "5":  # ОБЪЕДИНЯЕМ СУЩЕСТВУЮЩИЙ И НОВЫЙ ПУНКТ
            print_colored("\n📖 Получение случайной цитаты...", "blue")
            quote = client.get_random_quote()
            if quote:
                print_colored("\n" + "="*60, "yellow")
                print_colored("📜 ЦИТАТА ДНЯ", "yellow")
                print_colored("="*60, "yellow")
                print_colored(f"\n\"{quote['text']}\"", "green")
                print_colored(f"\n— {quote['author']}", "blue")
                if quote.get('tags'):
                    print_colored(f"🏷️ Теги: {', '.join(quote['tags'])}", "yellow")
                print_colored("\n" + "="*60, "yellow")
            else:
                print_colored("❌ Не удалось получить цитату", "red")
        elif choice == "4":
            stats = client.get_statistics()
            print_colored("\n--- СТАТИСТИКА ---", "yellow")
            for key, value in stats.items():
                print(f"   {key}: {value}")
        else:
            print_colored("❌ Неверный выбор. Попробуйте снова.", "red")

def main():
    """Главная функция программы."""
    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║      ЛАБОРАТОРНАЯ РАБОТА: СОЗДАНИЕ ПАКЕТА И РАБОТА С API ║
║                                                          ║
║            Пакет: mypackage                              ║
║            Версия: 1.0.0                                 ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
    """)
    
    while True:
        print("\nВыберите режим работы:")
        print("1. Демонстрация пакета (создание студентов, группы, API)")
        print("2. Интерактивный режим (работа с API)")
        print("0. Выход")
        
        choice = input("\nВаш выбор: ").strip()
        
        if choice == "0":
            print("До свидания!")
            break
        elif choice == "1":
            demo_package_usage()
        elif choice == "2":
            interactive_mode()
        else:
            print("❌ Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()