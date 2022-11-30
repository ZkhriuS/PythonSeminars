# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# Пример:

# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

num = int(input("Введите число n > "))
numbers = []
sum = 0
for i in range(1, num + 1):
    numbers.append(round((1 + 1/i)**i, 2))
    sum += numbers[i - 1]
print(f"Для n={num} {numbers}. Сумма {sum}")
