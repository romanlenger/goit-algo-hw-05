import json
import os
from typing import Callable, Dict
from functools import wraps


def load_contacts_error(func: Callable[[str], Dict]) -> Callable[[str], Dict]:
    """
    Декоратор який обробляє випадок, коли json файл відсутній. 
    При помилці поверне пустий список, який потім буде записаний в новий створений файл функцією save_contacts.
    """
    @wraps(func)
    def inner(filepath: str) -> Dict:
        try:
            return func(filepath)
        except (FileNotFoundError, json.JSONDecodeError, OSError):
            print('Now you don\'t have contacts.')
            return {}
        
    return inner


@load_contacts_error
def load_contacts(filepath: str) -> Dict:
    with open(filepath, 'r') as file:
        contacts_dict = json.load(file)
        count = len(contacts_dict)
        print(f'You have {count} contacts')

        return contacts_dict


def save_contacts(filepath, contacts):
    with open(filepath, 'w') as file:
        json.dump(contacts, file)