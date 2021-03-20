import os
import shutil

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
print(ROOT, type(ROOT))

print(os.path.dirname(__file__))
print(type(__file__))

dir_path = os.path.join('data', 'src')
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

print(dir(os))

result = shutil.copytree()