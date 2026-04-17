"""
Модуль Group - класс для представления учебной группы.
"""
from datetime import datetime
from mypackage.models.student import Student

class Group:
    """
    Класс, представляющий учебную группу.
    Атрибуты:
        name (str): Название группы
        students (list): Список студентов в группе
        curator (str): Куратор группы
    """
    def __init__(self, name, curator=None):
        """
        Инициализация группы.
        Args:
            name (str): Название группы
            curator (str, optional): Куратор группы
        """
        self.name = name
        self.curator = curator
        self.students = []
        self.created_at = datetime.now()

    def add_student(self, student):
        """Добавляет студента в группу."""
        if not isinstance(student, Student):
            print("❌ Ошибка: можно добавлять только объекты Student")
            return False
        
        self.students.append(student)
        print(f"✅ Студент {student.get_full_name()} добавлен в группу {self.name}")
        return True

    def remove_student(self, student_id):
        """Удаляет студента из группы по ID."""
        for i, student in enumerate(self.students):
            if student.student_id == student_id:
                removed = self.students.pop(i)
                print(f"✅ Студент {removed.get_full_name()} удален из группы {self.name}")
                return removed
        print(f"❌ Студент с ID {student_id} не найден")
        return None

    def get_group_average(self):
        """Возвращает средний балл группы."""
        if not self.students:
            return 0
        total = sum(s.get_average_grade() for s in self.students)
        return total / len(self.students)

    def get_best_student(self):
        """Возвращает лучшего студента группы."""
        if not self.students:
            return None
        return max(self.students, key=lambda s: s.get_average_grade())

    def get_students_count(self):
        """Возвращает количество студентов."""
        return len(self.students)

    def to_dict(self):
        """Преобразует объект в словарь."""
        return {
            'name': self.name,
            'curator': self.curator,
            'students_count': self.get_students_count(),
            'average_grade': self.get_group_average(),
            'students': [s.to_dict() for s in self.students],
            'created_at': self.created_at.isoformat() if isinstance(self.created_at, datetime) else str(self.created_at)
        }

    def __str__(self):
        return f"Group: {self.name} (студентов: {len(self.students)})"