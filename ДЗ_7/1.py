import pprint
import time

class PhoneBook():
    def __init__(self, home):
        self.home = home
        self.phone_books = {}

        self.add_contact('Петр 1', '89105555555', '@gmail.com', 'Домовой чат №1')
        self.add_contact('Петруша 1', '89105486555', 'фываы@gmail.com', 'Домовой чат №1')
        self.add_contact('Андрий 1', '89105534555', '1235@gmail.com', 'Домовой чат №2')
        self.add_contact('Ванечка 1', '8910586455', '375hf5@gmail.com', 'Домовой чат №2')
        self.management_console()

    def add_contact(self, name, tel, email, group):

        check_correctness = self.check_name(name)

        if check_correctness[0]:
            print(check_correctness[1])
            return None

        keys_contact = ['name', 'tel', 'email', 'group']
        values_contact = [name, tel, email, group]

        contact = {key: value for key, value in zip(keys_contact, values_contact)}
        self.phone_books[tel] = contact
        
        return ()

    def search_by_name(self, search_name):
        search_name = search_name.lower()

        for key, contact_data in self.phone_books.items():
            found_name = contact_data.get('name', 'Имя не найдено').lower()

            if found_name == search_name:
                return {key: contact_data}
            
        print('Человек не найден!')
        return None
    
    def search_by_group(self, search_group):
        search_group = search_group.lower()
        result = []

        for key, contact_data in self.phone_books.items():
            found_group = contact_data.get('group', 'Группа не найдена').lower()

            if found_group == search_group:
                result.append({key: contact_data})

        if not result:
            print('Группа не найдена')
            return None

        return result

    # Проверка введенных значений
    def check_name(self, name):
        name_split = name.split()
        
        if len(name_split) <= 1:
            return [True, 'ФИО не может состоять из одного слова!']
        else:
            return [False]

    # Консолькое управление:
    def management_console(self):
        while True:
            actions = {
                '1': {'name': 'Добавить контакт', 'handler': self.add_contact_console},
                '2': {'name': 'Поиск по имени', 'handler': self.search_by_name_console},
                '3': {'name': 'Поиск по группе', 'handler': self.search_by_group_console},
                '4': {'name': 'Вывести все группы', 'handler': self.show_all_groups},
                '5': {'name': 'Остановить программу', 'handler': exit}
            }

            # Создание с использованием гениратора

            # key_1 = ['1', '2', '3', '4', '5']
            # value_1 = [
            #     {'name': 'Добавить контакт', 'handler': self.add_contact_console},
            #     {'name': 'Поиск по имени', 'handler': self.search_by_name_console},
            #     {'name': 'Поиск по группе', 'handler': self.search_by_group_console},
            #     {'name': 'Вывести все группы', 'handler': self.show_all_groups},
            #     {'name': 'Остановить программу', 'handler': exit}
            # ]

            # actions = {k: v for k, v in zip(key_1, value_1) }

            print('====================================\nЧто вы хотите сделать?')
            for key, action in actions.items():
                print(f"{key}. {action['name']}")

            choice = input()

            if choice in actions:
                actions[choice]['handler'](True)
            else:
                print('Неверный выбор!')

            time.sleep(0.3)

    def add_contact_console(self, prints):
        name_contact = input('Введие ФИО: ')
        tel_contact = input('Введие телефон: ')
        email_contact = input('Введие email: ')
        group_contact = input('Введие группу: ')

        add_contact_check = self.add_contact(name_contact, tel_contact, email_contact, group_contact)

        if add_contact_check == None:
            print('Контакт НЕ добавлен!')
        else:
            print('Контакт добавлен!')

    def search_by_name_console(self, prints):
        name = input('Введите имя: ')

        if prints == True:
            pprint.pprint(self.search_by_name(name))

        return self.search_by_name(name)

    def search_by_group_console(self, prints):
        group = input('Введите группу: ')

        return self.search_by_group(group)
    
    def show_all_groups(self, prints):
        pprint.pprint(self.phone_books)

phone_book = PhoneBook('Главный дом')
