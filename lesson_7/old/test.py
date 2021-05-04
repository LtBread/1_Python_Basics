import os
import shutil

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
print(ROOT, type(ROOT))

print(os.path.dirname(__file__))
print(type(__file__))

dir_path = os.path.join('data', 'src')
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

# print(dir(os))

stat = {
    1: 10,
    2: 100,
    3: 1000
}
key = 2

if key in stat:
    print('есть')

for key in stat.keys():
    print(key)

print(stat.keys(), type(stat.keys()))
