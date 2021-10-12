import requests
import json


def main():
    json_dict = get_json()
    # json_dict = {'USDRUB': 72.880972, 'USDEUR': 0.861065, 'USDCHF': 0.929301, 'USDGBP': 0.737145, 'USDCNY': 6.446701}
    json_key_list = list(json_dict.keys())
    json_values_list = list(json_dict.values())
    json_key_list[0] = 'USDUSD'
    print('You want to convert your RUB. Choose the currency from the list:')
    while True:
        your_currency = input(currency_input(json_key_list)).upper()
        got_rate = search_currency(your_currency, json_key_list, json_values_list)
        if not got_rate[0]:
            print('-', got_rate[1], '-', sep="\n")
            continue
        else:
            print('-', 'You want to convert RUB into {}. Today rate - {}'.format(your_currency, got_rate[1]), sep="\n")
            break
    while True:
        got_amount = check_amount(input(amount_input()))
        if not got_amount[0]:
            print('-', got_amount[1], '-', sep="\n")
            continue
        else:
            converted = got_amount[1] / got_rate[1]
            print('-', "You'll get {} {} for your {} RUB"
                  .format(round(converted, 2), your_currency, round(got_amount[1], 2)), sep="\n")
            break
    print('=====')


def get_json():
    access_key = '4505e7fd8444688bd3cca12508ba4d95'
    url = 'http://api.currencylayer.com/live'
    head = {'access_key': access_key, 'currencies': 'RUB,EUR,CHF,GBP,CNY', 'source': 'USD', 'format': '1'}
    json_request = requests.get(url, params=head)
    request_text = json_request.text
    request_list = json.loads(request_text)
    # request_list = json.loads((requests.get('http://api.currencylayer.com/live',
    #                                         params={'access_key': '4505e7fd8444688bd3cca12508ba4d95'})).text)
    json_response = request_list.get('quotes')
    return json_response


def currency_input(currency_list):
    currency_line = []
    for i in currency_list:
        currency_line.append(i[3:])
    print('', *currency_line, '', sep="|")
    result = 'Enter your currency here: '
    return result


def search_currency(contraction, currency_list, rate_list):
    if contraction == '':
        result = 'Empty input. Please, enter currency from a list'
        return False, result
    currency = str('USD' + contraction)
    if currency not in currency_list:
        result = 'Invalid input. Please, enter currency from a list'
        return False, result
    elif currency != 'USDUSD':
        result = rate_list[0] / rate_list[currency_list.index(currency)]
        return True, result
    else:
        result = rate_list[0]
        return True, result


def amount_input():
    print('How much money you need to convert?')
    result = 'Enter your amount here: '
    return result


def check_amount(amount):
    if amount == '':
        result = 'Empty input. Please, enter an amount'
        return False, result
    try:
        amount = abs(float(amount))
    except ValueError:
        result = 'It\'s not a number. Please, enter an amount'
        return False, result
    if amount <= 0:
        result = 'We can\'t convert 0 RUB. Please, enter an amount'
        return False, result
    else:
        return True, amount


while True:
    main()
