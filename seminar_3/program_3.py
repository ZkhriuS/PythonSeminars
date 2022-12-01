# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 10.01] => 0.19

def set_list(length: int) -> list:
    lst = []
    for i in range(length):
        lst.append(float(input(f"Введите {i + 1}-е число > ")))
    return lst


def max_fractional(lst: list) -> float:
    max_f = 0
    for i in lst:
        if max_f < abs(i) % 1:
            max_f = abs(i) % 1
    return max_f


def min_fractional(lst: list) -> float:
    min_f = 1
    for i in lst:
        if min_f > abs(i) % 1:
            min_f = abs(i) % 1
    return min_f


my_lst = set_list(int(input("Введите размер списка > ")))
print(f"{my_lst} => {max_fractional(my_lst) - min_fractional(my_lst)}")
