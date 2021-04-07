class Overload(Exception):
    pass


class Helicarrier:
    unit_lifting = 'ton'

    def __init__(self, name, lifting_capacity):
        self.name = name
        self._lifting_capacity = float(lifting_capacity)
        self._passengers = []

    def __str__(self):
        return f'{self.name}, workload: {self.workload}/{self._lifting_capacity}'

    def embarkation(self, *robots):
        for robot in robots:
            self._passengers.append(robot)
        if self._lifting_capacity < self.workload:
            raise Overload(f'Overload: {self.workload}/{self._lifting_capacity}')
        return self._passengers

    def landing(self):
        pass

    @property
    def workload(self):
        return sum(self._passengers).weight


class WarRobots:
    unit_weight = 'ton'

    def __init__(self, weight, name='', pilot=''):
        self._weight = float(weight)
        self.name = name
        self.pilot = pilot
        self._is_pilot = True

    def __str__(self):
        return f'{self.name}: {self._weight} {self.unit_weight}'

    def __add__(self, other):
        return WarRobots(self._weight + other._weight)

    def __radd__(self, other):
        if not isinstance(other, WarRobots):
            return self
        return self.__add__(other)

    @property
    def weight(self):
        return self._weight


class Rhinoceros(WarRobots):
    unit_thickness = 'm'

    def __init__(self, weight, name, pilot, num_volleys, armor_thickness):
        super().__init__(weight, name, pilot)
        self._num_volleys = int(num_volleys)
        self._armor_thickness = float(armor_thickness)


class Worm(WarRobots):
    def __init__(self, weight, name, pilot, earthquake_ability):
        super().__init__(weight, name, pilot)
        self._earthquake_ability = bool(earthquake_ability)


class Octopus(WarRobots):
    def __init__(self, weight, name, pilot,
                 num_killer_tentacles, enslavement):
        super().__init__(weight, name, pilot)

        self._num_killer_tentacles = int(num_killer_tentacles)
        self._enslavement = bool(enslavement)
        self._levitation = True
        self._is_pilot = False


class Pterodactyl(WarRobots):
    unit_speed = 'km/h'

    def __init__(self, weight, name, pilot, flight_speed, kamikaze_ability):
        super().__init__(weight, name, pilot)
        self._flight_speed = float(flight_speed)
        self._kamikaze_ability = bool(kamikaze_ability)


if __name__ == '__main__':
    hammer = Rhinoceros('62', 'Hammer Wrath', 'Ivan Gromov', '5', '2.5')
    slider = Worm('14', 'Slider', 'Jane Hunn', True)
    sprite = Octopus('4', 'Sprite', 'drone', '18', False)
    arhey = Pterodactyl('3.2', 'Arhey', 'Alexander Dveen', '300', False)
    valkiria = Helicarrier('Valkiria', '80')
    valkiria.embarkation(sprite, hammer, arhey)
    print(valkiria)
    valkiria.embarkation(slider)
    print(valkiria)
