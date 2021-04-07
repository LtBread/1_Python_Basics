import re


class ComplexNumber:
    def __init__(self, c_num):
        self._c_num = c_num

    def __str__(self):
        return f'{self._c_num}'

    # (a + bi) ± (c + di) = (a ± c) + (b ± d)i

    def __add__(self, other):
        a = int(self.valid_num['a'])
        b = int(self.valid_num['b'])
        c = int(other.valid_num['a'])
        d = int(other.valid_num['b'])
        if b == 0 and d == 0:
            return self.__class__(f'{a + c}')
        return self.__class__(f"{a + c} + {b + d}i")

    # (a + bi) · (c + di) = (ac – bd) + (ad + bc)i

    def __mul__(self, other):
        a = int(self.valid_num['a'])
        b = int(self.valid_num['b'])
        c = int(other.valid_num['a'])
        d = int(other.valid_num['b'])
        if b == 0 and d == 0:
            return self.__class__(f'{a * c}')
        return self.__class__(f"{a * c - b * d} + {a * d + b * c}i")

    @property
    def valid_num(self):
        pattern_c = re.compile(r'(?P<a>\d+)\s*\+\s*(?P<b>\d+)i')
        result_c = pattern_c.search(f'{self._c_num}')
        if result_c:
            return result_c.groupdict()
        elif f'{self._c_num}'.isdigit:
            return {'a': self._c_num, 'b': '0'}
        raise ValueError(f'wrong value {self._c_num}')


if __name__ == '__main__':
    num_1 = ComplexNumber('7 + 1i')
    num_2 = ComplexNumber('2 + 2i')
    num_3 = ComplexNumber('1 + 3i')
    num_4 = ComplexNumber(5)
    num_5 = ComplexNumber(6)
    print((num_1 + num_2 + num_5) * num_3 * num_4)
