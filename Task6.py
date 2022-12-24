#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

print('Введите число:')
N = int(input())
out_dict = []
x = 1
for i in range(1, N + 1):
    x = x * i
    out_dict.insert(i, x)
print(out_dict)

