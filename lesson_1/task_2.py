# Задание 2

numbers = []

for number in range(1000):
    if number % 2 != 0:
        numbers.append(number ** 3)

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