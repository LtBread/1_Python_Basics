from itertools import zip_longest


def create_dict(file_left, file_right):
    dictionary = {}
    with open(file_left, 'r', encoding='utf-8') as f_l:
        with open(file_right, 'r', encoding='utf-8') as f_r:
            for row_l, row_r in zip_longest(f_l, f_r):
                if not row_l:
                    raise StopIteration('Закончились ключи')
                dictionary[clean_key(row_l)] = clean_value(row_r)
    return dictionary


def save_dict(dictionary, center_file):
    with open(center_file, 'w', encoding='utf-8') as f:
        f.write(to_string(dictionary))


def to_string(dictionary):
    data_list = [f'{key}: {value}' for key, value in dictionary.items()]
    return '\n'.join(data_list)


def show_check(file):
    with open(file, 'r', encoding='utf-8') as f:
        print(f.read())


def show(dictionary):
    for key, value in dictionary.items():
        print(f'{key}: {value}')


def clean_key(string):
    if not string:
        return string
    return ' '.join(map(str.strip, string.split(','))).strip()


def clean_value(string):
    if not string:
        return string
    return ', '.join(map(str.strip, string.split(','))).strip()


if __name__ == '__main__':
    file_keys = 'task_3_data/Gods.csv'
    file_values = 'task_3_data/Makra.csv'
    file_result = 'task_3_data/Aspects.txt'
    try:
        created = create_dict(file_keys, file_values)
        save_dict(created, file_result)
        show_check(file_result)
    except StopIteration as e:
        print(e)
        exit(1)
