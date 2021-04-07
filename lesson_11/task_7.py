import re


class ComplexNumber:
    def __init__(self, c_num):
        self._c_num = c_num

    def __str__(self):
        return f'{self._c_num}'

    # (a + bi) ± (c + di) = (a ± c) + (b ± d)i
    def __add__(self, other):
        return self.__class__(
            f"{int(self.valid_num['a']) + int(other.valid_num['a'])} + "
            f"{int(self.valid_num['b']) + int(other.valid_num['b'])}i")

    # (a + bi) · (c + di) = (ac – bd) + (ad + bc)i
    def __mul__(self, other):
        return self.__class__(
            f"{(int(self.valid_num['a']) * int(other.valid_num['a']) - int(self.valid_num['b']) * int(other.valid_num['b'])) + (int(self.valid_num['a']) * int(other.valid_num['b']) + int(self.valid_num['b']) * int(other.valid_num['a']))}i")

    @property
    def valid_num(self):
        pattern = re.compile(r'(?P<a>\d+)\s*\+\s*(?P<b>\d+)i')
        result = pattern.search(self._c_num)
        if not result:
            raise ValueError(f'wrong value {self._c_num}')
        return result.groupdict()


if __name__ == '__main__':
    num_1 = ComplexNumber('4 + 2i')
    num_2 = ComplexNumber('15 + 2i')
    num_3 = ComplexNumber('1 + 4i')
    print(num_1.valid_num)
    print(num_1 + num_2 + num_3)
    print(num_1 * num_2 * num_3)
