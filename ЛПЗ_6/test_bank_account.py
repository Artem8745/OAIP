"""
Тестирование всех возможностей банковского счета.
"""

from bank_account import BankAccount, SavingsAccount, CreditAccount, DepositAccount
import json


def test_basic_account():
    """Тестирование базового счета."""
    print("\n" + "=" * 70)
    print("ТЕСТИРОВАНИЕ БАЗОВОГО СЧЕТА")
    print("=" * 70)
    
    # Создаем счет
    account = BankAccount("ACC001", "Иван Петров", 1000, "RUB", 5.0)
    
    # Операции
    account.deposit(500, "Зарплата")
    account.withdraw(200, "Продукты")
    account.add_interest()
    
    # Статистика
    account.total_deposits()
    account.total_withdrawals()
    account.average_transaction()
    account.busiest_day()
    
    # Информация
    account.display_info()
    account.show_history()
    
    # Сохранение и загрузка
    account.save_to_file("account_test.json")
    
    # Закрытие счета
    account.withdraw(account.balance, "Закрытие")
    account.close_account()


def test_savings_account():
    """Тестирование сберегательного счета."""
    print("\n" + "=" * 70)
    print("ТЕСТИРОВАНИЕ СБЕРЕГАТЕЛЬНОГО СЧЕТА")
    print("=" * 70)
    
    savings = SavingsAccount("SAV001", "Анна Сидорова", 5000, "RUB", 5.0, 2)
    
    savings.deposit(1000, "Подарок")
    savings.withdraw(200, "Покупка 1")
    savings.withdraw(300, "Покупка 2")
    
    # Попытка превысить лимит
    savings.withdraw(100, "Покупка 3")
    
    savings.display_info()
    savings.add_interest()
    savings.show_history()


def test_credit_account():
    """Тестирование кредитного счета."""
    print("\n" + "=" * 70)
    print("ТЕСТИРОВАНИЕ КРЕДИТНОГО СЧЕТА")
    print("=" * 70)
    
    credit = CreditAccount("CRD001", "Петр Иванов", 10000, "RUB", 50000, 10.0)
    
    credit.withdraw(15000, "Покупка в кредит")
    credit.withdraw(30000, "Еще покупка")
    
    # Попытка превысить лимит
    credit.withdraw(10000, "Превышение лимита")
    
    credit.display_info()
    credit.add_interest()
    credit.show_history()
    
    # Вносим деньги для погашения долга
    credit.deposit(20000, "Погашение долга")
    credit.display_info()


def test_deposit_account():
    """Тестирование депозитного счета."""
    print("\n" + "=" * 70)
    print("ТЕСТИРОВАНИЕ ДЕПОЗИТНОГО СЧЕТА")
    print("=" * 70)
    
    deposit = DepositAccount("DEP001", "Елена Морозова", 100000, "RUB", 12, 8.0)
    
    # Попытка снять до окончания срока
    deposit.withdraw(10000, "Досрочное снятие")
    
    deposit.display_info()
    deposit.add_interest()
    
    # Имитация окончания срока
    print("\n⚠️ Имитация окончания срока депозита...")
    deposit._end_date = deposit._end_date.replace(year=2020)
    
    deposit.withdraw(50000, "Снятие после срока")
    deposit.add_interest()
    deposit.display_info()


def test_transfers():
    """Тестирование переводов между счетами."""
    print("\n" + "=" * 70)
    print("ТЕСТИРОВАНИЕ ПЕРЕВОДОВ")
    print("=" * 70)
    
    account1 = BankAccount("TRN001", "Отправитель", 5000)
    account2 = BankAccount("TRN002", "Получатель", 1000)
    
    print("\n--- ДО ПЕРЕВОДА ---")
    print(f"Счет 1: {account1.balance} {account1.currency}")
    print(f"Счет 2: {account2.balance} {account2.currency}")
    
    account1.transfer(account2, 2000, "Возврат долга")
    
    print("\n--- ПОСЛЕ ПЕРЕВОДА ---")
    print(f"Счет 1: {account1.balance} {account1.currency}")
    print(f"Счет 2: {account2.balance} {account2.currency}")
    
    account1.show_history()
    account2.show_history()


def test_statistics():
    """Тестирование статистических методов."""
    print("\n" + "=" * 70)
    print("ТЕСТИРОВАНИЕ СТАТИСТИКИ")
    print("=" * 70)
    
    account = BankAccount("STAT001", "Статистический счет", 1000)
    
    # Проводим несколько операций
    operations = [
        (100, "Пополнение 1"),
        (200, "Пополнение 2"),
        (50, "Снятие 1"),
        (300, "Пополнение 3"),
        (150, "Снятие 2"),
        (75, "Снятие 3"),
        (500, "Пополнение 4"),
    ]
    
    for amount, desc in operations:
        if "Пополнение" in desc:
            account.deposit(amount, desc)
        else:
            account.withdraw(amount, desc)
    
    # Статистика
    account.total_deposits()
    account.total_withdrawals()
    account.average_transaction()
    account.busiest_day()
    
    account.show_history()


def main():
    """Главная функция тестирования."""
    print("\n" + "█" * 70)
    print("КОМПЛЕКСНОЕ ТЕСТИРОВАНИЕ БАНКОВСКИХ СЧЕТОВ")
    print("█" * 70)
    
    test_basic_account()
    test_savings_account()
    test_credit_account()
    test_deposit_account()
    test_transfers()
    test_statistics()
    
    print("\n" + "█" * 70)
    print("✅ ТЕСТИРОВАНИЕ ЗАВЕРШЕНО УСПЕШНО")
    print("█" * 70)


if __name__ == "__main__":
    main()