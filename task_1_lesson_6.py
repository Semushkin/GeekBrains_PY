'''
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить
список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]
Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
'''
F_NAME = 'nginx_logs.txt'


def read_file(name):
    with open(name, 'r', encoding='UTF-8') as f:
        for pars in f:
            pars = pars.split()
            yield pars[0], pars[5].replace('"', ''), pars[6]


content_read = read_file(F_NAME)  # Чтение содержимого файла, разбитие на строки.
for result in content_read:
    print(result)