import re


def parser(file):
    data = []
    # pattern = re.compile(r'((\d{1,3}.){3}.\d{1,3})*([GET])*(/downloads/product_\d)')
    # pattern = re.compile(r'(?:\d{1,3}.){3}\d{1,3}')
    pattern = re.compile("(?:(?:^|:)(?:[0-9a-fA-F]{0,4})){1,8}")
    with open(file, 'r', encoding='utf-8') as f:
        for num, line in enumerate(f):
            # print(line.strip())
            print(f'{num + 1}) {pattern.match(line).group(0)}')
            # data.append(pattern.match(line))
    return tuple(data)


if __name__ == '__main__':
    file_name = 'nginx_logs.txt'
    result = parser(file_name)
    # print(result)
