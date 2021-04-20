import sys


ROW_LEN = 13


def show(argv):
    """
    Оптимизирована
    :param argv:
    :return:
    """
    if not argv:
        return 1
    with open('bakery.csv', 'r', encoding='utf-8') as file:
        if len(argv) == 1:
            start = 1
            stop = None
        elif len(argv) == 2:
            start = valid_int_converter(argv[1])
            stop = None
        elif len(argv) == 3:
            start = valid_int_converter(argv[1])
            stop = valid_int_converter(argv[2])
            if stop < start:
                raise Exception('Кривой диапазон')
        else:
            raise Exception('Избыток аргументов')
        file.seek((start - 1) * ROW_LEN)
        line = file.readline()
        while line:
            print(line.strip())
            if int(file.tell() / ROW_LEN) == stop:
                break
            line = file.readline()
    return 0


def valid_int_converter(value):
    if value.isdigit():
        return int(value)
    raise ValueError(f'Кривой параметр: {value}')


if __name__ == '__main__':
    try:
        exit(show(sys.argv))
    except ValueError as e:
        print(e)
        exit(1)
    except Exception as e:
        print(e)
        exit(2)

