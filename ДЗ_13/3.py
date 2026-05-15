from functools import reduce

numbers = [1, 2, 3, 4, 5]
strings = ["Hello", " ", "World", "!", "!!"]

# Произведение всех чисел списка
product = reduce(lambda x, y: x * y, numbers)
print("Произведение чисел:", product)  # 120 (1*2*3*4*5)

# Минимальное число
minimum = reduce(lambda x, y: x if x < y else y, numbers)
print("Минимальное число:", minimum)  # 1

# Объединить список строк в одну строку
combined_string = reduce(lambda x, y: x + y, strings)
print("Объединенная строка:", combined_string)  # "Hello World!!!"

# Факториал числа
n = 5
factorial = reduce(lambda x, y: x * y, range(1, n + 1))
print(f"Факториал {n}:", factorial)  # 120