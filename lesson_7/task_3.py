import os
import shutil


def reform_dir(root_dir, search_file='index.html'):
    templates = 'templates'
    templates_path = os.path.join(root_dir, templates)
    if os.path.exists(templates_path):
        shutil.rmtree(templates_path)
    os.mkdir(templates_path)
    for root, dirs, files in os.walk(root_dir):
        if root == templates_path:
            break
        if search_file in set(files):
            found_dir = os.path.split(root)[1]
            curr_path = os.path.join(templates_path, found_dir)
            os.mkdir(curr_path)
            for file in files:
                shutil.copy(os.path.join(root, file), curr_path)


if __name__ == '__main__':
    my_dir = './my_project'
    my_file = 'base.html'
    try:
        reform_dir(my_dir)
    except Exception as e:
        print(e)
        exit(1)
