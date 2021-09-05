'''
3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён);
предусмотреть возможные исключительные ситуации;
это реальная задача, которая решена, например, во фреймворке django.
'''
import os
import shutil

MAIN_FOLDER = 'my_project'
TEMPLATES_FOLDER = 'templates'

params = os.walk(MAIN_FOLDER)
for folder_main, folders_sub, files in params:
    template_new = os.path.join(MAIN_FOLDER, TEMPLATES_FOLDER)
    if os.path.basename(folder_main) == TEMPLATES_FOLDER and not folder_main == template_new:
        for folder in folders_sub:
            folder_target = os.path.join(folder_main, folder)
            try:
                shutil.copytree(folder_target, os.path.join(template_new, folder))
            except FileExistsError as e:
                print(f' Error!!!: {e}')