from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://currencyconversionapi.com/"
API_KEY = "e0ff324baa74fe3dd967e04b3e782359"

printer = PrettyPrinter()

endpoint = f'api/v1/live?access_key={API_KEY}'
url = BASE_URL + endpoint
data = get(url).json()["quotes"]
currencies = data.keys()


def get_target():
    while True:
        target = input(
            "Enter the abreviation of  your taregt currency (only 3letter): ")
        if target.isalpha() and len(target) == 3:
            target = target.upper()
            return target
        else:
            print("Invalid input, Enter the 3 letters of your currency name abreviated")


def check_target_currency(currencies, target):
    all_target_currency = []
    for currency in currencies:
        x = currency[-3:]
        all_target_currency.append(x)

    if target in all_target_currency:
        print('Valid target currency\n')
        print('-'*20)
        get_currencies(data, target)

    else:
        print(f'{target} is not supported')


def get_currencies(data, target):
    code = "USD"+target
    print(f"1 USD", end=" | ")
    print(f'{data[code]} {target}')


def main():
    while True:
        target = get_target()
        check_target_currency(currencies, target)

        convert_again = input(
            "Do you want to convert another currency to USD (y/n): ")
        if convert_again.isalpha() and convert_again.lower() == 'y':
            continue
        else:
            print("\nBye")
            exit()


main()
