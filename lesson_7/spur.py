import os
import shutil


def director():
    root_dir = './'  # '\' - бэкслэш использовать нежелательно, на линуксе он сломает код.
    files = os.listdir(root_dir)
    for item in files:
        print(item, os.path.isdir(item))
        print(item, os.path.isfile(item))

    # Упрощает верхнеуказанное

    for item in os.scandir(root_dir):
        print(type(item), item)
        print(dir(item))
        print(item.name, item.is_dir())
        print(item.name, item.is_file())

    # рекурсивный поиск

    for root, dirs, files in os.walk(root_dir):
        # print(root)
        for file in files:
            # print(root)
            # print(file)
            f_path = os.path.join(root, file)
            print(f_path, os.path.exists(f_path))  # проверка существования
            # print(os.stat(f_path))  # статы файла
            # print(os.stat(f_path).st_size)
            # print(os.path.abspath(f_path))
            # print(os.path.split(f_path))    #
            # print(os.path.dirname(f_path))
            # print(os.path.basename(f_path))

    # лайфхак, показывающий текущую директорию
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
    print(ROOT)

    root = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    # Создание папки по абсолютному пути
    dir_name = 'new_dir'
    dir_path = os.path.join(root, dir_name)
    # os.mkdir(dir_path)
    # os.rmdir(dir_path)
    os.makedirs('dir_par/dir_cld')  # Создает петку папок

    # удаляет непустую директорию
    shutil.rmtree(dir_path)

    # Копирование файлов через питон всегда медленно
    # os.walk() коварен

"""
    Тут всякие заметки
    str.replace(',', '.')   замена символа
    Принцип Python - Ask for forgiveness then permission. никогда не проси разрешения.  
"""


"""
    А тут Try Except 
"""


def try_except_theory():
    pass
