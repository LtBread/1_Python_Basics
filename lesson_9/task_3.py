from decimal import Decimal


class Worker:
    def __init__(self, name, surname, position, wade, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wade': wade, 'bonus': bonus}

    def __str__(self):
        return f'{self.name} {self.surname} {self.position} {self._income["wade"]} {self._income["bonus"]}'


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        result = Decimal(self._income['wade']) + Decimal(self._income['bonus'])
        return f'{result} галактических кредитов'


if __name__ == '__main__':
    kenobi = Worker("Обиван", "Кеноби", "Мастер-джедай", 150, 110)
    print(kenobi)
    skywalker = Position("Энакин", "Скайвокер", "Падаван", 120, 100)
    print(skywalker)
    print(skywalker.get_full_name())
    print(skywalker.get_total_income())
    weider = Position("Энакин", "Скайвокер", "Верховный главнокомандующий", 100, 1000)
    print(weider)
    print(weider.get_full_name())
    print(weider.get_total_income())
