# Задание 5

prices = [97, 54.37, 38.34, 76.7, 97.28, 53.5, 99.69, 40.99,
          96.42, 51.38, 64.1, 92.53, 96.68, 78.19, 72.64, 34.16,
          80.66, 17.73, 54.15, 41.72, 120, 1540]


def prices_show(list_prices):
    for idx in range(len(list_prices)):
        price = str(float(list_prices[idx]))
        price = price.split('.')
        price = f'{int(price[0]):.0f} руб {int(price[1]):02d} коп'
        print(price, end='')
        if idx != len(prices) - 1:
            print(end=', ')
    print(end='\n')


# A

print('По заданию А:')
prices_show(prices)

# B

print('По заданию B:')
prices_show(prices)
print('Доказательство: id объекта до сортировки:', id(prices))
prices.sort()
prices_show(prices)
print('Доказательство: id объекта после сортировки:', id(prices))

# C

print('По заданию C:')
new_prices = sorted(prices, reverse=True)
prices_show(new_prices)

# D
print('По заданию D:')
new_prices = new_prices[:5]
prices_show(new_prices)
