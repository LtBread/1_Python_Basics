class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return f'{self.matrix}'

    def __add__(self, other):
        pass


if __name__ == '__main__':
    filling_1 = [
        [1, 5, 6],
        [6, 2, 7],
        [4, 0, 3]
    ]
    mtx_1 = Matrix(filling_1)
    print(mtx_1)
    filling_2 = [
        [0, 7, 3],
        [5, 2, 6],
        [3, 8, 7]
    ]
    mtx_2 = Matrix(filling_2)
    print(mtx_2)
    print(mtx_1 + mtx_2)
