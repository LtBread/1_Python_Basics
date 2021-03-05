# Задание 5

from random import choice, shuffle


def get_jokes(num=1, repeat=False):
    """
    Функция формирования шуток

    Возвращает num шуток из трёх случайных слов,
    по одному из каждого списка.

    :param num:
    :param repeat:
    :return:

    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    list_jokes = []
    for joke in range(num):
        list_jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')

    # for joke in range(num):
    #     noun = map(shuffle, nouns)
    #     list_jokes.append(f'{nouns.pop()} {adverbs.pop()} {adjectives.pop()}')

    return list_jokes


print(get_jokes(repeat=True, num=3))

# for noun, adverb, adjective in zip(nouns, adverbs, adjectives):
#     print(f'{noun} {adverb} {adjective}')
