class MyZeroDivisionError(ZeroDivisionError):
    def __init__(self, txt):
        self.txt = txt


if __name__ == '__main__':
    try:
        number = int(input('Введите делитель: '))
        if number == 0:
            raise MyZeroDivisionError('divide by zero is still bad')
    except MyZeroDivisionError as e:
        print(e)
    else:
        result = 1 / number
        print(f'{result:.2f}')
