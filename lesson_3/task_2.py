# Задание 2

NUMERALS = {
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


def num_translate_adv(num):

    for en, rus in NUMERALS.items():
        if en == num:
            return rus
        elif en.title() == num:
            return rus.title()


print(num_translate_adv('Seven'))
print(num_translate_adv('ten'))
print(num_translate_adv('10'))
