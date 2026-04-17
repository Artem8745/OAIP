"""
Задача 2: Планировщик задач
Программа для учета задач с датами выполнения.
Показывает задачи на сегодня, просроченные и на ближайшие 7 дней.
"""

from datetime import date, datetime, timedelta
import json
import os


class TaskScheduler:
    """Класс для управления задачами."""
    
    def __init__(self, filename="tasks.json"):
        """
        Инициализация планировщика.
        
        Args:
            filename: имя файла для хранения задач
        """
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        """Загружает задачи из файла."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    tasks_data = json.load(f)
                    for task_data in tasks_data:
                        task_data['date'] = datetime.strptime(
                            task_data['date'], "%Y-%m-%d"
                        ).date()
                    self.tasks = tasks_data
            except (json.JSONDecodeError, KeyError):
                print("Ошибка чтения файла задач. Создан новый список.")
                self.tasks = []
        else:
            self.tasks = []
    
    def save_tasks(self):
        """Сохраняет задачи в файл."""
        tasks_data = []
        for task in self.tasks:
            task_copy = task.copy()
            task_copy['date'] = task_copy['date'].strftime("%Y-%m-%d")
            tasks_data.append(task_copy)
        
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(tasks_data, f, ensure_ascii=False, indent=2)
    
    def add_task(self, title, task_date, description=""):
        """
        Добавляет новую задачу.
        
        Args:
            title: название задачи
            task_date: дата выполнения
            description: описание задачи
        """
        task = {
            'title': title,
            'date': task_date,
            'description': description,
            'completed': False,
            'created': date.today().strftime("%Y-%m-%d")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✓ Задача '{title}' добавлена")
    
    def get_tasks_for_date(self, target_date):
        """
        Возвращает задачи на указанную дату.
        
        Args:
            target_date: дата для фильтрации
        
        Returns:
            list: список задач на указанную дату
        """
        return [task for task in self.tasks 
                if task['date'] == target_date and not task['completed']]
    
    def get_overdue_tasks(self):
        """
        Возвращает просроченные задачи.
        
        Returns:
            list: список просроченных задач
        """
        today = date.today()
        return [task for task in self.tasks 
                if task['date'] < today and not task['completed']]
    
    def get_tasks_next_week(self):
        """
        Возвращает задачи на ближайшие 7 дней.
        
        Returns:
            dict: словарь с задачами по датам
        """
        today = date.today()
        week_end = today + timedelta(days=7)
        tasks_by_date = {}
        
        for task in self.tasks:
            if today <= task['date'] <= week_end and not task['completed']:
                date_str = task['date'].strftime("%Y-%m-%d")
                if date_str not in tasks_by_date:
                    tasks_by_date[date_str] = []
                tasks_by_date[date_str].append(task)
        
        return dict(sorted(tasks_by_date.items()))
    
    def mark_completed(self, task_index):
        """
        Отмечает задачу как выполненную.
        
        Args:
            task_index: индекс задачи в списке
        """
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
            self.save_tasks()
            print(f"✓ Задача '{self.tasks[task_index]['title']}' выполнена")
        else:
            print("Неверный индекс задачи")
    
    def display_tasks(self, tasks, title="Задачи"):
        """
        Отображает список задач.
        
        Args:
            tasks: список задач для отображения
            title: заголовок
        """
        if not tasks:
            print(f"\n{title}: нет задач")
            return
        
        print(f"\n{title}:")
        print("-" * 60)
        for i, task in enumerate(tasks):
            status = "✓" if task['completed'] else "○"
            date_str = task['date'].strftime("%d.%m.%Y")
            print(f"{i+1}. [{status}] {task['title']}")
            print(f"   Дата: {date_str}")
            if task['description']:
                print(f"   Описание: {task['description']}")
        print("-" * 60)


def get_date_from_user(prompt="Введите дату (ДД.ММ.ГГГГ): "):
    """
    Запрашивает дату у пользователя.
    
    Args:
        prompt: текст запроса
    
    Returns:
        date: введенная дата
    """
    while True:
        try:
            date_input = input(prompt)
            if not date_input:  # Если пустой ввод - сегодняшняя дата
                return date.today()
            return datetime.strptime(date_input, "%d.%m.%Y").date()
        except ValueError:
            print("Неверный формат даты. Используйте ДД.ММ.ГГГГ")


def main():
    """Главная функция программы."""
    scheduler = TaskScheduler()
    
    # Добавляем тестовые задачи, если список пуст
    if not scheduler.tasks:
        today = date.today()
        scheduler.add_task("Подготовить отчет", today - timedelta(days=2), "Квартальный отчет")
        scheduler.add_task("Встреча с клиентом", today, "Обсуждение проекта")
        scheduler.add_task("Сходить в спортзал", today + timedelta(days=2))
        scheduler.add_task("Оплатить счета", today + timedelta(days=5))
        scheduler.add_task("Позвонить маме", today + timedelta(days=7))
    
    while True:
        print("\n" + "=" * 60)
        print("ПЛАНИРОВЩИК ЗАДАЧ")
        print("=" * 60)
        print("1. Показать задачи на сегодня")
        print("2. Показать просроченные задачи")
        print("3. Показать задачи на ближайшие 7 дней")
        print("4. Добавить новую задачу")
        print("5. Показать все задачи")
        print("6. Отметить задачу как выполненную")
        print("0. Выход")
        print("=" * 60)
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            today = date.today()
            tasks = scheduler.get_tasks_for_date(today)
            scheduler.display_tasks(tasks, f"Задачи на сегодня ({today.strftime('%d.%m.%Y')})")
        
        elif choice == "2":
            tasks = scheduler.get_overdue_tasks()
            if tasks:
                print("\n⚠️ ВНИМАНИЕ! ПРОСРОЧЕННЫЕ ЗАДАЧИ:")
            scheduler.display_tasks(tasks, "Просроченные задачи")
        
        elif choice == "3":
            tasks_by_date = scheduler.get_tasks_next_week()
            if tasks_by_date:
                print("\nЗадачи на ближайшие 7 дней:")
                for date_str, tasks in tasks_by_date.items():
                    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
                    day_name = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"][date_obj.weekday()]
                    print(f"\n{date_str} ({day_name}):")
                    for task in tasks:
                        print(f"  • {task['title']}")
            else:
                print("\nНет задач на ближайшие 7 дней")
        
        elif choice == "4":
            title = input("Название задачи: ")
            if not title:
                print("Название не может быть пустым")
                continue
            
            task_date = get_date_from_user("Дата выполнения (ДД.ММ.ГГГГ, Enter - сегодня): ")
            description = input("Описание (необязательно): ")
            scheduler.add_task(title, task_date, description)
        
        elif choice == "5":
            scheduler.display_tasks(scheduler.tasks, "Все задачи")
        
        elif choice == "6":
            active_tasks = [t for t in scheduler.tasks if not t['completed']]
            if not active_tasks:
                print("Нет активных задач")
                continue
            
            print("\nАктивные задачи:")
            for i, task in enumerate(active_tasks):
                print(f"{i+1}. {task['title']} (до {task['date'].strftime('%d.%m.%Y')})")
            
            try:
                task_num = int(input("Номер задачи для отметки выполнения: ")) - 1
                if 0 <= task_num < len(active_tasks):
                    # Находим оригинальный индекс в полном списке
                    original_index = scheduler.tasks.index(active_tasks[task_num])
                    scheduler.mark_completed(original_index)
                else:
                    print("Неверный номер задачи")
            except ValueError:
                print("Введите корректный номер")
        
        elif choice == "0":
            print("До свидания!")
            break
        
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()