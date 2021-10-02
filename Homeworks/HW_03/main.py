import requests
import json


def main():
    json_key_list = list(json_dict.keys())
    json_key_list[0] = 'USDUSD'
    while True:
        print('You want to convert your RUB. Choose the currency from the list:')
        for i in json_key_list:
            print(i[3:], sep=', ')
        your_currency = input('Enter your currency here: ').upper()
        got_rate = search_currency(your_currency, json_dict)
        if not got_rate[0]:
            print(got_rate[1])
            input('Press enter to continue')
            continue
        else:
            print('You want to convert RUB into {}. Today rate - {}'.format(your_currency, got_rate[1]))
            break
    while True:
        print('How much money you need to convert?')
        your_amount = input('Enter your amount here: ')
        got_amount = check_amount(your_amount)
        if not got_amount[0]:
            print(got_amount[1])
            continue
        else:
            converted = got_amount[1] / got_rate[1]
            print(
                "You'll get {} {} for your {} RUB".format(round(converted, 2), your_currency, round(got_amount[1], 2)))
            break
    input('Press enter to continue')
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


def search_currency(contraction, parsed_json):
    currency_key_list = list(parsed_json.keys())
    currency_key_list[0] = 'USDUSD'
    rate_values_list = list(parsed_json.values())
    if contraction == '':
        result = 'Empty input. Please, enter currency from a list'
        return False, result
    currency = str('USD' + contraction)
    if currency not in currency_key_list:
        result = 'Invalid input. Please, enter currency from a list'
        return False, result
    elif currency != 'USDUSD':
        result = rate_values_list[0] / rate_values_list[currency_key_list.index(currency)]
        return True, result
    else:
        result = rate_values_list[0]
        return True, result


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
        result = 'We can\'t convert 0 USD. Please, enter an amount'
        return False, result
    else:
        return True, amount


json_dict = get_json()
while True:
    main()
