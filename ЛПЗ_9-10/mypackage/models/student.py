"""
Модуль Student - класс для представления студента.
"""
from datetime import datetime

class Student:
    """
    Класс, представляющий студента.
    Атрибуты:
        first_name (str): Имя
        last_name (str): Фамилия
        age (int): Возраст
        student_id (str): Номер студенческого билета
        grades (list): Список оценок
        email (str): Email студента
        created_at (datetime): Дата создания записи
    """
    _id_counter = 1  # Счетчик для генерации ID

    def __init__(self, first_name, last_name, age, email=None):
        """
        Инициализация студента.
        Args:
            first_name (str): Имя
            last_name (str): Фамилия
            age (int): Возраст
            email (str, optional): Email студента
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.student_id = f"STU{Student._id_counter:04d}"
        self.grades = []
        self.created_at = datetime.now()
        Student._id_counter += 1

    def add_grade(self, grade, subject="General"):
        """
        Добавляет оценку студенту.
        Args:
            grade (int): Оценка (2-5)
            subject (str): Предмет
        Returns:
            bool: True если оценка добавлена, False если некорректна
        """
        if not 2 <= grade <= 5:
            print(f"❌ Ошибка: оценка {grade} должна быть от 2 до 5")
            return False
        
        self.grades.append({
            'subject': subject,
            'grade': grade,
            'date': datetime.now()
        })
        print(f"✅ Оценка {grade} по {subject} добавлена")
        return True

    def add_multiple_grades(self, grades_list):
        """
        Добавляет несколько оценок сразу.
        Args:
            grades_list (list): Список словарей с оценками
                               [{"grade": 5, "subject": "Math"}, ...]
        Returns:
            int: Количество успешно добавленных оценок
        """
        success_count = 0
        for grade_item in grades_list:
            grade = grade_item.get('grade')
            subject = grade_item.get('subject', 'General')
            if self.add_grade(grade, subject):
                success_count += 1
        
        print(f"📊 Всего добавлено оценок: {success_count} из {len(grades_list)}")
        return success_count

    def get_average_grade(self):
        """Возвращает средний балл студента."""
        if not self.grades:
            return 0
        total = sum(g['grade'] for g in self.grades)
        return total / len(self.grades)

    def get_full_name(self):
        """Возвращает полное имя студента."""
        return f"{self.last_name} {self.first_name}"

    def to_dict(self):
        """Преобразует объект в словарь для JSON."""
        # Преобразуем оценки, конвертируя datetime в строку
        grades_json = []
        for grade in self.grades:
            grade_copy = grade.copy()
            if isinstance(grade_copy.get('date'), datetime):
                grade_copy['date'] = grade_copy['date'].isoformat()
            grades_json.append(grade_copy)
        
        return {
            'student_id': self.student_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'email': self.email,
            'grades': grades_json,
            'average_grade': self.get_average_grade(),
            'created_at': self.created_at.isoformat() if isinstance(self.created_at, datetime) else str(self.created_at)
        }

    def __str__(self):
        return f"Student: {self.get_full_name()} (ID: {self.student_id}, возраст: {self.age})"

    def __repr__(self):
        return f"Student('{self.first_name}', '{self.last_name}', {self.age})"

# Пример использования модуля (для тестирования)
if __name__ == "__main__":
    # Создаем студента
    student = Student("Иван", "Петров", 19, "ivan@example.com")
    print(student)
    
    # Добавляем оценки по одной
    student.add_grade(5, "Python")
    student.add_grade(4, "Математика")
    
    # Добавляем несколько оценок сразу
    student.add_multiple_grades([
        {"grade": 5, "subject": "Python"},
        {"grade": 4, "subject": "SQL"},
        {"grade": 5, "subject": "Git"}
    ])
    
    # Выводим информацию
    print(f"Средний балл: {student.get_average_grade():.2f}")
    print(f"Количество оценок: {len(student.grades)}")