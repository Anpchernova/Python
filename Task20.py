# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
# Создайте список friends и добавьте в него N словарей с ключами name и age.
# Выведите средний возраст всех друзей и самое длинное имя.

print('Введите количество друзей:')
N = int(input())
name = []
age = []
for i in range (0, N):
    name.append(input('Введите имя друга:'))
    age.append(input('Введите возраст друга:'))
friends = dict(zip(name, age))
print(friends)

age = list(map(int, age))
sum = 0
for i in range (0, len(age)):
    sum += age[i]
    i += 1
avg = round(sum/len(age))
print(f"Средний возврат друзей - {avg} лет")

longest_word = ''
for name in name:
        if len(name) > len(longest_word):
            longest_word = name
print(f"Самое длинное имя - {longest_word}")
