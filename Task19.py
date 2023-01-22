# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
# Создайте список friends и добавьте в него N словарей с ключами name и age.
# Найдите самого младшего из друзей и выведите его имя.

print('Введите количество друзей:')
N = int(input())
name = []
age = []
for i in range (0, N):
    name.append(input('Введите имя друга:'))
    age.append(input('Введите возраст друга:'))
friends = dict(zip(name, age))
print(friends)

for key in friends:
    min_value = min(friends.values())
    for name, age in friends.items():
        if age == min_value:
            a = name
print(f"Самый младший друг - {a}")
