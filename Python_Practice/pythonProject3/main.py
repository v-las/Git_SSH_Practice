# Lesson 4

import random
import time

# count = 0
# while True:
#     count += 1
#     if 10 < count <= 30:
#         time.sleep(.200)
#         print('slow:', count)
#         continue
#     print('fast:', count)
#     if count >= 40:
#         break

# while True:
#     input_data = float(input("Enter BYN money: "))
#     if input_data <= 0:
#         print('Enter number grater than 0: ')
#         continue
#     print('your amount', input_data)
#     byn_to_usd = float(input_data) / 2.5
#     print('USD = ', byn_to_usd)

# todo генерация пустого списка?
# created_list = [value for value in range(1, random.randint(1, 10))]
# print('created_list', created_list)

# created_list = [value for value in range(1, random.randint(1, 10))]
# second_list = []
# random_and_of_list_values = random.randint(1, 10)
# for i in range(1, random_and_of_list_values):
#     second_list.append(i)
# print('created_list', created_list)
# print('second_list', second_list)


def main():
    input_money = get_money()
    usd_money = exchange(input_money)
    print('usd_money =', usd_money)


def get_money():
    input_data = input('Enter UAH amount: ')
    return input_data


def exchange(money):
    int_money = int(money) / 27
    return int_money


main()


# from package_function.imp_func import main
#
# main()
