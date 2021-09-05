'''
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание:
подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
'''

import os

FOLDER_MAIN = 'my_project'
FOLDER = ['settings', 'mainapp', 'adminapp', 'authapp']

root = os.path.join(os.path.dirname(__file__), FOLDER_MAIN)

if os.path.exists(root):
    for folder_list in FOLDER:
        sub_folder = os.path.join(root, folder_list)
        if not os.path.exists(sub_folder):
            os.mkdir(sub_folder)
        else:
            print(f'Folder "{folder_list}" already exists')
else:
    os.mkdir(root)
    for folder_list in FOLDER:
        sub_folder = os.path.join(root, folder_list)
        os.mkdir(sub_folder)