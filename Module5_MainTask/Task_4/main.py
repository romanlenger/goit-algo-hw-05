from handlers import *
from typing import Callable, Dict, List, Tuple

from variables import DATA_FILE


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    input_parts = user_input.strip().split()
    command = input_parts[0].lower()
    args = input_parts[1:]

    return command, args


def main():
    print('Hello, enter your command please (add, change, phone, all, exit)')
    contacts = load_contacts(DATA_FILE)

    command_handlers: Dict[str, Callable[..., str]] = {
        "hello": lambda: "Hello, enter your command please (add, change, phone, all, exit):",
        "add": lambda *args: add_contact(*args, contacts, DATA_FILE),
        "change": lambda *args: change_contact(*args, contacts, DATA_FILE),
        "phone": lambda *args: show_phone(*args, contacts),
        "all": show_all,
        "close": exit_bot,
        "exit": exit_bot,
    }

    while True:
        user_input = input("> ")
        command, args = parse_input(user_input)
        handler = command_handlers.get(command)

        if handler:
            response = handler(*args)
            print(response)

            if command in ["close", "exit"]:
                break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

