# write your code here!
import requests
import json
import pprint

pp = pprint.PrettyPrinter(indent=4)


def save_exchange_rates(rate):
    rate_request = requests.get(f'http://www.floatrates.com/daily/{rate}.json')

    if rate_request:
        response_dict = json.loads(rate_request.text)
        exchange_rates_dict[rate] = response_dict


exchange_rates_dict = {}
default_rates = ['usd', 'eur']

# save USD and EUR json data to dict
for default_rate in default_rates:
    save_exchange_rates(default_rate)


currency = input().lower()

while True:
    exchange_currency = input().lower()

    if exchange_currency != "":
        amount = float(input())

        print('Checking the cache...')

        if exchange_currency in exchange_rates_dict:
            print('Oh! It is in the cache!')

            exchange_amount = amount * exchange_rates_dict[exchange_currency][currency]['inverseRate']

            print(f'You received {round(exchange_amount, 2)} {exchange_currency.upper()}.')
        else:
            print('Sorry, but it is not in the cache!')

            save_exchange_rates(exchange_currency)

            exchange_amount = amount * exchange_rates_dict[exchange_currency][currency]['inverseRate']

            print(f'You received {round(exchange_amount, 2)} {exchange_currency.upper()}.')
    else:
        break
