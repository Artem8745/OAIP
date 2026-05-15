numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Найти квадраты всех чисел (map)
squares = list(map(lambda x: x ** 2, numbers))
print("Квадраты чисел:", squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Оставить только нечетные числа (filter)
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("Нечетные числа:", odd_numbers)
# [1, 3, 5, 7, 9]

# Оставить только числа, кратные 3 (filter)
multiples_of_3 = list(filter(lambda x: x % 3 == 0, numbers))
print("Кратные 3:", multiples_of_3)
# [3, 6, 9]

# Преобразовать числа в строки (map)
string_numbers = list(map(lambda x: str(x), numbers))
print("Числа как строки:", string_numbers)
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# Найти кубы четных чисел (filter + map)
even_cubes = list(map(lambda x: x ** 3, filter(lambda x: x % 2 == 0, numbers)))
print("Кубы четных чисел:", even_cubes)
# [8, 64, 216, 512, 1000]