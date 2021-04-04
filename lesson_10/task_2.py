# import abs


class Clothes:
    units = 'm^2'

    def __init__(self, name):
        self._name = name
        self._consumption = 0

    def __str__(self):
        return f'{self._name}: {self.consumption:.2f} {self.units}'

    def __add__(self, other):
        result = Clothes('Нужно материала')
        result._consumption = self.consumption + other.consumption
        return result

    @property
    def consumption(self):
        if not self._consumption:
            self._consumption = self.calc_consumption()
        return self._consumption

    def calc_consumption(self):
        raise NotImplementedError(self.__class__.__name__)

    # @abs.abstractmethod
    # def calc_consumption(self):
    #     pass


class Coat(Clothes):
    def __init__(self, name, v):
        super().__init__(name)
        self.size = int(v)

    def __str__(self):
        return f'{self._name}: {self.consumption:.2f} {self.units}'

    def calc_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, h):
        super().__init__(name)
        self.height = float(h)

    def __str__(self):
        return f'{self._name}: {self.consumption:.3f} {self.units}'

    def calc_consumption(self):
        return 2 * self.height + 0.3


if __name__ == '__main__':
    coat = Coat('Пальто', 48)
    suit = Suit('Костюм', 1.68)
    sheepskin_coat = Coat('Полушубок', 50)
    print(coat)
    print(suit)
    print(sheepskin_coat)
    print(coat + suit + sheepskin_coat)
