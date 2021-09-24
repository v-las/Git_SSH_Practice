def check_currency(currency):
    """
    Function checks if a currency was chosen right.
    :param currency:
    :return:
    """
    if currency == '':
        result = 'empty currency'
        return result, False
    try:
        currency = int(currency)
    except ValueError:
        return print('NaN currency'), False
    if currency < 1:
        return print('above 0 currency'), False
    elif currency > 5:
        return print('under 6 currency'), False
    else:
        return print('your currency', currency), currency


def check_amount(amount):
    """
    Function checks if a amount was input right.
    :param amount:
    :return:
    """
    if amount == '':
        return print('empty amount'), False
    try:
        amount = float(amount)
    except ValueError:
        return print('NaN amount'), False
    if amount <= 0:
        return print('above 0 amount'), False
    else:
        return print('your amount', amount), amount


# def rate_currency(rate_list, amount):
#     num = {"USDCAD": 1.227148, "USDCHF": 0.935689, "USDEUR": 0.837953, "USDGBP": 0.716673}
#     listRes = []
#     for i in rate_list:
#         try:
#             listRes.append((round((amount/[]))))
#
#     return list


jsonData = {"USDCAD": 1.227148, "USDCHF": 0.935689, "USDEUR": 0.837953, "USDGBP": 0.716673}
keys = jsonData.keys()
values = jsonData.values()
jsonData.items()
print(keys, '|', values, '|', jsonData.items())
while True:
    your_currency = input('choose ')
    # currency = check_currency(your_currency)
    if not check_currency(your_currency)[1]:
        continue
    your_amount = input('amount ')
    if not check_amount(your_amount)[1]:
        continue
    s = rate_currency(currency_list, your_amount)
    print('entered {} {}'.format(your_amount, 'USD'))
    # print('converted sum {} = {}'.format(currency_list[your_currency], s))
