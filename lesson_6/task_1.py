# Зададние 1

data = []
row_data = []

with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    for row in file:
        raw_row = row.split()
        row_data = [raw_row[0], raw_row[5][1:], raw_row[6]]
        data.append(tuple(row_data))
print(data)
