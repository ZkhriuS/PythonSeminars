# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def set_list(length: int) -> list:
    lst = []
    for i in range(length):
        lst.append(int(input(f"Введите {i + 1}-е число > ")))
    return lst


def pair_product(lst: list) -> list:
    new_list = []
    for i in range((len(lst) + 1)//2):
        new_list.append(lst[i]*lst[len(lst) - 1 - i])
    return new_list


print(pair_product(set_list(int(input("Введите размер списка > ")))))
