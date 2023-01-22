#Создайте список из случайных чисел. Найдите количество различных элементов в нем.

import random
n = int(input("Сколько элементов? "))
list1 = []
for i in range(n):
    list1.append(random.randint(1, 10))
print('Cделан такой список -', list1)

list1.sort()

i = 0
while i < n:
    count = 1
    if list1[i] == list1[i+1]:
        count += 1
        i += 1
    print(f"{list1[i]} - {count}")
    i = i + 1