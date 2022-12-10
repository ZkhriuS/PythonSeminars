# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.
import random


def polynomial(k: int) -> str:
    result = ''
    while k > 0:
        coeff = random.randint(0, 100)
        if coeff == 1:
            if k > 1:
                result += 'x**' + str(k) + ' + '
            else:
                result += 'x + '
        elif coeff > 1:
            if k > 1:
                result += str(coeff) + '*(x**' + str(k) + ') + '
            else:
                result += str(coeff) + '*x + '
        k -= 1
    coeff = random.randint(0, 100)
    if coeff > 0:
        result += str(coeff) + " = 0"
    return result


def write_file(file: str):
    with open(file, 'w') as fout:
        fout.write(polynomial(int(input("Введите степень полинома > "))))


filename = 'file.txt'

write_file(filename)
