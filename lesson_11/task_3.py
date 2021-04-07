class DigitError(ValueError):
    def __init__(self, txt):
        self.txt = txt


if __name__ == '__main__':
    digit_list = []
    num_inputs = 5
    while True:
        try:
            result = (input('Введите число, или "q" для завершения: '))
            if result == 'q':
                break
            elif not result.isdigit():
                raise DigitError('Только числа')
            digit_list.append(int(result))
        except DigitError as e:
            print(e.txt)
    print(*digit_list)
