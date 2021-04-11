def formator(list_str):
    idx = 0
    while idx < len(list_str):
        if modificator(list_str[idx]):
            digit = list_str[idx]
            list_str[idx] = '"'
            list_str.insert(idx + 1, modificator(digit))
            list_str.insert(idx + 2, '"')
            idx += 2
        idx += 1


def modificator(elem):
    if elem.isdigit():
        return f'{int(elem):02d}'
    if elem.startswith('-') or elem.startswith('+'):
        if elem[1:].isdigit():
            return f'{elem[0]}{int(elem[1:]):02d}'


strings = ['В', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '-5', 'градусов']
print(strings, '\n')
formator(strings)
print('\n', strings)
print(' '.join(strings))
