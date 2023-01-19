#Напишите программу, удаляющую из текста все слова, содержащие "абв".

my_text = input().split()
res_text = list(filter(lambda x: 'а' not in x and 'б' not in x and 'в' not in x, my_text))
print(res_text)