# Вычитание двух чисел
subtract = lambda x, y: x - y

# Нахождение остатка от деления
modulo = lambda x, y: x % y

# Возведение в степень
power = lambda x, y: x ** y

# Проверка, что число положительное
is_positive = lambda x: x > 0

# Проверка работы
print("Вычитание 10 - 3:", subtract(10, 3))       # 7
print("Остаток 17 % 5:", modulo(17, 5))          # 2
print("2 в степени 8:", power(2, 8))             # 256
print("Число 5 положительное?:", is_positive(5))  # True
print("Число -3 положительное?:", is_positive(-3)) # False