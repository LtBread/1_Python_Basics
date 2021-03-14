# Задание 6. Запись

import argparse
from decimal import Decimal


def write_records(sale):
    with open('bakery.csv', 'a', encoding='utf-8') as file:
        file.write(f'{sale}\n')


parser = argparse.ArgumentParser()
parser.add_argument('sale', type=str)
arg = parser.parse_args()
write_records(arg.sale)

