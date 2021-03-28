class Road:
    def __init__(self, length, width, depth=5.0, unit_weight=25.4):
        self._length = float(length.split()[0])
        self._width = float(width.split()[0])
        self._depth = depth
        self._unit_weight = unit_weight

    def weight_calc(self):
        weight = self._length * self._width * self._depth * self._unit_weight
        return f'{weight / 1000} т'


if __name__ == '__main__':
    m53 = Road('5000 м', '20 м')
    print(m53.weight_calc())
    m110 = Road('20154 м', '6 м')
    print(m110.weight_calc())
