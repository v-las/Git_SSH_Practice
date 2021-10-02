def check_currency(contraction):
    if contraction == '':
        result = 'empty currency'
        return False, result
    else:
        result = str(contraction).upper()
        return True, result


def search_currency(contraction, parsed_json):
    currency_key_list = list(parsed_json.keys())
    rate_values_list = list(parsed_json.values())
    for currency in currency_key_list:
        if currency[3:] != contraction:
            result = 'invalid ent'
            return False, result
        else:
            result = rate_values_list[currency_key_list.index(currency)]
            return True, result


def check_amount(amount):
    if amount == '':
        return False, print('empty amount')
    try:
        amount = float(amount)
    except ValueError:
        return False, print('NaN amount')
    if amount <= 0:
        return False, print('above 0 amount')
    else:
        return True, amount


json_data = {"USDCAD": 1.227148, "USDCHF": 0.935689, "USDEUR": 0.837953, "USDGBP": 0.716673}
your_currency = input('choose ')
print('1', your_currency)
got_currency = check_currency(your_currency)
print('2', got_currency[1])
if not got_currency[0]:
    print('3 fail', got_currency[1])
got_rate = search_currency(got_currency[1], json_data)
if not got_rate[0]:
    print('4 fail', got_rate[1])
else:
    print('4.1 nice', got_rate[1])
your_amount = input('amount ')
if not check_amount(your_amount)[0]:
    print('5', check_amount(your_amount)[1])
else:
    got_amount = check_amount(your_amount)
    print('6', got_rate[1], got_amount[1])
