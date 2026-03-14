"""
Программа для безопасного чтения данных из файлов.
Поддерживает JSON и CSV форматы.
"""

import json
import csv
from datetime import datetime
import os

class FileReader:
    """
    Класс для безопасного чтения данных из файлов.
    Обрабатывает различные ошибки и логирует результаты.
    """

    def __init__(self, log_file="file_operations.log"):
        """
        Инициализация читателя файлов.

        Args:
            log_file (str): Имя файла для логирования
        """
        self.log_file = log_file
        self.operations_count = 0
        self.errors_count = 0

    def log_operation(self, message, level="INFO"):
        """
        Записывает операцию в лог-файл.

        Args:
            message (str): Сообщение для записи
            level (str): Уровень логирования (INFO, WARNING, ERROR)
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {level}: {message}\n"

        try:
            with open(self.log_file, "a", encoding="utf-8") as log:
                log.write(log_entry)

            # Также выводим в консоль с цветом
            colors = {
                "INFO": "\033[92m",   # Зеленый
                "WARNING": "\033[93m", # Желтый
                "ERROR": "\033[91m"    # Красный
            }
            reset = "\033[0m"

            if level in colors:
                print(f"{colors[level]}{log_entry.strip()}{reset}")
            else:
                print(log_entry.strip())

        except Exception as e:
            print(f"Не удалось записать в лог: {e}")

    def read_json_file(self, filename):
        """
        Безопасно читает JSON файл.

        Args:
            filename (str): Имя файла для чтения

        Returns:
            tuple: (данные, успех_операции)
        """
        self.operations_count += 1
        self.log_operation(f"Попытка чтения JSON файла: {filename}")

        # 1. Проверяем существование файла
        if not os.path.exists(filename):
            self.errors_count += 1
            self.log_operation(f"Файл не найден: {filename}", "ERROR")
            return None, False

        # 2. Проверяем, что это файл, а не папка
        if not os.path.isfile(filename):
            self.errors_count += 1
            self.log_operation(f"Указанный путь не является файлом: {filename}", "ERROR")
            return None, False

        # 3. Пробуем прочитать файл
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            self.log_operation(f"JSON файл успешно прочитан: {len(data)} записей")
            return data, True

        except json.JSONDecodeError as e:
            self.errors_count += 1
            self.log_operation(f"Ошибка формата JSON: {e}", "ERROR")
            return None, False

        except PermissionError as e:
            self.errors_count += 1
            self.log_operation(f"Нет прав на чтение файла: {e}", "ERROR")
            return None, False

        except Exception as e:
            self.errors_count += 1
            self.log_operation(f"Неожиданная ошибка при чтении JSON: {e}", "ERROR")
            return None, False

    def read_csv_file(self, filename, delimiter=",", has_header=True):
        """
        Безопасно читает CSV файл.

        Args:
            filename (str): Имя файла для чтения
            delimiter (str): Разделитель полей
            has_header (bool): Есть ли заголовок в файле

        Returns:
            tuple: (заголовки, данные, успех_операции)
        """
        self.operations_count += 1
        self.log_operation(f"Попытка чтения CSV файла: {filename}")

        # Проверки существования файла
        if not os.path.exists(filename):
            self.errors_count += 1
            self.log_operation(f"Файл не найден: {filename}", "ERROR")
            return None, None, False

        try:
            with open(filename, "r", encoding="utf-8") as file:
                # Читаем все строки
                lines = file.readlines()

            if not lines:
                self.log_operation("Файл пуст", "WARNING")
                return [], [], True

            # Разбираем CSV
            headers = []
            data = []

            for i, line in enumerate(lines):
                # Убираем пробелы и символы перевода строки
                line = line.strip()
                if not line:  # Пропускаем пустые строки
                    continue

                # Разделяем по разделителю
                row = line.split(delimiter)

                # Убираем лишние пробелы у каждого поля
                row = [field.strip() for field in row]

                if i == 0 and has_header:
                    headers = row
                else:
                    data.append(row)

            self.log_operation(f"CSV файл прочитан: {len(data)} строк данных")
            return headers, data, True

        except PermissionError as e:
            self.errors_count += 1
            self.log_operation(f"Нет прав на чтение файла: {e}", "ERROR")
            return None, None, False

        except Exception as e:
            self.errors_count += 1
            self.log_operation(f"Ошибка при чтении CSV: {e}", "ERROR")
            return None, None, False

    def write_json_file(self, filename, data):
        """
        Безопасно записывает данные в JSON файл.

        Args:
            filename (str): Имя файла для записи
            data: Данные для записи

        Returns:
            bool: Успех операции
        """
        self.operations_count += 1
        self.log_operation(f"Попытка записи в JSON файл: {filename}")

        try:
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            self.log_operation(f"Данные успешно записаны в {filename}")
            return True

        except PermissionError as e:
            self.errors_count += 1
            self.log_operation(f"Нет прав на запись файла: {e}", "ERROR")
            return False

        except Exception as e:
            self.errors_count += 1
            self.log_operation(f"Ошибка при записи JSON: {e}", "ERROR")
            return False

    def write_csv_file(self, filename, data, headers=None, delimiter=","):
        """
        Безопасно записывает данные в CSV файл.

        Args:
            filename (str): Имя файла для записи
            data (list): Список строк данных
            headers (list): Заголовки столбцов
            delimiter (str): Разделитель полей

        Returns:
            bool: Успех операции
        """
        self.operations_count += 1
        self.log_operation(f"Попытка записи в CSV файл: {filename}")

        try:
            with open(filename, "w", encoding="utf-8", newline="") as file:
                writer = csv.writer(file, delimiter=delimiter)

                if headers:
                    writer.writerow(headers)

                writer.writerows(data)

            self.log_operation(f"Данные успешно записаны в {filename}")
            return True

        except PermissionError as e:
            self.errors_count += 1
            self.log_operation(f"Нет прав на запись файла: {e}", "ERROR")
            return False

        except Exception as e:
            self.errors_count += 1
            self.log_operation(f"Ошибка при записи CSV: {e}", "ERROR")
            return False

    def get_statistics(self):
        """Возвращает статистику работы."""
        return {
            "total_operations": self.operations_count,
            "errors_count": self.errors_count,
            "success_rate": (self.operations_count - self.errors_count) / self.operations_count * 100
            if self.operations_count > 0 else 0
        }

    def display_statistics(self):
        """Выводит статистику работы."""
        stats = self.get_statistics()
        print("\n" + "=" * 50)
        print("СТАТИСТИКА РАБОТЫ")
        print("=" * 50)
        print(f"Всего операций: {stats['total_operations']}")
        print(f"Ошибок: {stats['errors_count']}")
        print(f"Успешность: {stats['success_rate']:.1f}%")
        print("=" * 50)