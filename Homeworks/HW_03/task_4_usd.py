import requests
import json


def main():
    # json_dict = get_json()
    json_dict = {'USDAED': 3.673198, 'USDAFN': 89.074335, 'USDALL': 104.70609, 'USDAMD': 489.387813, 'USDANG': 1.796401,
     'USDAOA': 598.999739, 'USDARS': 98.887677, 'USDAUD': 1.374505, 'USDAWG': 1.8005, 'USDAZN': 1.703525,
     'USDBAM': 1.684369, 'USDBBD': 2.020747, 'USDBDT': 85.697812, 'USDBGN': 1.686545, 'USDBHD': 0.376947,
     'USDBIF': 1989.27801, 'USDBMD': 1, 'USDBND': 1.358033, 'USDBOB': 6.910414, 'USDBRL': 5.45501, 'USDBSD': 1.000814,
     'USDBTC': 2.0229978e-05, 'USDBTN': 74.399504, 'USDBWP': 11.283076, 'USDBYN': 2.516029, 'USDBYR': 19600,
     'USDBZD': 2.017302, 'USDCAD': 1.260015, 'USDCDF': 2004.000171, 'USDCHF': 0.926325, 'USDCLF': 0.029205,
     'USDCLP': 805.85948, 'USDCNY': 6.446699, 'USDCOP': 3790, 'USDCRC': 626.462445, 'USDCUC': 1, 'USDCUP': 26.5,
     'USDCVE': 94.960665, 'USDCZK': 21.847972, 'USDDJF': 178.167428, 'USDDKK': 6.41145, 'USDDOP': 56.385237,
     'USDDZD': 136.960136, 'USDEGP': 15.695361, 'USDERN': 15.004954, 'USDETB': 46.441603, 'USDEUR': 0.862015,
     'USDFJD': 2.118699, 'USDFKP': 0.72248, 'USDGBP': 0.733885, 'USDGEL': 3.134992, 'USDGGP': 0.72248,
     'USDGHS': 6.052696, 'USDGIP': 0.72248, 'USDGMD': 51.510825, 'USDGNF': 9764.762114, 'USDGTQ': 7.745152,
     'USDGYD': 209.246748, 'USDHKD': 7.78433, 'USDHNL': 24.11995, 'USDHRK': 6.463983, 'USDHTG': 97.757855,
     'USDHUF': 307.460021, 'USDIDR': 14239.65, 'USDILS': 3.22955, 'USDIMP': 0.72248, 'USDINR': 74.479761,
     'USDIQD': 1461.153238, 'USDIRR': 42190.000101, 'USDISK': 128.270065, 'USDJEP': 0.72248, 'USDJMD': 147.618535,
     'USDJOD': 0.708968, 'USDJPY': 111.096018, 'USDKES': 110.449698, 'USDKGS': 84.799899, 'USDKHR': 4085.207529,
     'USDKMF': 423.850278, 'USDKPW': 900.000014, 'USDKRW': 1186.854975, 'USDKWD': 0.30148, 'USDKYD': 0.83399,
     'USDKZT': 425.934299, 'USDLAK': 9970.934113, 'USDLBP': 1523.225309, 'USDLKR': 200.158462, 'USDLRD': 171.074998,
     'USDLSL': 15.069391, 'USDLTL': 2.95274, 'USDLVL': 0.60489, 'USDLYD': 4.556756, 'USDMAD': 9.048076,
     'USDMDL': 17.569058, 'USDMGA': 3963.923852, 'USDMKD': 53.063088, 'USDMMK': 1873.001623, 'USDMNT': 2839.237786,
     'USDMOP': 8.026938, 'USDMRO': 356.999828, 'USDMUR': 42.951689, 'USDMVR': 15.449937, 'USDMWK': 816.593823,
     'USDMXN': 20.58799, 'USDMYR': 4.179799, 'USDMZN': 63.830011, 'USDNAD': 15.070063, 'USDNGN': 410.81272,
     'USDNIO': 35.223246, 'USDNOK': 8.578895, 'USDNPR': 119.040094, 'USDNZD': 1.437795, 'USDOMR': 0.384508,
     'USDPAB': 1.000805, 'USDPEN': 4.133866, 'USDPGK': 3.530648, 'USDPHP': 50.699887, 'USDPKR': 171.136928,
     'USDPLN': 3.95915, 'USDPYG': 6911.566501, 'USDQAR': 3.640967, 'USDRON': 4.266599, 'USDRSD': 101.260372,
     'USDRUB': 72.617504, 'USDRWF': 1017.306044, 'USDSAR': 3.750447, 'USDSBD': 8.067802, 'USDSCR': 13.3838,
     'USDSDG': 441.000204, 'USDSEK': 8.735804, 'USDSGD': 1.357015, 'USDSHP': 1.377401, 'USDSLL': 10585.000047,
     'USDSOS': 584.999808, 'USDSRD': 21.410061, 'USDSTD': 20697.981008, 'USDSVC': 8.756723, 'USDSYP': 1257.438219,
     'USDSZL': 14.962946, 'USDTHB': 33.780052, 'USDTJS': 11.34405, 'USDTMT': 3.5, 'USDTND': 2.822498,
     'USDTOP': 2.263802, 'USDTRY': 8.853699, 'USDTTD': 6.791713, 'USDTWD': 27.8915, 'USDTZS': 2304.999682,
     'USDUAH': 26.553303, 'USDUGX': 3562.801152, 'USDUSD': 1, 'USDUYU': 42.989093, 'USDUZS': 10700.468926,
     'USDVEF': 213830222338.07285, 'USDVND': 22757.5, 'USDVUV': 111.631732, 'USDWST': 2.560319, 'USDXAF': 564.91769,
     'USDXAG': 0.044242, 'USDXAU': 0.000568, 'USDXCD': 2.70255, 'USDXDR': 0.708949, 'USDXOF': 564.91769,
     'USDXPF': 103.149678, 'USDYER': 250.125025, 'USDZAR': 15.05735, 'USDZMK': 9001.193572, 'USDZMW': 16.888529,
     'USDZWL': 321.999592}
    json_key_list = list(json_dict.keys())
    json_values_list = list(json_dict.values())
    while True:
        print('You want to convert your USD. Choose the currency from the list:')
        your_currency = input(currency_input(json_key_list)).upper()
        got_rate = search_currency(your_currency, json_key_list, json_values_list)
        if not got_rate[0]:
            print(got_rate[1])
            continue
        else:
            print('You want to convert USD into {}. Today rate - {}'.format(your_currency, got_rate[1]))
            break
    while True:
        got_amount = check_amount(input(amount_input()))
        if not got_amount[0]:
            print(got_amount[1])
            continue
        else:
            converted = got_amount[1] / got_rate[1]
            print("You'll get {} {} for your {} USD"
                  .format(round(converted, 2), your_currency, round(got_amount[1], 2)))
            break
    print('=====')


def get_json():
    # access_key = '4505e7fd8444688bd3cca12508ba4d95'
    # url = 'http://api.currencylayer.com/live'
    # head = {'access_key': access_key,'currencies': }
    # json_request = requests.get(url, params=head)
    # request_text = json_request.text
    # request_list = json.loads(request_text)
    request_list = json.loads((requests.get('http://api.currencylayer.com/live',
                                            params={'access_key': '4505e7fd8444688bd3cca12508ba4d95'})).text)
    json_response = request_list.get('quotes')
    return json_response


def currency_input(currency_list):
    currency_line = []
    for i in currency_list:
        currency_line.append(i[3:])
    print('', *currency_line, '', sep="|")
    result = 'Enter your currency here: '
    return result


def search_currency(contraction, currency_list, rate_list):
    if contraction == '':
        result = 'Empty input. Please, enter currency from a list'
        return False, result
    currency = str('USD' + contraction)
    if currency not in currency_list:
        result = 'Invalid input. Please, enter currency from a list'
        return False, result
    else:
        result = rate_list[0] / rate_list[currency_list.index(currency)]
        return True, result


def amount_input():
    print('How much money you need to convert?')
    result = 'Enter your amount here: '
    return result


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


while True:
    main()
