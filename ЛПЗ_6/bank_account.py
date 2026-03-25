"""
Модуль для работы с банковскими счетами.
Содержит класс BankAccount и его подклассы для моделирования различных типов счетов.
"""

import json
from datetime import datetime, date
from collections import defaultdict


class BankAccount:
    """
    Базовый класс, представляющий банковский счет.
    
    Атрибуты:
        _account_number (str): Номер счета
        _owner (str): Владелец счета
        _balance (float): Текущий баланс
        _currency (str): Валюта счета
        _transactions (list): История операций
        _is_active (bool): Статус счета
        _interest_rate (float): Процентная ставка
        _withdrawal_count (int): Количество снятий в текущем месяце
        _last_reset_date (str): Дата последнего сброса счетчика снятий
    """
    
    def __init__(self, account_number, owner, initial_balance=0, currency="RUB", interest_rate=0.0):
        """
        Конструктор класса. Вызывается при создании нового счета.
        
        Args:
            account_number (str): Номер счета
            owner (str): Владелец счета
            initial_balance (float): Начальный баланс (по умолчанию 0)
            currency (str): Валюта счета (по умолчанию "RUB")
            interest_rate (float): Процентная ставка (по умолчанию 0.0)
        """
        # Проверяем входные данные
        if not account_number or not isinstance(account_number, str):
            raise ValueError("Номер счета должен быть непустой строкой")
        
        if not owner or not isinstance(owner, str):
            raise ValueError("Имя владельца должно быть непустой строкой")
        
        if initial_balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")
        
        if interest_rate < 0:
            raise ValueError("Процентная ставка не может быть отрицательной")
        
        # Приватные атрибуты
        self._account_number = account_number
        self._owner = owner
        self._balance = initial_balance
        self._currency = currency
        self._transactions = []
        self._is_active = True
        self._interest_rate = interest_rate
        self._withdrawal_count = 0
        self._last_reset_date = datetime.now().strftime("%Y-%m")
        
        if initial_balance > 0:
            self._add_transaction("DEPOSIT", initial_balance, "Начальный взнос")
        
        print(f"✅ Счет {account_number} создан для {owner}")
        if interest_rate > 0:
            print(f"   Процентная ставка: {interest_rate}%")
        print(f"   Начальный баланс: {initial_balance} {currency}")
    
    def _add_transaction(self, transaction_type, amount, description=""):
        """
        Добавляет запись в историю операций.
        Внутренний метод (начинается с _), не для прямого вызова извне.
        """
        transaction = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": transaction_type,
            "amount": amount,
            "balance_after": self._balance,
            "description": description
        }
        self._transactions.append(transaction)
    
    @property
    def balance(self):
        """Возвращает текущий баланс (только для чтения)."""
        return self._balance
    
    @property
    def account_number(self):
        return self._account_number
    
    @property
    def owner(self):
        return self._owner
    
    @property
    def currency(self):
        return self._currency
    
    @property
    def is_active(self):
        return self._is_active
    
    @property
    def interest_rate(self):
        """Геттер для процентной ставки."""
        return self._interest_rate
    
    def deposit(self, amount, description=""):
        """
        Вносит деньги на счет.
        
        Args:
            amount (float): Сумма для внесения
            description (str): Описание операции
            
        Returns:
            bool: True если операция успешна, False если сумма некорректна
        """
        if not self._is_active:
            print("❌ Ошибка: счет закрыт")
            return False
        
        if amount <= 0:
            print("❌ Ошибка: сумма должна быть положительной!")
            return False
        
        self._balance += amount
        self._add_transaction("DEPOSIT", amount, description)
        
        print(f"💰 Внесено: {amount} {self._currency}")
        if description:
            print(f"   Описание: {description}")
        print(f"   Текущий баланс: {self._balance} {self._currency}")
        return True
    
    def withdraw(self, amount, description=""):
        """
        Снимает деньги со счета.
        
        Args:
            amount (float): Сумма для снятия
            description (str): Описание операции
            
        Returns:
            bool: True если операция успешна, False если недостаточно средств
        """
        if not self._is_active:
            print("❌ Ошибка: счет закрыт")
            return False
        
        if amount <= 0:
            print("❌ Ошибка: сумма должна быть положительной!")
            return False
        
        if amount > self._balance:
            print(f"❌ Ошибка: недостаточно средств!")
            print(f"   Запрошено: {amount} {self._currency}")
            print(f"   Доступно: {self._balance} {self._currency}")
            return False
        
        self._balance -= amount
        self._withdrawal_count += 1
        self._add_transaction("WITHDRAWAL", amount, description)
        
        print(f"💸 Снято: {amount} {self._currency}")
        if description:
            print(f"   Описание: {description}")
        print(f"   Текущий баланс: {self._balance} {self._currency}")
        return True
    
    def transfer(self, to_account, amount, description=""):
        """
        Переводит деньги на другой счет.
        
        Args:
            to_account (BankAccount): Счет получателя
            amount (float): Сумма перевода
            description (str): Описание перевода
            
        Returns:
            bool: True если перевод успешен
        """
        if not isinstance(to_account, BankAccount):
            print("❌ Ошибка: получатель должен быть банковским счетом")
            return False
        
        # Сначала снимаем со своего счета
        if self.withdraw(amount, f"Перевод: {description}"):
            # Затем кладем на счет получателя
            to_account.deposit(amount, f"Перевод от {self._owner}: {description}")
            print(f"🔄 Перевод выполнен успешно")
            return True
        
        return False
    
    def add_interest(self):
        """
        Начисляет проценты на остаток счета.
        
        Returns:
            float: Сумма начисленных процентов
        """
        if not self._is_active:
            print("❌ Ошибка: счет закрыт")
            return 0
        
        if self._interest_rate <= 0:
            print("ℹ️ Процентная ставка не установлена")
            return 0
        
        interest_amount = self._balance * (self._interest_rate / 100)
        self._balance += interest_amount
        self._add_transaction("INTEREST", interest_amount, f"Начисление процентов ({self._interest_rate}%)")
        
        print(f"📈 Начислены проценты: {interest_amount:.2f} {self._currency} ({self._interest_rate}%)")
        print(f"   Текущий баланс: {self._balance:.2f} {self._currency}")
        return interest_amount
    
    def set_interest_rate(self, rate):
        """
        Устанавливает новую процентную ставку.
        
        Args:
            rate (float): Новая процентная ставка
        """
        if rate < 0:
            print("❌ Процентная ставка не может быть отрицательной")
            return False
        
        old_rate = self._interest_rate
        self._interest_rate = rate
        print(f"📊 Процентная ставка изменена: {old_rate}% → {rate}%")
        self._add_transaction("INTEREST_RATE_CHANGE", 0, f"Изменение ставки: {old_rate}% → {rate}%")
        return True
    
    def close_account(self):
        """Закрывает счет."""
        if self._balance > 0:
            print(f"⚠️ На счете остались средства: {self._balance} {self._currency}")
            print("   Снимите все средства перед закрытием")
            return False
        
        self._is_active = False
        print(f"🔒 Счет {self._account_number} закрыт")
        return True
    
    def display_info(self):
        """Выводит информацию о счете."""
        status = "Активен" if self._is_active else "Закрыт"
        print("\n" + "=" * 50)
        print("ИНФОРМАЦИЯ О СЧЕТЕ")
        print("=" * 50)
        print(f"Номер счета: {self._account_number}")
        print(f"Владелец: {self._owner}")
        print(f"Баланс: {self._balance:.2f} {self._currency}")
        print(f"Процентная ставка: {self._interest_rate}%")
        print(f"Статус: {status}")
        print(f"Количество операций: {len(self._transactions)}")
        print("=" * 50)
    
    def show_history(self, last_n=None):
        """
        Показывает историю операций.
        
        Args:
            last_n (int, optional): Показать только последние N операций
        """
        print("\n" + "=" * 70)
        print(f"ИСТОРИЯ ОПЕРАЦИЙ ПО СЧЕТУ {self._account_number}")
        print("=" * 70)
        
        if not self._transactions:
            print("История операций пуста")
            return
        
        transactions_to_show = self._transactions
        if last_n:
            transactions_to_show = self._transactions[-last_n:]
            print(f"Показаны последние {last_n} операций:\n")
        
        for t in transactions_to_show:
            if t["type"] == "DEPOSIT":
                emoji = "💰"
                operation = "ПОПОЛНЕНИЕ"
            elif t["type"] == "WITHDRAWAL":
                emoji = "💸"
                operation = "СНЯТИЕ"
            elif t["type"] == "INTEREST":
                emoji = "📈"
                operation = "ПРОЦЕНТЫ"
            elif t["type"] == "INTEREST_RATE_CHANGE":
                emoji = "📊"
                operation = "ИЗМЕНЕНИЕ СТАВКИ"
            else:
                emoji = "📝"
                operation = "ОПЕРАЦИЯ"
            
            print(f"{emoji} {t['date']} | {operation}")
            if t['amount'] != 0:
                print(f"   Сумма: {t['amount']:.2f} {self._currency}")
            if t['description']:
                print(f"   Описание: {t['description']}")
            if t['type'] != "INTEREST_RATE_CHANGE":
                print(f"   Баланс после: {t['balance_after']:.2f} {self._currency}")
            print("-" * 70)
    
    # ==================== Задание 4: Статистика ====================
    
    def total_deposits(self):
        """
        Возвращает общую сумму всех пополнений.
        
        Returns:
            float: Общая сумма пополнений
        """
        total = sum(t['amount'] for t in self._transactions if t['type'] == 'DEPOSIT')
        print(f"📊 Общая сумма пополнений: {total:.2f} {self._currency}")
        return total
    
    def total_withdrawals(self):
        """
        Возвращает общую сумму всех снятий.
        
        Returns:
            float: Общая сумма снятий
        """
        total = sum(t['amount'] for t in self._transactions if t['type'] == 'WITHDRAWAL')
        print(f"📊 Общая сумма снятий: {total:.2f} {self._currency}")
        return total
    
    def average_transaction(self):
        """
        Возвращает среднюю сумму операции.
        
        Returns:
            float: Средняя сумма операции
        """
        if not self._transactions:
            print("📊 Нет операций для анализа")
            return 0
        
        total = sum(t['amount'] for t in self._transactions if t['type'] not in ['INTEREST_RATE_CHANGE'])
        count = len([t for t in self._transactions if t['type'] not in ['INTEREST_RATE_CHANGE']])
        if count == 0:
            print("📊 Нет операций для анализа")
            return 0
        
        avg = total / count
        print(f"📊 Средняя сумма операции: {avg:.2f} {self._currency}")
        return avg
    
    def busiest_day(self):
        """
        Возвращает день с наибольшим количеством операций.
        
        Returns:
            tuple: (дата, количество операций)
        """
        if not self._transactions:
            print("📊 Нет операций для анализа")
            return None, 0
        
        day_counts = defaultdict(int)
        for t in self._transactions:
            day = t['date'].split()[0]  # Берем только дату
            day_counts[day] += 1
        
        busiest_day = max(day_counts.items(), key=lambda x: x[1])
        print(f"📊 Самый активный день: {busiest_day[0]} ({busiest_day[1]} операций)")
        return busiest_day
    
    # ==================== Задание 3: Сохранение данных ====================
    
    def to_dict(self):
        """
        Преобразует объект в словарь для JSON сериализации.
        
        Returns:
            dict: Словарь с данными счета
        """
        return {
            'account_number': self._account_number,
            'owner': self._owner,
            'balance': self._balance,
            'currency': self._currency,
            'transactions': self._transactions,
            'is_active': self._is_active,
            'interest_rate': self._interest_rate,
            'withdrawal_count': self._withdrawal_count,
            'last_reset_date': self._last_reset_date
        }
    
    def save_to_file(self, filename):
        """
        Сохраняет данные счета в JSON файл.
        
        Args:
            filename (str): Имя файла для сохранения
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.to_dict(), f, ensure_ascii=False, indent=2)
            print(f"💾 Данные счета сохранены в файл: {filename}")
            return True
        except Exception as e:
            print(f"❌ Ошибка при сохранении: {e}")
            return False
    
    @classmethod
    def load_from_file(cls, filename):
        """
        Загружает данные счета из JSON файла.
        
        Args:
            filename (str): Имя файла для загрузки
            
        Returns:
            BankAccount: Загруженный объект счета
        """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            account = cls(
                data['account_number'],
                data['owner'],
                data['balance'],
                data['currency'],
                data['interest_rate']
            )
            account._transactions = data['transactions']
            account._is_active = data['is_active']
            account._withdrawal_count = data['withdrawal_count']
            account._last_reset_date = data['last_reset_date']
            
            print(f"📂 Данные счета загружены из файла: {filename}")
            return account
        except Exception as e:
            print(f"❌ Ошибка при загрузке: {e}")
            return None


# ==================== Задание 2: Разные типы счетов ====================

class SavingsAccount(BankAccount):
    """
    Сберегательный счет - ограничение на количество снятий в месяц.
    """
    
    def __init__(self, account_number, owner, initial_balance=0, currency="RUB", 
                 interest_rate=3.0, max_withdrawals_per_month=3):
        """
        Конструктор сберегательного счета.
        
        Args:
            max_withdrawals_per_month (int): Максимальное количество снятий в месяц
        """
        super().__init__(account_number, owner, initial_balance, currency, interest_rate)
        self._max_withdrawals_per_month = max_withdrawals_per_month
        self._reset_monthly_counter()
    
    def _reset_monthly_counter(self):
        """Сбрасывает счетчик снятий при наступлении нового месяца."""
        current_month = datetime.now().strftime("%Y-%m")
        if current_month != self._last_reset_date:
            self._withdrawal_count = 0
            self._last_reset_date = current_month
    
    def withdraw(self, amount, description=""):
        """
        Снимает деньги со счета с проверкой лимита снятий.
        """
        self._reset_monthly_counter()
        
        if self._withdrawal_count >= self._max_withdrawals_per_month:
            print(f"❌ Ошибка: превышен лимит снятий ({self._max_withdrawals_per_month} в месяц)")
            return False
        
        return super().withdraw(amount, description)
    
    def set_interest_rate(self, rate):
        """Устанавливает новую процентную ставку для сберегательного счета."""
        if rate < 0:
            print("❌ Процентная ставка не может быть отрицательной")
            return False
        
        if rate > 20:
            print("⚠️ Внимание: высокая процентная ставка для сберегательного счета")
        
        old_rate = self._interest_rate
        self._interest_rate = rate
        print(f"📊 Процентная ставка сберегательного счета изменена: {old_rate}% → {rate}%")
        self._add_transaction("INTEREST_RATE_CHANGE", 0, f"Изменение ставки: {old_rate}% → {rate}%")
        return True
    
    def display_info(self):
        """Выводит информацию о сберегательном счете."""
        super().display_info()
        print(f"Лимит снятий в месяц: {self._max_withdrawals_per_month}")
        print(f"Снятий в этом месяце: {self._withdrawal_count}")
        print("=" * 50)


class CreditAccount(BankAccount):
    """
    Кредитный счет - можно уходить в минус до определенного лимита.
    """
    
    def __init__(self, account_number, owner, initial_balance=0, currency="RUB",
                 credit_limit=50000, interest_rate=15.0):
        """
        Конструктор кредитного счета.
        
        Args:
            credit_limit (float): Кредитный лимит
        """
        super().__init__(account_number, owner, initial_balance, currency, interest_rate)
        self._credit_limit = credit_limit
        self._interest_charged = 0
    
    @property
    def available_funds(self):
        """Доступные средства (баланс + кредитный лимит)."""
        return self._balance + self._credit_limit
    
    def withdraw(self, amount, description=""):
        """
        Снимает деньги со счета, позволяя уходить в минус до лимита.
        """
        if not self._is_active:
            print("❌ Ошибка: счет закрыт")
            return False
        
        if amount <= 0:
            print("❌ Ошибка: сумма должна быть положительной!")
            return False
        
        if amount > self.available_funds:
            print(f"❌ Ошибка: недостаточно средств!")
            print(f"   Запрошено: {amount} {self._currency}")
            print(f"   Доступно: {self.available_funds:.2f} {self._currency}")
            return False
        
        self._balance -= amount
        self._withdrawal_count += 1
        self._add_transaction("WITHDRAWAL", amount, description)
        
        print(f"💸 Снято: {amount} {self._currency}")
        if description:
            print(f"   Описание: {description}")
        
        if self._balance < 0:
            print(f"⚠️ Кредитный долг: {abs(self._balance):.2f} {self._currency}")
        
        print(f"   Текущий баланс: {self._balance:.2f} {self._currency}")
        return True
    
    def add_interest(self):
        """
        Начисляет проценты на кредитную задолженность.
        """
        if self._balance >= 0:
            print("ℹ️ Нет кредитной задолженности")
            return 0
        
        debt = abs(self._balance)
        interest_amount = debt * (self._interest_rate / 100)
        self._balance -= interest_amount
        self._interest_charged += interest_amount
        self._add_transaction("INTEREST", interest_amount, 
                              f"Начисление процентов на кредит ({self._interest_rate}%)")
        
        print(f"📈 Начислены проценты на кредит: {interest_amount:.2f} {self._currency}")
        print(f"   Текущий баланс: {self._balance:.2f} {self._currency}")
        return interest_amount
    
    def set_interest_rate(self, rate):
        """Устанавливает новую процентную ставку для кредитного счета."""
        if rate < 0:
            print("❌ Процентная ставка не может быть отрицательной")
            return False
        
        if rate > 30:
            print("⚠️ Внимание: очень высокая процентная ставка по кредиту")
        
        old_rate = self._interest_rate
        self._interest_rate = rate
        print(f"📊 Процентная ставка по кредиту изменена: {old_rate}% → {rate}%")
        self._add_transaction("INTEREST_RATE_CHANGE", 0, f"Изменение кредитной ставки: {old_rate}% → {rate}%")
        return True
    
    def display_info(self):
        """Выводит информацию о кредитном счете."""
        super().display_info()
        print(f"Кредитный лимит: {self._credit_limit} {self._currency}")
        print(f"Доступно средств: {self.available_funds:.2f} {self._currency}")
        if self._balance < 0:
            print(f"Кредитный долг: {abs(self._balance):.2f} {self._currency}")
        print("=" * 50)


class DepositAccount(BankAccount):
    """
    Депозитный счет - нельзя снимать до окончания срока.
    """
    
    def __init__(self, account_number, owner, initial_balance=0, currency="RUB",
                 term_months=12, interest_rate=8.0):
        """
        Конструктор депозитного счета.
        
        Args:
            term_months (int): Срок депозита в месяцах
        """
        super().__init__(account_number, owner, initial_balance, currency, interest_rate)
        self._term_months = term_months
        self._start_date = datetime.now()
        self._end_date = self._start_date.replace(
            year=self._start_date.year + term_months // 12,
            month=self._start_date.month + term_months % 12
        )
        self._is_withdraw_allowed = False
    
    def _is_term_expired(self):
        """Проверяет, истек ли срок депозита."""
        return datetime.now() >= self._end_date
    
    def withdraw(self, amount, description=""):
        """
        Снимает деньги только после окончания срока депозита.
        """
        if not self._is_term_expired():
            days_left = (self._end_date - datetime.now()).days
            print(f"❌ Ошибка: срок депозита не истек!")
            print(f"   До окончания срока осталось {days_left} дней")
            print(f"   Дата окончания: {self._end_date.strftime('%Y-%m-%d')}")
            return False
        
        return super().withdraw(amount, description)
    
    def add_interest(self):
        """
        Начисляет проценты (капитализация) в конце срока.
        """
        if self._is_term_expired():
            return super().add_interest()
        else:
            print(f"ℹ️ Проценты будут начислены по окончании срока депозита")
            return 0
    
    def set_interest_rate(self, rate):
        """Устанавливает новую процентную ставку для депозитного счета."""
        if rate < 0:
            print("❌ Процентная ставка не может быть отрицательной")
            return False
        
        if rate > 15:
            print("⚠️ Внимание: высокая процентная ставка для депозита")
        
        old_rate = self._interest_rate
        self._interest_rate = rate
        print(f"📊 Процентная ставка по депозиту изменена: {old_rate}% → {rate}%")
        self._add_transaction("INTEREST_RATE_CHANGE", 0, f"Изменение депозитной ставки: {old_rate}% → {rate}%")
        return True
    
    def display_info(self):
        """Выводит информацию о депозитном счете."""
        super().display_info()
        print(f"Срок депозита: {self._term_months} месяцев")
        print(f"Дата начала: {self._start_date.strftime('%Y-%m-%d')}")
        print(f"Дата окончания: {self._end_date.strftime('%Y-%m-%d')}")
        print(f"Досрочное снятие: {'Разрешено' if self._is_withdraw_allowed else 'Запрещено'}")
        print("=" * 50)