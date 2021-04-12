PRICES = [97.55, 54.37, 38, 76.7, 36000, 53.5, 99.69, 40.99, 96.42, 51]


def show_prices(list_prices):
    list_prices = map(float, list_prices)
    list_prices = map(str, list_prices)
    result = [f"{int(price.split('.')[0])} руб {int(price.split('.')[1]):02d} коп"
              for price in list_prices]
    print(', '.join(result))


print('По заданию А:')
show_prices(PRICES)

print('\n', 'По заданию B:')
show_prices(PRICES)
print('Доказательство: id объекта до сортировки:', id(PRICES))
PRICES.sort()
show_prices(PRICES)
print('Доказательство: id объекта после сортировки:', id(PRICES))

print('\n', 'По заданию C:')
new_prices = sorted(PRICES, reverse=True)
show_prices(new_prices)

print('\n', 'По заданию D:')
show_prices(new_prices[:5])
