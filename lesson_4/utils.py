import requests
from decimal import Decimal
from datetime import date


def currency_rates(currency_code=None):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    cur_date = content.split('Date="')[1][:10].split('.')
    cur_date = date(day=int(cur_date[0]), month=int(cur_date[1]), year=int(cur_date[2]))
    for el in content.split('<CharCode>')[1:]:
        char_code = el[:3]
        value = (el.split('<Value>')[1:][0].split('</Value>')[0])
        value = Decimal(f'{value.split(",")[0]}.{value.split(",")[1]}')
        nominal = Decimal(el.split('<Nominal>')[1:][0].split('</Nominal>')[0])
        if str(currency_code).upper() == char_code:
            return cur_date, value / nominal


def show_currency_rates(dat_rat_tuple=None):
    answer = currency_rates(dat_rat_tuple)
    if answer is None:
        print(answer)
    else:
        print(*answer)


if __name__ == '__main__':
    print(*currency_rates('usd'))
    print(*currency_rates('GBP'))
