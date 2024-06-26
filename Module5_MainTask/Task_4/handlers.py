from data import *
from functools import wraps
from variables import DATA_FILE


def input_error(func):
    """
    Декоратор для обробки стандартних помилок.
    """
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Provide all the required arguments."
        except TypeError:
            return "Provide all the required arguments."
            
    return inner


@input_error
def add_contact(name: str, phone: str, contacts: dict, jsonpath: str) -> str:
    contacts[name] = phone
    save_contacts(jsonpath, contacts)
    return "Contact added."


@input_error
def change_contact(name: str, phone: str, contacts: dict, jsonpath: str) -> str:
    contacts[name] = phone
    save_contacts(jsonpath, contacts)
    return "Contact updated."


@input_error
def show_phone(name: str, contacts: dict) -> str:
    return contacts[name]


@input_error
def show_all() -> str:
    contacts = load_contacts(DATA_FILE)
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def exit_bot() -> str:
    return "Good bye!"

