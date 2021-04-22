# Задание 4 коварное

src = [1000, 300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 30, 20]
result = (src[idx] for idx in range(1, len(src)) if src[idx] > src[idx - 1])
print('Результат:', *result)


from time import perf_counter
from sys import getsizeof


# Оптимизация по памяти

start = perf_counter()
src = [1000, 300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 30, 20]
result = (src[idx] for idx in range(1, len(src)) if src[idx] > src[idx - 1])
print('Результат:', *result)
print('Время:', perf_counter() - start)
print('Память:', getsizeof(result))

# Оптимизация по скорости

start = perf_counter()
src = [1000, 300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 30, 20]
result = [src[idx] for idx in range(1, len(src)) if src[idx] > src[idx - 1]]
print('Результат:', result)
print('Время:', perf_counter() - start)
print('Память:', getsizeof(result))
