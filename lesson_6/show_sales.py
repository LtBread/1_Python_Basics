# Задание 6. Чтение

def show_records():
    with open('bakery.csv', 'r', encoding='utf-8') as file:
        for row in file:
            print(row, end='')


if __name__ == '__main__':
    show_records()
