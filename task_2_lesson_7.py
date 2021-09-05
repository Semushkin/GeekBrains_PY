'''
2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками»
(не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
'''

import os
import json

CONFIG_FILE = 'config.json'

with open(CONFIG_FILE, 'r', encoding='UTF-8') as f:
    params = json.loads(f.read())

for param in params:
    if not os.path.exists(param):
        os.makedirs(param)
    for file in params.get(param):
        file = os.path.join(param, file)
        if not os.path.exists(file):
            with open(file, 'w', encoding='UTF-8') as f:
                pass