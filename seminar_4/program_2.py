# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import math


def is_simple_divider(num: int) -> bool:
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


def div_list(num: int) -> list:
    result = []
    i = 2
    while num > 1:
        if num % i == 0 and is_simple_divider(i):
            result.append(i)
            num /= i
        else:
            i += 1
    return result


number = int(input("Введите натуральное число > "))
print(f"Список простых делителей числа {number}: {div_list(number)}")
