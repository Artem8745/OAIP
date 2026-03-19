class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
        print(f'Оценка {grade} добавлена студенту {self.name}')
    
    def average_grade(self):
        if not self.grades:
            return 0
        return round((sum(self.grades) / len(self.grades)), 2)


class Group:
    def __init__(self, group_name):
        self.group_name = group_name
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
        print(f'Студент {student.name} добавлен в группу {self.group_name}')
    
    def show_top(self):
        if not self.students:
            print("Группа пуста")
            return None
        
        best_student = None
        best_average = -1
        
        for student in self.students:
            avg = student.average_grade()
            print(f"Средний балл {student.name}: {avg}")
            
            if avg > best_average:
                best_average = avg
                best_student = student
        
        print(f"\nЛучший студент в группе {self.group_name}: {best_student.name}")
        print(f"Его средний балл: {best_average}")
        return best_student


# Проверка
# Создаем студентов
student1 = Student('Петр')
student2 = Student('Анна')
student3 = Student('Иван')

# Добавляем оценки (по 3-4 оценки каждому)
student1.add_grade(5)
student1.add_grade(5)
student1.add_grade(4)
student1.add_grade(3)

student2.add_grade(5)
student2.add_grade(4)
student2.add_grade(5)
student2.add_grade(5)

student3.add_grade(3)
student3.add_grade(4)
student3.add_grade(3)
student3.add_grade(4)

# Создаем группу и добавляем студентов
group = Group('Группа 101')
group.add_student(student1)
group.add_student(student2)
group.add_student(student3)

print("\n" + "="*40)
print("Анализ успеваемости группы:")
print("="*40)

# Выводим лучшего студента
group.show_top()