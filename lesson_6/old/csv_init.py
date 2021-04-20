import csv
from random import choice


def csv_reader(file_obj):
    reader = csv.reader(file_obj)
    for row in reader:
        print(" ".join(row))


def csv_writer(data, path):
    with open(path, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)


def filing():
    first_names = ["Иван", "Игорь", "Семён", "Аркадий", "Александр"]
    middle_names = ["Петрович", "Семёнович", "Георгиевич", "Николаевич"]
    last_names = ["Петренко", "Игнатенко", "Соловьёв", "Пистолетов"]
    data = []
    users = 10
    for el in range(users + 1):
        data.append(
            f'{choice(first_names)},'
            f'{choice(middle_names)},'
            f'{choice(last_names)}'
        )
    for el in data:
        print(el)
    # print(data)


if __name__ == '__main__':
    csv_path = 'users.csv'
    # csv_path = 'hobby.csv'
    with open(csv_path, 'r', encoding='utf-8') as f_obj:
        csv_reader(f_obj)
