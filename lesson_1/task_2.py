# Задание 2

numbers = []

for number in range(1000):
    if number % 2 != 0:
        numbers.append(number ** 3)


# Реализация без преобразования типа
sum_result = 0
for num in numbers:
    rem = 0
    integer = num
    while integer != 0:
        rem += integer % 10
        integer = integer // 10
        # print('Вывод:', num, integer, rem)
    if rem % 7 == 0:
        sum_result += num

print('sum_result =', sum_result)
# конец реализации

sum_result = 0
for number in numbers:
    sum_div_7 = 0
    number = str(number)
    for item in number:
        item = int(item)
        sum_div_7 += item
    number = int(number)
    if sum_div_7 % 7 == 0:
        sum_result += number

print('sum_result =', sum_result)

sum_result = 0
for number in numbers:
    sum_div_7 = 0
    number += 17
    number = str(number)
    for item in number:
        item = int(item)
        sum_div_7 += item
    number = int(number)
    if sum_div_7 % 7 == 0:
        sum_result += number

print('sum_result =', sum_result)

# Реализация без преобразования типа
sum_result = 0
for num in numbers:
    num += 17
    rem = 0
    integer = num
    while integer != 0:
        rem += integer % 10
        integer = integer // 10
    if rem % 7 == 0:
        sum_result += num

print('sum_result =', sum_result)
# конец реализации
