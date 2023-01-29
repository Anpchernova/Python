# Напишите функцию encrypt_caesar(msg, shift), которая кодирует сообщение шифром
# Цезаря и возвращает его. Шифр Цезаря заменяет каждую букву в тексте на букву, которая
# отстоит в алфавите на некоторое фиксированное число позиций.
# В функцию передается сообщение и сдвиг алфавита. Если сдвиг не указан, то пусть ваша
# функция кодирует сдвиг алфавита на 3 позиции.
# Напишите также функцию декодирования decrypt_caesar(msg, shift), также
# использующую сдвиг по умолчанию. При написании функции декодирования используйте
# вашу функцию кодирования.

def encrypt_caesar(msg, shift=3):
    small_symbols1 = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    big_symbols1 = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    shift = shift % len(small_symbols1)
    small_symbols2 = small_symbols1[shift:] + small_symbols1[:shift]
    big_symbols2 = big_symbols1[shift:] + big_symbols1[:shift]
    translation = msg.maketrans(small_symbols1 + big_symbols1, small_symbols2 + big_symbols2)
    return msg.translate(translation)


def decrypt_caesar(msg, shift=3):
    return encrypt_caesar(msg, -1 * shift)

print(encrypt_caesar("Да здравствует салат Цезарь!", 3))
print(decrypt_caesar("Зг кзугефхецих фгогх Щикгуя!", 3))