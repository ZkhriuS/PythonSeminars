# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях). Пример того, что будет в итогвом файле: 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0

# from program_4 import polynomial
# from program_4 import write_file
#import sympy


# def read_file(file: str) -> str:
#     with open(file, 'r') as fin:
#         return fin.read()


# def polynomial_sum(str1, str2) -> str:
#     coeffs1 = sympy.poly_from_expr(str1)
#     coeffs2 = sympy.poly_from_expr(str2)
#     print(coeffs1)

#print(sympy.poly_from_expr('24*(x**5) + 69*(x**4) + 15*(x**3) + 26*(x**2) + 26*x + 72 = 0'))
