import random
import string


def generate_email(name='ananas'):
    random_email = ''.join(random.choices(string.ascii_lowercase, k=4))
    return f'{name}_{random_email}@yandex.ru'
