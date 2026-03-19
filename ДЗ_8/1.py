class Book:
    def __init__(self, title, author, year, is_available=True):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = is_available

    def borrow(self):
        if self.is_available == True:
            self.is_available = False
            print('Книга теперь не доступна')
        else:
            print('Книга уже не доступна')

    def return_book(self):
        if self.is_available == False:
            self.is_available = True
            print('Книга теперь доступна')
        else:
            print('Книга уже доступна')

    def get_info(self):
        print(f"{self.title}, {self.author}, {self.year} г. Доступна: { 'ДА' if self.is_available == True else 'Нет'}")

book_voina_i_mir = Book('Война и мир', 'Толстой', 1867)

book_voina_i_mir.get_info()

# Создаём две книги
book1 = Book('Война и мир', 'Толстой', 1867)
book2 = Book('Преступление и наказание', 'Достоевский', 1866)

# Проверяем согласно заданию
print("=== Начальное состояние ===")
book1.get_info()
book2.get_info()

print("\n=== Берём первую книгу ===")
book1.borrow()
book1.get_info()

print("\n=== Пытаемся взять её ещё раз ===")
book1.borrow()

print("\n=== Возвращаем книгу ===")
book1.return_book()
book1.get_info()

print("\n=== Берём снова ===")
book1.borrow()
book1.get_info()