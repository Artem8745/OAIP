import random
import time

# Создаем список из 10 000 случайных чисел
print("Создание списка из 10 000 случайных чисел...")
numbers = [random.randint(1, 100000) for _ in range(10000)]

# Сортировка пузырьком
def bubble_sort(arr):
    n = len(arr)
    # Создаем копию, чтобы не изменять оригинал
    sorted_arr = arr.copy()
    
    for i in range(n):
        # Флаг для оптимизации: если не было обменов, массив отсортирован
        swapped = False
        
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        
        # Если не было обменов, выходим
        if not swapped:
            break
    
    return sorted_arr

# Тестируем сортировку пузырьком
print("\nВыполняется сортировка пузырьком...")
start_time = time.time()
bubble_sorted = bubble_sort(numbers)
bubble_time = time.time() - start_time
print(f"Время сортировки пузырьком: {bubble_time:.4f} секунд")

# Тестируем встроенную сортировку
print("\nВыполняется встроенная сортировка (Timsort)...")
start_time = time.time()
builtin_sorted = sorted(numbers)
builtin_time = time.time() - start_time
print(f"Время встроенной сортировки: {builtin_time:.6f} секунд")

# Проверяем, что оба метода дают одинаковый результат
is_same = bubble_sorted == builtin_sorted
print(f"\nРезультаты сортировки совпадают: {is_same}")

# Сравнение
print(f"\n{'='*50}")
print(f"Сравнение времени выполнения:")
print(f"  Сортировка пузырьком: {bubble_time:.4f} сек")
print(f"  Встроенная сортировка: {builtin_time:.6f} сек")
print(f"  Встроенная быстрее в {bubble_time/builtin_time:.0f} раз(а)")