# def json_split(parsed_json):
#     currency_key_list = list(parsed_json.keys())
#     rate_values_list = list(parsed_json.values())
#     return currency_key_list, rate_values_list
# def check_currency(currency_input, splited_json):
#     if currency_input == '':
#         result = 'empty currency'
#         return False, result
#     try:
#         currency_input = str(currency_input)
#     except ValueError:
#         return False, print('NaN currency')
#     for currency in splited_json[1]:
#         if currency_input == splited_json[:3]:
#             return print(currency)
json_data = {"USDCAD": 1.227148, "USDCHF": 0.935689, "USDEUR": 0.837953, "USDGBP": 0.716673}
print(json_data)
currency_key_list = list(json_data.keys())
print(currency_key_list)
rate_values_list = list(json_data.values())
print(rate_values_list)
json_tuple = (currency_key_list, rate_values_list)
print(json_tuple)
your_currency = input('choose ').upper()
print(your_currency)
if your_currency == '':
    result = 'empty currency'
    print(result)
for currency in json_tuple[0]:
    if currency[3:] == your_currency:
        rate_value = rate_values_list[currency_key_list.index(currency)]
        print(rate_value)



# employer = {'id1': {'name': "Джон", 'Familia': "Трамп", 'Otchestvo': "Дональдович", 'Telefon': "33-33-33"},
#             'id2': {'name': "Владимир", 'Familia': "Путин", 'Otchestvo': "Владимирович", 'Telefon': "8(912)911911911"}}
#
# name1 = input("Введите имя: ")
# flag = True
#
# for search_emploers in employer:
#     if employer[search_emploers]['name'] == name1:
#         print(employer[search_emploers]['Telefon'])
#         flag = False
#
# if flag:
#     print('нет такого значения')