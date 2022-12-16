
# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]


def count_repeating(num: int, lst: list) -> int:
    count = 0
    for i in range(len(lst)):
        if num == lst[i]:
            count += 1
    return count


lst = [int(i) for i in input("Введите числа через пробел > ").split()]
print([value for _, value in filter(lambda tpl: tpl < (2, ), zip(
    map(lambda num: count_repeating(num, lst), lst), lst))])
