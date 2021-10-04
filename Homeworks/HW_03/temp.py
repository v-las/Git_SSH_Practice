def currency_input():
    while True:
        your_currency = input('Enter your currency here: ').upper()
        got_rate = search_currency(your_currency)
        if not got_rate[0]:
            result = got_rate[1]
            input('Press enter to continue')
            continue
        else:
            result = 'You want to convert RUB into {}. Today rate - {}'.format(your_currency, got_rate[1])
            break
    return result


def search_currency(contraction):
    if contraction == '':
        result = 'Empty input. Please, enter currency from a list'
        return False, result
    currency = str('USD' + contraction)
    if currency not in json_key_list:
        result = 'Invalid input. Please, enter currency from a list'
        return False, result
    elif currency != 'USDUSD':
        result = json_values_list[0] / json_values_list[json_key_list.index(currency)]
        return True, result
    else:
        result = json_values_list[0]
        return True, result


def amount_input():
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


# json_dict = get_json()
json_dict = {'USDRUB': 72.880972, 'USDEUR': 0.861065, 'USDCHF': 0.929301, 'USDGBP': 0.737145, 'USDCNY': 6.446701}
json_key_list = list(json_dict.keys())
json_values_list = list(json_dict.values())
json_key_list[0] = 'USDUSD'
while True:
    print('You want to convert your RUB. Choose the currency from the list:')
    for i in json_key_list:
        print(i[3:], sep=', ')
    currency_input()
    amount_input()
    input('Press enter to continue')
    print('=====')
    # main()
