from colorama import Fore


def required_input(input_message, error_message):
    value = input(input_message).strip()

    while not value:
        print(Fore.LIGHTRED_EX + error_message)

        value = input(Fore.WHITE + input_message).strip()

    return value
