# Задание 1

def odd_nums_gen(nums):
    for n in range(1, nums + 1, 2):
        yield n


odd_to_nums = odd_nums_gen(5)
print(next(odd_to_nums))
print(next(odd_to_nums))
print(next(odd_to_nums))
print(next(odd_to_nums))
