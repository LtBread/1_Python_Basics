import os
import shutil


def show_stat(folder_path):
    stat = {}
    size = 100000
    files_count = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if os.stat(os.path.join(root, file)).st_size < size:
                files_count += 1
                print(root, files_count)
        stat[size] = files_count
    print(stat)


if __name__ == '__main__':
    my_folder_path = 'C:/Users/Bread/Documents/[]'
    show_stat(my_folder_path)
