# Задание 2

strings = ['В', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
strings_mod = []
strings_format = []

print(strings)

for idx in range(len(strings)):
    # Проверка элемента списка на число и число со знаком
    char_detected = False
    char_t_detected = False
    string = strings[idx]
    for inx in range(len(string)):
        if inx == 0 and string[inx] == '+' or string[inx] == '-':
            char_t_detected = True
            continue

        if 48 <= ord(string[inx]) <= 57:
            char_detected = True
        else:
            char_detected = False
            break

    if char_t_detected and char_detected:
        strings[idx] = f'{strings[idx][0]}{int(strings[idx][1:]):02d}'
        quotes_t = ['"', strings[idx], '"']
        strings_mod.extend(quotes_t)
        quotes_t = ''.join(quotes_t)
        strings_format.append(quotes_t)
    elif char_detected:
        strings[idx] = f'{int(strings[idx]):02d}'
        quotes = ['"', strings[idx], '"']
        strings_mod.extend(quotes)
        quotes = ''.join(quotes)
        strings_format.append(quotes)
    else:
        strings_mod.append(strings[idx])
        strings_format.append(strings[idx])

print(strings)
print(strings_mod)
strings_format = ' '.join(strings_format)
print(strings_format)
