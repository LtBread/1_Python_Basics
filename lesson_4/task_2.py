# Задание 2

import requests
from decimal import Decimal


def currency_rates(currency_code):
    response = requests.get(r'http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    for el in content.split('<CharCode>')[1:]:
        char_code = el[:3]
        value = (el.split('<Value>')[1:][0].split('</Value>')[0])
        value = Decimal(f'{value.split(",")[0]}.{value.split(",")[1]}')
        nominal = Decimal(el.split('<Nominal>')[1:][0].split('</Nominal>')[0])
        course = value / nominal
        if currency_code.upper() == char_code:
            return course


print(currency_rates('eur'))
print(currency_rates('USD'))
print(currency_rates('12'))

# print(response.status_code)
# print(response.content)
# print(type(response.content))
# print(response.content.decode(encoding=response.encoding))
# print(type(response.content.decode(encoding=response.encoding)))
