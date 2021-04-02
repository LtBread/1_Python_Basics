import random

ROWS = 3
COLS = 3


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result_row = ''
        for row in self.matrix:
            result = ''
            for el in row:
                result += f'{el}\t'
            result_row += f'\n{result}\n'
        return f'{result_row}'

    def __add__(self, other):
        filling = []
        for row_f, row_l in zip(self.matrix, other.matrix):
            _row = []
            for el_f, el_l in zip(row_f, row_l):
                _row.append(el_f + el_l)
            filling.append(_row)
        return self.__class__(filling)


def fill():
    filling = []
    for row in range(ROWS):
        _row = []
        for el in range(COLS):
            _row.append(random.randint(-10, 10))
        filling.append(_row)
    return filling


if __name__ == '__main__':
    mtx_1 = Matrix(fill())
    print(mtx_1)
    mtx_2 = Matrix(fill())
    print(mtx_2)
    mtx_3 = Matrix(fill())
    print(mtx_3)
    print(mtx_1 + mtx_2 + mtx_3)
