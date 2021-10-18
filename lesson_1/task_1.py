DUR_KEYS = ["сек", "мин", "час", "дн", "мес", "год (лет)"]
DIVIDERS = [60, 60, 24, 31, 12, 100]


def show_convert(interval):
    print(f'{interval}:',
          ' '.join([f'{dir_value} {dir_key}'
                    for dir_key, dir_value in convert(interval)]))


def convert(interval):
    dur_list = []
    for dur_key, divider in zip(DUR_KEYS, DIVIDERS):
        if not interval % divider == 0:
            dur_list.append([dur_key, interval % divider])
        interval = interval // divider
        if interval == 0:
            break
    dur_list.reverse()
    return dur_list


show_convert(249701)
show_convert(1617235200)
show_convert(1619827199)
durations = [59, 62, 125, 3601]
for duration in durations:
    show_convert(duration)
