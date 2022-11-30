# Реализуйте алгоритм перемешивания списка.

from random import randint

lst = []
length = int(input("Введите длину исходного списка > "))
for i in range(length):
    lst.append(randint(-100, 100))
print(f"Исходный список: {lst}")

test_num = int(input("Введите количество тестов перемешивания > "))
for i in range(test_num):
    for i in range(length):
        temp = lst[i]
        temp_index = (13*lst[length - i - 1] + lst[i]*7) % length
        lst[i] = lst[temp_index]
        lst[temp_index] = temp
    print(f"Список после перемешивания: {lst}")
