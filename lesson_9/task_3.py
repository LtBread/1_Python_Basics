from decimal import Decimal


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

    def __str__(self):
        return f'{self.name} {self.surname} {self.position} {self._income}'


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        result = Decimal(self._income['wade']) + Decimal(self._income['bonus'])
        return f'{result} галактических кредитов'


if __name__ == '__main__':
    kenobi = Worker("Обиван", "Кеноби", "Мастер-джедай",
                    {'wade': 150, 'bonus': 110})
    print(kenobi)
    skywalker = Position("Энакин", "Скайвокер", "Падаван",
                         {'wade': 120, 'bonus': 100})
    print(skywalker)
    print(skywalker.get_full_name())
    print(skywalker.get_total_income())
    weider = Position("Энакин", "Скайвокер", "Верховный главнокомандующий",
                      {'wade': 100, 'bonus': 1000})
    print(weider)
    print(weider.get_full_name())
    print(weider.get_total_income())
