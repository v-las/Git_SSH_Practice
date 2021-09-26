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

# def rate_currency(keys, amount):
#     # num = {"USDCAD": 1.227148, "USDCHF": 0.935689, "USDEUR": 0.837953, "USDGBP": 0.716673}
#     listRes = []
#     for i in keys:
#         try:
#             listRes.append((round((amount/['USDRUB'])*keys[i], 1)))
#
#     return list
# input().upper()
curr_input = 'CAD'
amount_usd = 100
jsonData = {"USDCAD": 1.227148, "USDCHF": 0.935689, "USDEUR": 0.837953, "USDGBP": 0.716673}
keys = list(jsonData.keys())
values = list(jsonData.values())
# jsonData.items()
# print(jsonData, keys, values, list(jsonData.items()))
# cad_string = keys[3:]
# print(cad_string)
# for currency in keys:
#     if currency[3:] == curr_input:
#         curr_index = keys.index(currency)
#         print(curr_index)
#         print(amount_usd * values[curr_index])
def get_rate_value_from(parsed_json, currency_input):
    currency_key_list = list(parsed_json.keys())
    rate_values_list = list(parsed_json.values())
    for currency in currency_key_list:
        if currency[3:] == currency_input:
            # curr_index = currency_key_list.index(currency)
            rate_value = rate_values_list[currency_key_list.index(currency)]
            return rate_value
print(get_currency_from_keys(jsonData, curr_input))
# def get_rate_from_values(parsed_json, currency_index):
#     rate_values_list = list(parsed_json.values())



# for
# get_cad = amount_usd * values[0]
# print(get_cad)
# get_chf = amount_usd * values[1]
# print(get_chf)
# get_eur = amount_usd * values[2]
# print(get_eur)
# get_gbp = amount_usd * values[3]
# print(get_gbp)

# # def rate_currency(keys, amount):
# # num = {"USDCAD": 1.227148, "USDCHF": 0.935689, "USDEUR": 0.837953, "USDGBP": 0.716673}
# jsonData = {"USDCAD": 1.227148, "USDCHF": 0.935689, "USDEUR": 0.837953, "USDGBP": 0.716673}
# keys = jsonData.keys()
# values = jsonData.values()
# # jsonData.items()
# listRes = []
# # for i in keys:
# #     listRes.append((round((30/3['USDRUB'])*keys[i], 1)))
# #     print(listRes)
# amount = 1000
# currency = 'USD'+'CAD'
# item = ('USDCAD', 1.227148)
# # rate = item[currency]
# # rate = next(key for key in item if currency in item[key])
# rate = next(filter(lambda x: currency in item[x], item))
# print(rate)
