# Задание 2

strings = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
strings_format = []

print(strings)

# Выявить числа

for idx in range(len(strings)):
    if strings[idx].isdigit():  # Костыль
        strings[idx] = int(strings[idx])  # Возможно костыль
        strings[idx] = f'{strings[idx]:02d}'  # Возможно костыль

print(strings)

for idx in range(len(strings)):
    print(type(strings[idx]))

# print(ex_list[1].isdigit())
# string = ''.join(strings)
