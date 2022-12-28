# Задайте натуральное число N. Напишите программу, которая составит список простых
# множителей числа N.
import math

print('Введите число:')
n = int(input())
b = []
for i in range(2, n + 1):
    if n % i == 0:
        count = 1
        for j in range(2, (i//2 + 1)):
            if i % j == 0:
                count = 0
                break
        if count == 1:
            b.append(i)
print(f"Простые множители числа {n} приведены в списке: {b}")