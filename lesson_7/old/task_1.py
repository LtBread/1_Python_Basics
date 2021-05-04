from os import path, mkdir
from shutil import rmtree


def create_starter(dir_path, dir_name, folders):
    current_path = path.join(dir_path, dir_name)
    if not path.exists(current_path):
        mkdir(current_path)
    for folder in folders:
        current_folder = path.join(current_path, folder)
        if not path.exists(current_folder):
            mkdir(current_folder)


def destroy_starter(dir_path, dir_name):
    current_path = path.join(dir_path, dir_name)
    rmtree(current_path)


if __name__ == '__main__':
    my_name = 'my_first_project'
    my_path = './'
    my_folders = ('settings', 'mainapp', 'adminapp', 'authapp')
    try:
        create_starter(my_path, my_name, my_folders)
        # destroy_starter(my_path, my_name)
    except Exception as e:
        print(e)
