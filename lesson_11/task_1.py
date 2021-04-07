class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def converter(cls, date):
        instance = cls(cls.validator(date.split('-')))

        return instance

    @staticmethod
    def validator(date):
        date_dict = {
            'day': date[0],
            'month': date[1],
            'year': date[2]
        }
        if date_dict['day'] < 0 and date_dict['day'] > 31:
            raise ValueError('wrong date')
        if not date:
            raise ValueError('wrong date')
        return date


if __name__ == '__main__':
    my_date = Date('04-04-2021')
    print((my_date.date), type(my_date.date))

    my_date.converter('04-04-2021')
    print((my_date.date), type(my_date.date))

    my_date2 = Date.converter('04-04-2021')
    print((my_date2.date), type(my_date2.date))
