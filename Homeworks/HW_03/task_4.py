# Задача №4
# Обменник. Скрипт запускается в консоли и работает постоянно. Остановится нажатием ctrl+c.
#     1. Скрипт сначала выводит "Выберите валюту из ['USD','EUR','CHF','GBP','CNY']"
#     2. Пользователь вводит один из 5 вариантов ['USD','EUR','CHF','GBP','CNY']
#     3. Потом Скрипт выводит "Введите сумму"
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


def search_currency(contraction, parsed_json):
    currency_key_list = list(parsed_json.keys())
    rate_values_list = list(parsed_json.values())
    if contraction == '':
        result = 'Empty input. Please, enter currency from a list'
        return False, result
    currency = str('USD' + contraction)
    if currency not in currency_key_list:
        result = 'Invalid input. Please, enter currency from a list'
        return False, result
    else:
        result = rate_values_list[currency_key_list.index(currency)]
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


json_data = {"USDCAD": 1.227148, "USDCHF": 0.935689, "USDEUR": 0.837953, "USDGBP": 0.716673}
while True:
    print('You want to convert your USD. Choose the currency:')
    for i in list(json_data.keys()):
        print(i[3:], sep=', ')
    while True:
        your_currency = input('Enter your currency here: ').upper()
        got_rate = search_currency(your_currency, json_data)
        if not got_rate[0]:
            print(got_rate[1])
            continue
        else:
            print('You want to convert USD into {}. Today rate - {}'.format(your_currency, got_rate[1]))
            break
    while True:
        print('How much money you need to convert?')
        your_amount = input('Enter your amount here: ')
        got_amount = check_amount(your_amount)
        if not got_amount[0]:
            print(got_amount[1])
            continue
        else:
            converted = got_rate[1] * got_amount[1]
            print("You'll get {} {} for your {} USD".format(round(converted, 2), your_currency, round(got_amount[1], 2)))
            break
    print('=====')
