"""
Задача 1: Калькулятор возраста
Программа запрашивает дату рождения и вычисляет возраст в годах, месяцах и днях,
а также показывает количество дней до следующего дня рождения.
"""

from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta


def calculate_age(birth_date):
    """
    Вычисляет точный возраст в годах, месяцах и днях.
    
    Args:
        birth_date: дата рождения (date или datetime)
    
    Returns:
        tuple: (years, months, days) или None если дата в будущем
    """
    today = date.today()
    
    # Проверка на будущую дату
    if birth_date > today:
        return None
    
    # Используем relativedelta для точного расчета с учетом разной длины месяцев
    delta = relativedelta(today, birth_date)
    return delta.years, delta.months, delta.days


def days_until_next_birthday(birth_date):
    """
    Вычисляет количество дней до следующего дня рождения.
    
    Args:
        birth_date: дата рождения (date или datetime)
    
    Returns:
        int: количество дней до следующего дня рождения
    """
    today = date.today()
    
    # Определяем дату ближайшего дня рождения
    next_birthday = date(today.year, birth_date.month, birth_date.day)
    
    # Если день рождения в этом году уже прошел, берем следующий год
    if next_birthday < today:
        next_birthday = date(today.year + 1, birth_date.month, birth_date.day)
    
    days_left = (next_birthday - today).days
    return days_left


def get_birth_date_from_user():
    """
    Запрашивает дату рождения у пользователя.
    
    Returns:
        date: дата рождения
    """
    while True:
        try:
            birth_input = input("Введите дату рождения в формате ДД.ММ.ГГГГ: ")
            birth_date = datetime.strptime(birth_input, "%d.%m.%Y").date()
            
            # Проверка на реалистичность даты (не слишком старая)
            if birth_date.year < 1900:
                print("Пожалуйста, введите реалистичную дату рождения (после 1900 года)")
                continue
                
            return birth_date
        except ValueError:
            print("Неверный формат даты. Используйте ДД.ММ.ГГГГ (например, 15.05.1990)")


def format_age_string(years, months, days):
    """
    Форматирует строку с возрастом, правильно склоняя слова.
    
    Args:
        years: количество лет
        months: количество месяцев
        days: количество дней
    
    Returns:
        str: отформатированная строка с возрастом
    """
    year_str = "год" if years % 10 == 1 and years % 100 != 11 else \
               "года" if 2 <= years % 10 <= 4 and not (12 <= years % 100 <= 14) else "лет"
    
    month_str = "месяц" if months % 10 == 1 and months % 100 != 11 else \
                "месяца" if 2 <= months % 10 <= 4 and not (12 <= months % 100 <= 14) else "месяцев"
    
    day_str = "день" if days % 10 == 1 and days % 100 != 11 else \
              "дня" if 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14) else "дней"
    
    return f"{years} {year_str}, {months} {month_str}, {days} {day_str}"


def main():
    """Главная функция программы."""
    print("=" * 50)
    print("КАЛЬКУЛЯТОР ВОЗРАСТА")
    print("=" * 50)
    
    # Получаем дату рождения
    birth_date = get_birth_date_from_user()
    
    # Вычисляем возраст
    age = calculate_age(birth_date)
    
    if age is None:
        print("Ошибка: дата рождения не может быть в будущем!")
        return
    
    years, months, days = age
    
    # Вычисляем дни до дня рождения
    days_left = days_until_next_birthday(birth_date)
    
    # Выводим результаты
    print("\n" + "=" * 50)
    print("РЕЗУЛЬТАТЫ РАСЧЕТА")
    print("=" * 50)
    print(f"Дата рождения: {birth_date.strftime('%d.%m.%Y')}")
    print(f"Возраст: {format_age_string(years, months, days)}")
    print(f"До следующего дня рождения осталось: {days_left} дней")
    
    if days_left == 0:
        print("\n🎉 С ДНЕМ РОЖДЕНИЯ! 🎂")
    elif days_left <= 7:
        print(f"\n🎈 Скоро день рождения! Всего {days_left} дней!")


if __name__ == "__main__":
    # Примечание: требуется установка python-dateutil
    # pip install python-dateutil
    try:
        main()
    except ImportError:
        print("Ошибка: требуется установить библиотеку python-dateutil")
        print("Выполните команду: pip install python-dateutil")