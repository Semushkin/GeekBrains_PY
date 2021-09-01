'''
2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего
задания.
Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых
превышает объем ОЗУ компьютера.
'''
F_NAME = 'nginx_logs.txt'

spams = dict()

def read_file(name):
    with open(name, 'r', encoding='UTF-8') as f:
        for pars in f:
            pars = pars.split()
            if pars[0] in spams:
                spams[pars[0]] += 1
            else:
                spams[pars[0]] = 1
    return spams


spams = read_file(F_NAME)
count_r = max(spams.values())
for spammer in spams:
    if spams.get(spammer) == count_r:
        print(f'Spammer: {spammer}, count: {count_r}')