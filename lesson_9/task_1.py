class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def __str__(self):
        return f'{self.__color}'

    def running(self):
        pass


if __name__ == '__main__':
    tr = TrafficLight('red')
    print(tr)
    tr.running()