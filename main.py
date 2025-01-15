import numpy as np

# Створення масиву з чисел від 0 до 9
array = np.arange(10)

# Операції над масивом
squared_array = np.power(array, 2)  # Піднесення до квадрату
sqrt_array = np.sqrt(array)          # Квадратний корінь
sum_array = np.sum(array)            # Сума всіх елементів масиву

# Виведення результатів
print("Оригінальний масив:")
print(array)
print("\nМасив після піднесення до квадрату:")
print(squared_array)
print("\nМасив після обчислення квадратного кореня:")
print(sqrt_array)
print("\nСума елементів масиву:", sum_array)