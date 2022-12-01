# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(value: int) -> list:
    result = [1, 0, 1]
    for i in (range(1, value)):
        result.append(result[len(result) - 1] + result[len(result) - 2])
        result.insert(0, result[1] - result[0])
    return result


print(fibonacci(int(input("Введите k > "))))
