# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# 0,56 -> 11

number = float(input("Введите вещественное число > "))

# можно было бы без преобразования ввода в float, но если это будет отдельный модуль, принимающий float, то лучше это учесть

sum = 0
for el in str(number):
    if el in '123456789':
        sum += int(el)

print(sum)
