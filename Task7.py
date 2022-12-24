#Реализуйте алгоритм перемешивания списка.

import random
lst = list(range(1, 50, 6))
print(lst)
random.shuffle(lst)
print(lst)