# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import math


def is_simple_divider(num: int) -> bool:
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


number = int(input("Введите натуральное число > "))
result = list(filter(is_simple_divider, map(lambda num: num if (
    number % num == 0) else number, range(2, number))))
print(f"Список простых делителей числа {number}: {result}")
