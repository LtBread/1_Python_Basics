import random

ROWS = 3
COLS = 3


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = '\n\n'.join(['\t'.join([f'{el}' for el in row])
                              for row in self.matrix])
        return f'{result}\n'

    def __add__(self, other):
        filling = [[(el_f + el_l) for el_f, el_l in zip(row_f, row_l)]
                   for row_f, row_l in zip(self.matrix, other.matrix)]
        return self.__class__(filling)


def fill():
    return [[random.randint(-10, 10) for _ in range(COLS)]
            for _ in range(ROWS)]


if __name__ == '__main__':
    mtx_1 = Matrix(fill())
    print(mtx_1)
    mtx_2 = Matrix(fill())
    print(mtx_2)
    mtx_3 = Matrix(fill())
    print(mtx_3)
    print(mtx_1 + mtx_2 + mtx_3)
