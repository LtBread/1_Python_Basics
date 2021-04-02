class Cell:
    def __init__(self, num):
        self.num = int(num)

    def __str__(self):
        return f'{self.num}'

    def __add__(self, other):
        return self.__class__(self.num + other.num)

    def __sub__(self, other):
        if self.num > other.num:
            return self.__class__(self.num - other.num)
        else:
            return f'Subzero'

    def __mul__(self, other):
        return self.__class__(self.num * other.num)

    def __floordiv__(self, other):
        return self.__class__(self.num // other.num)

    def make_order(self, cols):
        result = self.num // int(cols) * f'{int(cols) * "* "}\n'
        result += f'{self.num % int(cols) * "* "}'
        print(result)


if __name__ == '__main__':
    cell_1 = Cell(20)
    cell_2 = Cell(2)
    cell_3 = Cell(5)
    print(cell_1 + cell_2 + cell_3)
    print(cell_2 - cell_1)
    print(cell_1 * cell_2 * cell_3)
    print(cell_1 // cell_2 + cell_3)
    cell_1.make_order(5)
    cell_2.make_order(3)
