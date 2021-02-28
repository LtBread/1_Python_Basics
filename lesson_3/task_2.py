# Задание 2

numerals = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(num=None):
    for en, rus in numerals.items():
        if num == en:
            return rus
        elif num == en.title():
            return rus.title()


print(num_translate_adv('Seven'))
print(num_translate_adv('seven'))
print(num_translate_adv('одиннадцать'))
