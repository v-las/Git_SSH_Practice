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

def check_currency(number):
    if number == '':
        result = 'empty currency'
        return result, False
    try:
        number = int(number)
    except ValueError:
        return print('NaN currency'), False
    if number < 1:
        return print('above 0 currency'), False
    elif number > 4:
        return print('under 5 currency'), False
    else:
        currency_index = number - 1
        return print('your currency', number), currency_index


def check_amount(amount):
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


def get_rate_value_from(parsed_json, currency_input):
    currency_key_list = list(parsed_json.keys())
    rate_values_list = list(parsed_json.values())
    for currency in currency_key_list:
        if currency[3:] == currency_input:
            # curr_index = currency_key_list.index(currency)
            rate_value = rate_values_list[currency_key_list.index(currency)]
            return rate_value


# curr_input = input().upper()
# amount_usd = float(input())

json_data = {"USDCAD": 1.227148, "USDCHF": 0.935689, "USDEUR": 0.837953, "USDGBP": 0.716673}
while True:
    your_currency = input('choose ')
    # currency = check_currency(your_currency)
    if not check_currency(your_currency)[1]:
        continue
    your_amount = input('amount ')
    if not check_amount(your_amount)[1]:
        continue
    get_rate = check_amount(your_amount) * get_rate_value_from(json_data, your_currency)
    print(round(get_rate, 2))
