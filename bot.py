from typing import Dict, List

# Декоратор для обробки помилок
def input_error(func):
    """Декоратор для обробки помилок у функціях."""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input format."
        except IndexError:
            return "Not enough arguments."
    return inner

# Функція для додавання контакту
@input_error
def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """
    Додає контакт до словника контактів.

    Аргументи:
    - args: Список рядків, де args[0] — це ім'я, а args[1] — це номер телефону.
    - contacts: Словник контактів, де ключем є ім'я, а значенням — номер телефону.

    Повертає:
    - Рядок, що вказує на результат додавання контакту.
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Функція для отримання телефону
@input_error
def get_phone(args: List[str], contacts: Dict[str, str]) -> str:
    """
    Отримує номер телефону контакту за ім'ям.

    Аргументи:
    - args: Список рядків, де args[0] — це ім'я контакту.
    - contacts: Словник контактів, де ключем є ім'я, а значенням — номер телефону.

    Повертає:
    - Номер телефону контакту, або повідомлення про помилку, якщо контакт не знайдений.
    """
    name = args[0]
    return contacts.get(name, "Contact not found.")

def main():
    """
    Головна функція для взаємодії з користувачем і керування телефонними контактами.

    Дозволяє користувачу додавати, отримувати та перераховувати контакти або вийти з програми.
    """
    phone_numbers = {}

    while True:
        com = input("Enter a command: ").lower()

        if com == 'hello':
            print('How can I help you?')

        elif com.startswith('add'):
            parts = com.split(' ')
            if len(parts) < 3:
                print('Invalid format. Use: add [name] [number]')
            else:
                name = parts[1]
                number = parts[2]
                print(add_contact([name, number], phone_numbers))

        elif com.startswith("phone"):
            parts = com.split(" ")
            if len(parts) < 2:
                print("Invalid format. Use: phone [name]")
            else:
                name = parts[1]
                print(get_phone([name], phone_numbers))

        elif com == "all":
            if phone_numbers:
                print("Saved contacts:")
                for name, number in phone_numbers.items():
                    print(f"{name}: {number}")
            else:
                print("No contacts saved yet.")

        elif com == 'exit':
            print('Good bye!')
            break

        else:
            print('Invalid command. Try again.')

if __name__ == "__main__":
    main()
