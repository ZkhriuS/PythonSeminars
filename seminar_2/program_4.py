# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

numbers = []
product = 1
num = int(input("Введите число N > "))
for i in range(-num, num + 1):
    numbers.append(i)
print(numbers)
indexes = input("Введите индексы > ").split()
for i in range(len(indexes)):
    product *= numbers[int(indexes[i])]
    print(f'{numbers[int(indexes[i])]}',
          end=' * ' if (i < len(indexes) - 1) else ' = ')
print(product)
