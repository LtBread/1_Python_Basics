# Задание 6. Чтение

import argparse


def show_records(*args):
    with open('bakery.csv', 'r', encoding='utf-8') as file:
        print(file.read())


parser = argparse.ArgumentParser()
parser.add_argument('start', type=int)
# parser.add_argument('end', type=int)
args = parser.parse_args()
show_records(args.start)
