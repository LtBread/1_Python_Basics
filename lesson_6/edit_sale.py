import sys
import re

ROW_LEN = 13


def edit(argv):
    if not argv:
        return 1
    if len(argv) == 3:
        with open('bakery.csv', 'r+', encoding='utf-8') as file:
            file.seek(0, 2)
            num_line = valid_int_converter(argv[1])
            if (num_line - 1) * ROW_LEN >= file.tell():
                raise Exception('За пределами диапазона')
            file.seek((num_line - 1) * ROW_LEN)
            file.write(f'{valid_float_converter(argv[2]):11.2f}\n')
        return 0
    raise Exception('Неверное число аргументов')


def valid_int_converter(value):
    if value.isdigit():
        return int(value)
    raise ValueError(f'Кривой параметр: {value}')


def valid_float_converter(value):
    pattern = re.compile(r'\d+(?:[.,]\d+)*$')
    if pattern.match(value):
        return float(value.replace(',', '.'))
    raise ValueError(f'не float: {value}')


if __name__ == '__main__':
    try:
        exit(edit(sys.argv))
    except ValueError as e:
        print(e)
        exit(1)
    except Exception as e:
        print(e)
        exit(2)
