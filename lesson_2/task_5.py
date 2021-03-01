# Задание 5

prices = [97, 54.37, 38.34, 76.7, 97.28, 53.5, 99.69, 40.99,
          96.42, 51.38, 64.1, 92.53, 96.68, 78.19, 72.64, 34.16,
          80.66, 17.73, 54.15, 41.72]

# A
print('По заданию А:')
for idx in range(len(prices)):
    prices[idx] = str(prices[idx])
    price = prices[idx].split('.')
    if len(price) == 1:
        price = f'{int(price[0]):.0f} руб {0:02d} коп'
    else:
        price = f'{int(price[0]):.0f} руб {int(price[1]):02d} коп'
    print(price, end='')
    if idx != len(prices) - 1:
        print(end=', ')
print(end='\n')

# B
print('По заданию B:')
for idx in range(len(prices)):
    price = prices[idx].split('.')
    if len(price) == 1:
        price = f'{int(price[0]):.0f} руб {0:02d} коп'
    else:
        price = f'{int(price[0]):.0f} руб {int(price[1]):02d} коп'
    print(price, end='')
    if idx != len(prices) - 1:
        print(end=', ')
print(end='\n')
print('Доказательство: id объекта до сортировки:', id(prices))

prices.sort()

for idx in range(len(prices)):
    price = prices[idx].split('.')
    if len(price) == 1:
        price = f'{int(price[0]):.0f} руб {0:02d} коп'
    else:
        price = f'{int(price[0]):.0f} руб {int(price[1]):02d} коп'
    print(price, end='')
    if idx != len(prices) - 1:
        print(end=', ')
print(end='\n')
print('Доказательство: id объекта после сортировки:', id(prices))

# C
print('По заданию C:')
new_prices = sorted(prices, reverse=True)
for idx in range(len(new_prices)):
    new_prices[idx] = str(new_prices[idx])
    new_prices[idx] = new_prices[idx].split('.')
    if len(new_prices[idx]) == 1:
        new_prices[idx] = f'{int(new_prices[idx][0]):.0f} руб {0:02d} коп'
    else:
        new_prices[idx] = f'{int(new_prices[idx][0]):.0f} руб {int(new_prices[idx][1]):02d} коп'
    print(new_prices[idx], end='')
    if idx != len(new_prices) - 1:
        print(end=', ')
print(end='\n')

# D
print('По заданию D:')
new_prices = new_prices[:5]
new_prices = ', '.join(new_prices)
print(new_prices)
