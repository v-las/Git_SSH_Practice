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


jsonData = {"USDCAD": 1.227148, "USDCHF": 0.935689, "USDEUR": 0.837953, "USDGBP": 0.716673}
keys = list(jsonData.keys())
values = list(jsonData.values())
jsonData.items()
print(jsonData, keys, '|', values, '|', list(jsonData.items()))
# def rate_currency(keys, amount):
# num = {"USDCAD": 1.227148, "USDCHF": 0.935689, "USDEUR": 0.837953, "USDGBP": 0.716673}
jsonData = {"USDCAD": 1.227148, "USDCHF": 0.935689, "USDEUR": 0.837953, "USDGBP": 0.716673}
keys = jsonData.keys()
values = jsonData.values()
# jsonData.items()
listRes = []
# for i in keys:
#     listRes.append((round((30/3['USDRUB'])*keys[i], 1)))
#     print(listRes)
amount = 1000
currency = 'USD'+'CAD'
item = ('USDCAD', 1.227148)
# rate = item[currency]
# rate = next(key for key in item if currency in item[key])
rate = next(filter(lambda x: currency in item[x], item))
print(rate)
