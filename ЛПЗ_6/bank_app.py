"""
Интерактивное приложение для управления банковскими счетами.
"""

from bank_account import BankAccount, SavingsAccount, CreditAccount, DepositAccount
import sys


class BankApplication:
    """Консольное приложение для работы с банковскими счетами."""
    
    def __init__(self):
        self.accounts = {}  # Словарь для хранения счетов: номер -> объект
        self.current_account = None
    
    def print_menu(self):
        """Выводит главное меню."""
        print("\n" + "=" * 50)
        print("🏦 БАНКОВСКОЕ ПРИЛОЖЕНИЕ")
        print("=" * 50)
        print("1. Создать новый счет")
        print("2. Выбрать счет")
        print("3. Внести деньги")
        print("4. Снять деньги")
        print("5. Перевести деньги")
        print("6. Показать информацию о счете")
        print("7. Показать историю операций")
        print("8. Показать все счета")
        print("9. Статистика по счету")
        print("10. Начислить проценты")
        print("11. Сохранить счет в файл")
        print("12. Загрузить счет из файла")
        print("13. Закрыть счет")
        print("0. Выход")
        print("=" * 50)
    
    def create_account(self):
        """Создает новый банковский счет."""
        print("\n--- СОЗДАНИЕ НОВОГО СЧЕТА ---")
        
        # Выбор типа счета
        print("\nТипы счетов:")
        print("1. Обычный счет")
        print("2. Сберегательный счет")
        print("3. Кредитный счет")
        print("4. Депозитный счет")
        
        account_type = input("Выберите тип счета (1-4): ").strip()
        
        account_number = input("Введите номер счета: ").strip()
        if not account_number:
            print("❌ Номер счета не может быть пустым")
            return
        
        if account_number in self.accounts:
            print("❌ Счет с таким номером уже существует")
            return
        
        owner = input("Введите имя владельца: ").strip()
        if not owner:
            print("❌ Имя владельца не может быть пустым")
            return
        
        try:
            initial_balance = float(input("Введите начальный баланс (по умолчанию 0): ") or "0")
            if initial_balance < 0:
                print("❌ Начальный баланс не может быть отрицательным")
                return
        except ValueError:
            print("❌ Неверный формат числа")
            return
        
        currency = input("Введите валюту (по умолчанию RUB): ").strip().upper() or "RUB"
        
        # Создание счета в зависимости от типа
        try:
            if account_type == "2":
                interest_rate = float(input("Введите процентную ставку (по умолчанию 3%): ") or "3")
                max_withdrawals = int(input("Максимум снятий в месяц (по умолчанию 3): ") or "3")
                account = SavingsAccount(account_number, owner, initial_balance, 
                                         currency, interest_rate, max_withdrawals)
            elif account_type == "3":
                credit_limit = float(input("Введите кредитный лимит (по умолчанию 50000): ") or "50000")
                interest_rate = float(input("Введите процентную ставку по кредиту (по умолчанию 15%): ") or "15")
                account = CreditAccount(account_number, owner, initial_balance, 
                                        currency, credit_limit, interest_rate)
            elif account_type == "4":
                term_months = int(input("Введите срок депозита в месяцах (по умолчанию 12): ") or "12")
                interest_rate = float(input("Введите процентную ставку (по умолчанию 8%): ") or "8")
                account = DepositAccount(account_number, owner, initial_balance, 
                                         currency, term_months, interest_rate)
            else:
                interest_rate = float(input("Введите процентную ставку (по умолчанию 0%): ") or "0")
                account = BankAccount(account_number, owner, initial_balance, currency, interest_rate)
            
            self.accounts[account_number] = account
            print(f"✅ Счет успешно создан")
        except ValueError as e:
            print(f"❌ Ошибка при создании счета: {e}")
    
    def select_account(self):
        """Выбирает активный счет."""
        if not self.accounts:
            print("❌ Нет созданных счетов")
            return
        
        print("\n--- ДОСТУПНЫЕ СЧЕТА ---")
        for acc_num, acc in self.accounts.items():
            status = "✅" if acc.is_active else "🔒"
            print(f"   {status} {acc_num} - {acc.owner} ({acc.balance:.2f} {acc.currency})")
        
        account_number = input("\nВведите номер счета: ").strip()
        
        if account_number in self.accounts:
            self.current_account = self.accounts[account_number]
            print(f"✅ Выбран счет: {account_number}")
            self.current_account.display_info()
        else:
            print("❌ Счет не найден")
    
    def deposit(self):
        """Вносит деньги на текущий счет."""
        if not self.current_account:
            print("❌ Сначала выберите счет (пункт 2)")
            return
        
        try:
            amount = float(input("Введите сумму для внесения: "))
            description = input("Введите описание (необязательно): ").strip()
            self.current_account.deposit(amount, description)
        except ValueError:
            print("❌ Неверный формат суммы")
    
    def withdraw(self):
        """Снимает деньги с текущего счета."""
        if not self.current_account:
            print("❌ Сначала выберите счет (пункт 2)")
            return
        
        try:
            amount = float(input("Введите сумму для снятия: "))
            description = input("Введите описание (необязательно): ").strip()
            self.current_account.withdraw(amount, description)
        except ValueError:
            print("❌ Неверный формат суммы")
    
    def transfer(self):
        """Переводит деньги между счетами."""
        if not self.current_account:
            print("❌ Сначала выберите счет отправителя (пункт 2)")
            return
        
        if len(self.accounts) < 2:
            print("❌ Нужно минимум 2 счета для перевода")
            return
        
        print("\n--- ДОСТУПНЫЕ СЧЕТА ПОЛУЧАТЕЛЕЙ ---")
        for acc_num, acc in self.accounts.items():
            if acc_num != self.current_account.account_number:
                print(f"   {acc_num} - {acc.owner} ({acc.balance:.2f} {acc.currency})")
        
        to_account_num = input("\nВведите номер счета получателя: ").strip()
        
        if to_account_num not in self.accounts:
            print("❌ Счет получателя не найден")
            return
        
        if to_account_num == self.current_account.account_number:
            print("❌ Нельзя перевести деньги на тот же счет")
            return
        
        try:
            amount = float(input("Введите сумму перевода: "))
            description = input("Введите описание перевода (необязательно): ").strip()
            to_account = self.accounts[to_account_num]
            self.current_account.transfer(to_account, amount, description)
        except ValueError:
            print("❌ Неверный формат суммы")
    
    def show_info(self):
        """Показывает информацию о текущем счете."""
        if not self.current_account:
            print("❌ Сначала выберите счет (пункт 2)")
            return
        self.current_account.display_info()
    
    def show_history(self):
        """Показывает историю операций текущего счета."""
        if not self.current_account:
            print("❌ Сначала выберите счет (пункт 2)")
            return
        
        try:
            last_n = input("Сколько последних операций показать (Enter - все): ").strip()
            if last_n:
                self.current_account.show_history(int(last_n))
            else:
                self.current_account.show_history()
        except ValueError:
            print("❌ Неверное число")
    
    def show_all_accounts(self):
        """Показывает все созданные счета."""
        if not self.accounts:
            print("❌ Нет созданных счетов")
            return
        
        print("\n" + "=" * 60)
        print(f"ВСЕ СЧЕТА (всего: {len(self.accounts)})")
        print("=" * 60)
        
        for acc_num, acc in self.accounts.items():
            status = "✅ Активен" if acc.is_active else "🔒 Закрыт"
            print(f"{acc_num} | {acc.owner} | {acc.balance:.2f} {acc.currency} | {status}")
        
        print("=" * 60)
    
    def show_statistics(self):
        """Показывает статистику по текущему счету."""
        if not self.current_account:
            print("❌ Сначала выберите счет (пункт 2)")
            return
        
        print("\n" + "=" * 60)
        print("СТАТИСТИКА ПО СЧЕТУ")
        print("=" * 60)
        
        self.current_account.total_deposits()
        self.current_account.total_withdrawals()
        self.current_account.average_transaction()
        self.current_account.busiest_day()
    
    def add_interest(self):
        """Начисляет проценты на текущий счет."""
        if not self.current_account:
            print("❌ Сначала выберите счет (пункт 2)")
            return
        
        self.current_account.add_interest()
    
    def save_account(self):
        """Сохраняет текущий счет в файл."""
        if not self.current_account:
            print("❌ Сначала выберите счет (пункт 2)")
            return
        
        filename = input("Введите имя файла для сохранения (например, account.json): ").strip()
        if not filename:
            filename = f"{self.current_account.account_number}.json"
        
        self.current_account.save_to_file(filename)
    
    def load_account(self):
        """Загружает счет из файла."""
        filename = input("Введите имя файла для загрузки: ").strip()
        if not filename:
            print("❌ Имя файла не может быть пустым")
            return
        
        # Определяем тип счета по файлу
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Создаем соответствующий тип счета
            # (в упрощенном варианте загружаем как обычный счет)
            account = BankAccount.load_from_file(filename)
            
            if account and account.account_number not in self.accounts:
                self.accounts[account.account_number] = account
                print(f"✅ Счет загружен и добавлен в список")
            elif account:
                print("⚠️ Счет с таким номером уже существует")
        except FileNotFoundError:
            print(f"❌ Файл {filename} не найден")
        except Exception as e:
            print(f"❌ Ошибка при загрузке: {e}")
    
    def close_account(self):
        """Закрывает текущий счет."""
        if not self.current_account:
            print("❌ Сначала выберите счет (пункт 2)")
            return
        
        print(f"\n⚠️ ВНИМАНИЕ! Вы собираетесь закрыть счет {self.current_account.account_number}")
        confirm = input("Вы уверены? (да/нет): ").strip().lower()
        
        if confirm == "да":
            if self.current_account.close_account():
                self.current_account = None
        else:
            print("Операция отменена")
    
    def run(self):
        """Запускает главный цикл приложения."""
        print("=" * 60)
        print("ДОБРО ПОЖАЛОВАТЬ В БАНКОВСКОЕ ПРИЛОЖЕНИЕ")
        print("=" * 60)
        
        while True:
            self.print_menu()
            
            if self.current_account:
                print(f"\n💰 Текущий счет: {self.current_account.account_number} ({self.current_account.owner})")
            
            choice = input("\nВыберите действие (0-13): ").strip()
            
            if choice == "0":
                print("\n👋 До свидания!")
                break
            elif choice == "1":
                self.create_account()
            elif choice == "2":
                self.select_account()
            elif choice == "3":
                self.deposit()
            elif choice == "4":
                self.withdraw()
            elif choice == "5":
                self.transfer()
            elif choice == "6":
                self.show_info()
            elif choice == "7":
                self.show_history()
            elif choice == "8":
                self.show_all_accounts()
            elif choice == "9":
                self.show_statistics()
            elif choice == "10":
                self.add_interest()
            elif choice == "11":
                self.save_account()
            elif choice == "12":
                self.load_account()
            elif choice == "13":
                self.close_account()
            else:
                print("❌ Неверный выбор. Пожалуйста, выберите 0-13")


if __name__ == "__main__":
    app = BankApplication()
    app.run()