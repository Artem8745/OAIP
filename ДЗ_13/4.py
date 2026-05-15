numbers = [-2, -1, 0, 1, 2, 3, 4, 5, -10, 15]

result = sum([x ** 2 for x in numbers if x > 0])
print("Генератор списка:", result)  # 255

result = sum(map(lambda x: x ** 2, filter(lambda x: x > 0, numbers)))
print("map/filter:", result)  # 255

result = 0
for x in numbers:
    if x > 0:
        result += x ** 2
print("Цикл:", result)  # 255