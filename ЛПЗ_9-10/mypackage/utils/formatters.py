"""
Модуль formatters - функции для форматирования вывода.
"""
def format_student_info(student):
    """
    Форматирует информацию о студенте для вывода.
    Args:
        student: Объект Student
    Returns:
        str: Отформатированная строка
    """
    separator = "=" * 50
    info = f"""
{separator}
СТУДЕНТ: {student.get_full_name()}
{separator}
📋 ID студента: {student.student_id}
🎂 Возраст: {student.age}
📧 Email: {student.email if student.email else 'Не указан'}
📊 Средний балл: {student.get_average_grade():.2f}
📝 Количество оценок: {len(student.grades)}
📅 Дата создания: {student.created_at.strftime('%d.%m.%Y %H:%M')}
{separator}
"""
    return info

def format_grades(student, show_all=False):
    """
    Форматирует список оценок студента.
    Args:
        student: Объект Student
        show_all (bool): Показывать все оценки или только среднюю
    Returns:
        str: Отформатированная строка с оценками
    """
    if not student.grades:
        return "📝 Оценок пока нет"
    
    if show_all:
        result = f"📊 Оценки студента {student.get_full_name()}:\n"
        for i, grade_info in enumerate(student.grades, 1):
            date = grade_info['date'].strftime('%d.%m')
            result += f"   {i}. {grade_info['subject']}: {grade_info['grade']} ({date})\n"
        return result
    else:
        return f"📊 Средний балл {student.get_full_name()}: {student.get_average_grade():.2f}"

def format_group_report(group):
    """
    Форматирует отчет по группе.
    Args:
        group: Объект Group
    Returns:
        str: Отформатированный отчет
    """
    separator = "=" * 60
    report = f"""
{separator}
ОТЧЕТ ПО ГРУППЕ: {group.name}
{separator}
👨‍🏫 Куратор: {group.curator if group.curator else 'Не назначен'}
👥 Количество студентов: {group.get_students_count()}
📈 Средний балл группы: {group.get_group_average():.2f}
"""
    if group.get_best_student():
        best = group.get_best_student()
        report += f"🏆 Лучший студент: {best.get_full_name()} (ср. балл: {best.get_average_grade():.2f})\n"
    
    report += f"\nСПИСОК СТУДЕНТОВ:\n"
    report += "-" * 40 + "\n"
    
    for i, student in enumerate(group.students, 1):
        report += f"{i:2}. {student.get_full_name():20} | ID: {student.student_id} | Ср.балл: {student.get_average_grade():.2f}\n"
    
    report += separator
    return report

def print_colored(text, color="green"):
    """
    Выводит цветной текст в консоль.
    Args:
        text (str): Текст для вывода
        color (str): Цвет (green, red, yellow, blue)
    """
    colors = {
        "green": "\033[92m",
        "red": "\033[91m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "reset": "\033[0m"
    }
    print(f"{colors.get(color, colors['reset'])}{text}{colors['reset']}")