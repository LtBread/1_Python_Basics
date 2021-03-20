from os import path, mkdir
from shutil import rmtree


def create_starter(dir_name, dir_path='./', folders=None):
    current_path = path.join(dir_path, dir_name)
    mkdir(path.join(dir_path, dir_name))
    if folders:
        for folder in folders:
            mkdir(path.join(path.abspath(current_path), folder))


def destroy_starter(dir_name, dir_path='./'):
    current_path = path.join(dir_path, dir_name)
    rmtree(current_path)


if __name__ == '__main__':
    my_name = 'my_project'
    my_path = 'C:/Users/Bread/Desktop'
    my_folders = ('settings', 'mainapp', 'adminapp', 'authapp')
    try:
        create_starter(my_name, folders=my_folders)
        # destroy_starter(my_name)
    except Exception as e:
        print(e.args[1])
