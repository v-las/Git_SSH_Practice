import requests
import json

# Обменник. Скрипт запускается в консоли и работает постоянно. Остановится нажатием ctrl+c.
#     1. Скрипт сначала выводит "Выберите валюту из ['USD','EUR','CHF','GBP','CNY']"
#     2. Пользователь вводит один из 5 вариантов ['USD','EUR','CHF','GBP','CNY']
#     3. Потом Скрипт выводит "Введите сумму"  # RUB,EUR,CHF,GBP,CNY
#     4. Пользователь вводит сумму int
#     5. Скрипт выводит:
#             "Вы ввели сумму int и валюту "Валюта" "
#             "конвертированная сумма в "Валюта" = int"
#     6. Скипт должен выдать сообщение
#                 "Введите положительное число." Если число меньше 0.
#                 "Вы ввели не число. Введите число." Если введены буквы.
#                 "Вы ввели пустое поле. Введите число." Если введено пустое значение.
#     7. После сообщеня об ошибке, скрипт должен автоматом вернуться к шагу 1.
#     8. Валюту пользователя определите сами.


def main():
    """
    Function take value from input, validate and compare it with JSON.
    Then it take value from another input, validate and output value based on comparison above.
    """
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


def get_json():
    """
    Yeah, my access key laying down right here. You can get your own on website, it's free.
    A JSON parsing. It taking the JSON from the API of the website.
    JSON containing currencies and its rates, paired like keys and values.
    :return: JSON response with dict type
    """
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
    """
    It outputting currency from parsed JSON list and waiting for input.
    """
    currency_line = []
    for i in currency_list:
        currency_line.append(i[3:])
    print('', *currency_line, '', sep="|")
    result = 'Enter your currency here: '
    return result


def search_currency(contraction, currency_list, rate_list):
    """
    It validates inputted currency abbreviation with list of currencies from API.
    :param contraction: currency abbreviation from input
    :param currency_list: parsed JSON key list
    :param rate_list: parsed JSON value list
    :return: currency rate based on contraction
    """
    if contraction == '':
        result = 'Empty input. Please, enter currency from a list'
        return False, result
    currency = str('USD' + contraction)
    if currency not in currency_list:
        result = 'Invalid input. Please, enter currency from a list'
        return False, result
    # I need to replace source currency to RUB, so i do this:
    elif currency != 'USDUSD':
        result = rate_list[0] / rate_list[currency_list.index(currency)]
        return True, result
    else:
        result = rate_list[0]
        return True, result


def amount_input():
    """
    It waiting for amount input.
    :return:
    """
    print('How much money you need to convert?')
    result = 'Enter your amount here: '
    return result


def check_amount(amount):
    """
    It validates inputted amount.
    :param amount: from input
    :return: amount of money changed into sought currency by its rate.
    """
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


# JSON updating once per day
json_dict = get_json()
# Dict from parsed JSON looks like this
# json_dict = {'USDRUB': 72.880972, 'USDEUR': 0.861065, 'USDCHF': 0.929301, 'USDGBP': 0.737145, 'USDCNY': 6.446701}
# It splitting into two lists by keys and values
json_key_list = list(json_dict.keys())
json_values_list = list(json_dict.values())
# I need to replace source currency to RUB, so i do this:
json_key_list[0] = 'USDUSD'
# Beginning of main cycle
while True:
    print('...', 'You want to convert your RUB. Choose the currency from the list:', sep="\n")
    main()
    print('=====')
