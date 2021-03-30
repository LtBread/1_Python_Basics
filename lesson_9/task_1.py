class TrafficLight:
    def __init__(self, color='red'):
        self.__color = color

    def __str__(self):
        return f'{self.__color}'

    def switch(self):
        if self.__color == 'red':
            self.__color = 'yellow'
        elif self.__color == 'yellow':
            self.__color = 'green'
        else:
            self.__color = 'red'

    def running(self):
        for _ in range(4):
            print(self.__color)
            self.switch()


if __name__ == '__main__':
    tr = TrafficLight()
    print(tr)
    tr.running()
