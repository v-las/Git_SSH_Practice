contraction = 'chf'.upper()
parsed_json = {"USDCAD": 1.227148, "USDCHF": 0.935689, "USDEUR": 0.837953, "USDGBP": 0.716673}
currency_key_list = list(parsed_json.keys())
rate_values_list = list(parsed_json.values())
if 'USD' + contraction in currency_key_list:
        print(contraction)
        # curr_index = currency_key_list.index(currency)
        print(rate_values_list[currency_key_list.index('USD' + contraction)])
else:
    print('invalid ent')
