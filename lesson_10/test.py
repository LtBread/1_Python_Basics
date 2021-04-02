

filling_1 = [
        [1, 5, 6],
        [6, 2, 7],
        [4, 0, 3]
    ]

filling_2 = [
    [0, 7, 3],
    [5, 2, 6],
    [3, 8, 6]
]

filling_3 = []

for row_1, row_2 in zip(filling_1, filling_2):
    _row = []
    for el_1, el_2 in zip(row_1, row_2):
        _row.append(el_1 + el_2)
    filling_3.append(_row)
print(filling_3)
