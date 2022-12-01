# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def bin(value: int) -> str:
    result = ''
    digit = 1
    while (digit <= value):
        result = str(int(bool(value & digit))) + result
        digit *= 2
    return result


num = int(input("Введите число > "))
print(f"{num} = {bin(num)}")
