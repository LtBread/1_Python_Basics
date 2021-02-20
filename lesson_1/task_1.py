# Задание 1

durations = [55, 114, 3756, 4865634, 157134324] # Промежутки времени в секундах
for duration in durations:
    # больше года
    if (60 ** 3) * 24 * 31 < duration < (60 ** 3) * 24 * 31 * 12:
        print(duration // (60 ** 3) * 24 * 31, 'лет', duration // (60 ** 3) * 24 * 31, 'мес', duration // (60 ** 3) * 24, 'сут', duration // 60 ** 2, 'час', duration // 60, 'мин', duration % 60, 'сек')
    # до года
    elif (60 ** 3) * 24 < duration < (60 ** 3) * 24 * 31:
        print(duration // (60 ** 3) * 24, 'мес', duration // (60 ** 3) * 24, 'сут', duration // 60 ** 2, 'час', duration // 60, 'мин', duration % 60, 'сек')
    # до месяца
    elif 60 ** 3 < duration < (60 ** 3) * 24:
        print(duration // 60 ** 3, 'сут', duration // 60 ** 2, 'часа', duration // 60, 'мин', duration % 60, 'сек')
    # до суток
    elif 60 ** 2 < duration < 60 ** 3:
        print(duration // 60 ** 2, 'час', duration // 60, 'мин', duration % 60, 'сек')
    # до часа
    elif 60 < duration < 60 ** 2:
        print(duration // 60, 'мин', duration % 60, 'сек')
    # до минуты
    else:
        print(duration, 'сек')

