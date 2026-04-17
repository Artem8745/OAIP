"""
Задача 3: Форматирование дат
Функция для форматирования даты в различных представлениях.
"""

from datetime import date, datetime


class DateFormatter:
    """Класс для форматирования дат в различных форматах."""
    
    # Словари для русского форматирования
    MONTHS_RU = {
        1: "января", 2: "февраля", 3: "марта", 4: "апреля",
        5: "мая", 6: "июня", 7: "июля", 8: "августа",
        9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
    }
    
    MONTHS_EN = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }
    
    MONTHS_EN_SHORT = {
        1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr",
        5: "May", 6: "Jun", 7: "Jul", 8: "Aug",
        9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
    }
    
    @classmethod
    def format_russian_full(cls, date_obj):
        """
        Формат: "10 апреля 2026 года"
        """
        day = date_obj.day
        month = cls.MONTHS_RU[date_obj.month]
        year = date_obj.year
        return f"{day} {month} {year} года"
    
    @classmethod
    def format_russian_numeric(cls, date_obj):
        """
        Формат: "10.04.2026"
        """
        return date_obj.strftime("%d.%m.%Y")
    
    @classmethod
    def format_iso(cls, date_obj):
        """
        Формат: "2026-04-10"
        """
        return date_obj.strftime("%Y-%m-%d")
    
    @classmethod
    def format_english_short(cls, date_obj):
        """
        Формат: "Apr 10, 2026"
        """
        month_short = cls.MONTHS_EN_SHORT[date_obj.month]
        return f"{month_short} {date_obj.day:02d}, {date_obj.year}"
    
    @classmethod
    def format_english_full(cls, date_obj):
        """
        Формат: "April 10, 2026"
        """
        month = cls.MONTHS_EN[date_obj.month]
        return f"{month} {date_obj.day}, {date_obj.year}"
    
    @classmethod
    def get_all_formats(cls, date_obj):
        """
        Возвращает все доступные форматы даты.
        """
        return {
            "Русский (полный)": cls.format_russian_full(date_obj),
            "Русский (цифровой)": cls.format_russian_numeric(date_obj),
            "ISO формат": cls.format_iso(date_obj),
            "Английский (краткий)": cls.format_english_short(date_obj),
            "Английский (полный)": cls.format_english_full(date_obj)
        }


def format_date(date_input, format_type="all"):
    """
    Функция для форматирования даты в разных форматах.
    
    Args:
        date_input: дата (строка в формате ДД.ММ.ГГГГ или объект date/datetime)
        format_type: тип формата или "all" для всех форматов
    
    Returns:
        str или dict: отформатированная дата или словарь с форматами
    """
    # Преобразование строки в дату, если необходимо
    if isinstance(date_input, str):
        try:
            date_obj = datetime.strptime(date_input, "%d.%m.%Y").date()
        except ValueError:
            try:
                date_obj = datetime.strptime(date_input, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("Неверный формат даты. Используйте ДД.ММ.ГГГГ или ГГГГ-ММ-ДД")
    elif isinstance(date_input, (date, datetime)):
        date_obj = date_input
        if isinstance(date_obj, datetime):
            date_obj = date_obj.date()
    else:
        raise TypeError("date_input должен быть строкой, date или datetime")
    
    formatter = DateFormatter()
    
    if format_type == "all":
        return formatter.get_all_formats(date_obj)
    elif format_type == "ru_full":
        return formatter.format_russian_full(date_obj)
    elif format_type == "ru_numeric":
        return formatter.format_russian_numeric(date_obj)
    elif format_type == "iso":
        return formatter.format_iso(date_obj)
    elif format_type == "en_short":
        return formatter.format_english_short(date_obj)
    elif format_type == "en_full":
        return formatter.format_english_full(date_obj)
    else:
        raise ValueError(f"Неизвестный тип формата: {format_type}")


def demonstrate_formats():
    """Демонстрация всех форматов даты."""
    test_dates = [
        date(2026, 4, 10),
        date(2023, 1, 5),
        date(2024, 12, 31),
        date.today()
    ]
    
    print("=" * 70)
    print("ДЕМОНСТРАЦИЯ ФОРМАТИРОВАНИЯ ДАТ")
    print("=" * 70)
    
    for test_date in test_dates:
        print(f"\nИсходная дата: {test_date.strftime('%Y-%m-%d')} ({test_date.strftime('%d.%m.%Y')})")
        print("-" * 70)
        
        formats = format_date(test_date)
        for format_name, formatted_date in formats.items():
            print(f"{format_name:25}: {formatted_date}")


def interactive_mode():
    """Интерактивный режим для тестирования форматов."""
    print("\n" + "=" * 70)
    print("ИНТЕРАКТИВНЫЙ РЕЖИМ ФОРМАТИРОВАНИЯ ДАТ")
    print("=" * 70)
    
    while True:
        print("\nВыберите действие:")
        print("  1 - Ввести дату для форматирования")
        print("  2 - Показать демонстрацию на примерах")
        print("  0 - Выход в главное меню")
        
        choice = input("\nВаш выбор: ").strip()
        
        if choice == "0":
            print("Выход из интерактивного режима...")
            break
        elif choice == "2":
            print("\n")
            demonstrate_formats()
            continue
        elif choice != "1":
            print("Неверный выбор. Попробуйте снова.")
            continue
        
        # Ввод даты
        print("\nВведите дату в одном из форматов:")
        print("  • ДД.ММ.ГГГГ (например, 10.04.2026)")
        print("  • ГГГГ-ММ-ДД (например, 2026-04-10)")
        print("  • Enter - использовать сегодняшнюю дату")
        print("  • 0 - вернуться в меню")
        
        user_input = input("\nДата: ").strip()
        
        if user_input == "0":
            continue
        
        try:
            if not user_input:
                date_obj = date.today()
                print(f"\nИспользуется сегодняшняя дата: {date_obj.strftime('%d.%m.%Y')}")
            else:
                date_obj = user_input
            
            print("\n" + "=" * 70)
            print("РЕЗУЛЬТАТЫ ФОРМАТИРОВАНИЯ:")
            print("=" * 70)
            formats = format_date(date_obj)
            for format_name, formatted_date in formats.items():
                print(f"{format_name:25}: {formatted_date}")
            print("=" * 70)
            
            # Спрашиваем, хочет ли пользователь продолжить
            again = input("\nХотите ввести другую дату? (y/n): ").strip().lower()
            if again not in ['y', 'yes', 'да', 'д']:
                print("Выход из интерактивного режима...")
                break
            
        except (ValueError, TypeError) as e:
            print(f"\nОшибка: {e}")
            print("Пожалуйста, попробуйте снова.")


def main():
    """Главная функция."""
    while True:
        print("\n" + "=" * 70)
        print("ПРОГРАММА ФОРМАТИРОВАНИЯ ДАТ")
        print("=" * 70)
        print("1 - Демонстрация всех форматов на примерах")
        print("2 - Интерактивный режим (ввод своей даты)")
        print("0 - Выход")
        print("=" * 70)
        
        choice = input("\nВыберите режим: ").strip()
        
        if choice == "1":
            print("\n")
            demonstrate_formats()
            input("\nНажмите Enter для продолжения...")
        elif choice == "2":
            interactive_mode()
        elif choice == "0":
            print("\nДо свидания!")
            break
        else:
            print("\nНеверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()