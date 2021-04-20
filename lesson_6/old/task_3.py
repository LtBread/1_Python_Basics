# Задание 3

from itertools import zip_longest
import pickle

users = []
hobbies = []

with open('users.csv', 'r', encoding='utf-8') as f:
    for line in f:
        users.append(line.strip())

with open('hobby.csv', 'r', encoding='utf-8') as f:
    for line in f:
        hobbies.append(line.strip())

if len(users) < len(hobbies):
    exit(1)

hobbies_of_users = {user: hobby for (user, hobby) in zip_longest(users, hobbies)}

with open('hobbies_of_users.pickle', 'wb') as f:
    pickle.dump(hobbies_of_users, f)

with open('hobbies_of_users.pickle', 'rb') as f:
    content = pickle.load(f)

print(type(content))
for el in content.items():
    print(el)
