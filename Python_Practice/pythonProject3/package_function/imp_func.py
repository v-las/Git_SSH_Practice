# def main():
#     input_money = get_money()
#     usd_money = exchange(input_money)
#     print('usd_money =', usd_money)
#
#
# def get_money():
#     input_data = input('Enter UAH amount: ')
#     return input_data
#
#
# def exchange(money):
#     int_money = int(money) / 27
#     return int_money
#
#
# main()
#
#

import random
import time

a = 1
b = 2
c = 3
count = 4
var_list = tuple('c', 'a', 'b', 'count')
result = ('Вы загадали число {0}, которое больше случайного числа {1}, но меньше случайного числа {2}. '
          'Осталось попыток: {3}'.format(str(var_list)))
print(result)
