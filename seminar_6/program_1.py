# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

def set_list(length: int) -> list:
    lst = []
    for i in range(length):
        lst.append(int(input(f"Введите {i + 1}-е число > ")))
    return lst


def sum_odd(lst: list) -> int:
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
        print(f'{lst[i]}',
              end=' + ' if (i < len(lst) - 1) else ' = ')
    return sum


lst = set_list(int(input("Введите размер списка > ")))
print(sum_odd([value for pos, value in list(enumerate(lst)) if pos % 2 == 1]))
