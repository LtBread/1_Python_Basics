# Задание 2


def num_translate_adv(num):
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
    for en, rus in numerals.items():
        if en == num:
            return rus
        elif en.title() == num:
            return rus.title()


print(num_translate_adv('Seven'))
print(num_translate_adv('ten'))
print(num_translate_adv('10'))
