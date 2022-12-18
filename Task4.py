#Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве.
import math

print('Введите координаты первой точки:')
x1 = int(input())
y1 = int(input())
print(f'({x1}, {y1})')
print('Введите координаты второй точки:')
x2 = int(input())
y2 = int(input())
print(f'({x2}, {y2})')
L = round(math.sqrt(math.pow((x1-x2), 2)+math.pow((y1-y2), 2)), 2)
print(L)