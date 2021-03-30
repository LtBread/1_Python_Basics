class Car:
    is_police = False

    def __init__(self, speed, color, name):
        self._speed = float(speed)
        self._color = color
        self._name = name
        self._is_police = False

    def __str__(self):
        return f'{self._speed} {self._color} {self._name} {self._is_police}'

    def go(self):
        return f'{self._name} went.'

    def stop(self):
        return f'{self._name} stopped.'

    def turn(self, direction):
        if direction == '<':
            return f'{self._name} turned left.'
        elif direction == '>':
            return f'{self._name} turned right.'
        else:
            raise ValueError('wrong symbol!')

    def show_speed(self):
        return f'{self._speed} km/h'


class TownCar(Car):
    def show_speed(self):
        if self._speed > 60:
            return f'{self._speed} km/h, over speed!'
        return f'{self._speed} km/h'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self._speed > 40:
            return f'{self._speed} km/h, over speed!'
        return f'{self._speed} km/h'


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self._is_police = True


if __name__ == '__main__':
    kamaz = WorkCar('120.4', 'yellow', 'KAMAZ')
    print(kamaz)
    print(kamaz.go())
    print(kamaz.show_speed())
    print(kamaz.turn('<'))
    print(kamaz.turn('>'))
    print(kamaz.stop())

    lada_calina = SportCar('270', 'red', 'LADA Calina Sport')
    print(lada_calina)

    lada_priora = PoliceCar('240', 'blue-white', 'LADA Priora')
    print(lada_priora)
