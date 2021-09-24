def check_currency(currency):
    """
    Function checks if a currency was chosen right.
    :param currency:
    :return:
    """
    if currency == '':
        return print('empty'), False
    try:
        int(currency)
    except ValueError:
        return print('NaN'), False
    if int(currency) < 1:
        return print('above 0'), False
    elif 1 <= int(currency) <= 5:
        return print('your choice ', int(currency)), True,
    else:
        return print('under 6'), False


# def check_amount():


currency_list = []
while True:
    your_currency = input('choose ')
    # currency = check_currency(your_currency)
    if not check_currency(your_currency)[1]:
        continue
    your_amount = input('amount')
    if not check_amount(your_amount)[0]:
        continue

