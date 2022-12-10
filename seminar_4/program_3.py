# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

def unique(src_list: list) -> list:
    result = []
    for i in range(len(src_list)):
        if count_repeating(src_list[i], src_list) == 1:
            result.append(src_list[i])
    return result


def count_repeating(num: int, lst: list) -> int:
    count = 0
    for i in range(len(lst)):
        if num == lst[i]:
            count += 1
    return count


print(unique([int(i) for i in input("Введите числа через пробел > ").split()]))
