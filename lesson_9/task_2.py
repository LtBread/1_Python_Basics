class Road:
    def __init__(self, length, width):
        self._length = float(length.split()[0])
        self._width = float(width.split()[0])

    def weight_calc(self, depth, unit_weight):
        weight = self._length * self._width * depth * unit_weight
        return f'{weight / 1000} т'


if __name__ == '__main__':
    m53 = Road('5000 м', '20 м')
    print(m53.weight_calc(5.0, 25.4))
    m110 = Road('20154 м', '6 м')
    print(m110.weight_calc(4.0, 25.4))
