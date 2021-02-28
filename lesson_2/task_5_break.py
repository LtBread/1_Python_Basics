# Задание 5

# Если забуду это вырезать, прошу не обращать внимание.
# import random
# prices = []
# for price in range(20):
#     price = str(random.randint(10, 100))
#     cop = str(random.randint(0, 99))
#     price = f'{price}.{cop}'
#     price = float(price)
#     prices.append(price)
#     # print(type(price))
# print(prices)

prices = [97.2, 54.37, 38.34, 76.7, 97.28, 53.5, 99.69, 40.99,
          96.42, 51.38, 64.1, 92.53, 96.68, 78.19, 72.64, 34.16,
          80.66, 17.73, 54.15, 41.72]

# A
print('По заданию А:')
for idx in range(len(prices)):
    prices[idx] = str(prices[idx])
    prices[idx] = prices[idx].split('.')
    prices[idx] = f'{int(prices[idx][0]):.0f} руб {int(prices[idx][1]):02d} коп'

prices = ', '.join(prices)
print(prices)

# B
print('По заданию B:')
print(prices)
print('Доказательство: id объекта до сортировки:', id(prices))
prices = prices.split(', ')
prices.sort()
prices = ', '.join(prices)
print(prices)
print('Доказательство: id объекта после сортировки:', id(prices))

# C
print('По заданию C:')
prices = prices.split(', ')
new_prices = sorted(prices, reverse=True)
new_prices = ', '.join(new_prices)
print(new_prices)

# D
print('По заданию D:')
new_prices = new_prices.split(', ')
new_prices = new_prices[:4]
new_prices = ', '.join(new_prices)
print(new_prices)
