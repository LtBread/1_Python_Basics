class TrafficLight:

    def __init__(self):
        self.__color = 'red'

    def __str__(self):
        return f'{self.__color}'

    def running(self):
        if self.__color == 'red':
            self.__color = 'yellow'
        elif self.__color == 'yellow':
            self.__color = 'green'
        else:
            self.__color = 'red'


if __name__ == '__main__':
    tr = TrafficLight()
    print(tr)
    tr.running()
    print(tr)
    tr.running()
    print(tr)
    tr.running()
    print(tr)
    tr.running()
