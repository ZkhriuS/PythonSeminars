# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 10.01] => 0.19

def set_list(length: int) -> list:
    lst = []
    for i in range(length):
        lst.append(float(input(f"Введите {i + 1}-е число > ")))
    return lst


my_lst = set_list(int(input("Введите размер списка > ")))
print(f"{my_lst} => {max(map(lambda x: abs(x)%1, my_lst)) - min(map(lambda x: abs(x)%1, my_lst))}")
