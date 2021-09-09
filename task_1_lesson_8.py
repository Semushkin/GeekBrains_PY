'''
1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и
почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
Пример:
#>>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
#>>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл в
данном случае использовать функцию re.compile()?
'''
import re

mail = 'rkzton@yandex.ru'
user = {'username': '', 'domain': ''}
mark_1 = r'@'
mark_2 = r'\.'


def mail_validator(mail):
    if len(re.compile(mark_1).findall(mail)) != 1 or len(mail) < 6 or len(re.compile(mark_2).findall(mail)) != 1:
        raise ValueError()
    return mail

try:
    mail = mail_validator(mail)
except ValueError:
    print(f'Wrong email: {mail}')
else:
    result = re.compile(mark_1).search(mail)
    user['username'] = mail[:result.span()[0]]
    user['domain'] = mail[result.span()[1]:]
    print(user)
finally:
    print('End')
