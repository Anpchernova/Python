#Вычислить число пи c заданной точностью d
import math

print('Введите число от 10 в (-10) до 10 в (-1) степени:')
d = float(input())
if math.pow(10, -10) <= d <= math.pow(10, -1):
    n = int(math.log10(d) // (-1))
    print(round(math.pi, n))
else:
    print('Повторите ввод числа')