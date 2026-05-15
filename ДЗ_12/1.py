import random
import time

# Создаем список из 1 000 000 случайных чисел
print("Создание списка из 1 000 000 случайных чисел...")
numbers = [random.randint(1, 10_000_000) for _ in range(1_000_000)]

# Выбираем случайное число для поиска
target = random.choice(numbers)
print(f"Ищем число: {target}")

# Линейный поиск
def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

start_time = time.time()
index_linear = linear_search(numbers, target)
linear_time = time.time() - start_time

print(f"\nЛинейный поиск:")
print(f"  Индекс: {index_linear}")
print(f"  Время: {linear_time:.6f} секунд")

# Сортировка списка для бинарного поиска
print("\nСортировка списка...")
start_time = time.time()
sorted_numbers = sorted(numbers)
sort_time = time.time() - start_time
print(f"Время сортировки: {sort_time:.4f} секунд")

# Бинарный поиск
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

start_time = time.time()
index_binary = binary_search(sorted_numbers, target)
binary_time = time.time() - start_time

print(f"\nБинарный поиск:")
print(f"  Индекс: {index_binary}")
print(f"  Время: {binary_time:.6f} секунд")

# Сравнение
print(f"\n{'='*50}")
print(f"Сравнение времени выполнения:")
print(f"  Линейный поиск: {linear_time:.6f} сек")
print(f"  Бинарный поиск: {binary_time:.6f} сек")
try:
    print(f"  Бинарный поиск быстрее в {linear_time/binary_time:.0f} раз(а)")
except:
    print(f"  Бинарный поиск быстрее в бесконечность раз")
print(f"  Но с учетом сортировки: {linear_time/(sort_time + binary_time):.6f}")