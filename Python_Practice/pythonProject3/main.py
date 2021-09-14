# Lesson 4

import random
import time

count = 0
test_list = [1, 2, 3, 4, 5, 6, 34, 72, 32, 14, 52, 92, 36, 57]
test_list_2 = []
print('test_list_2_before = ', test_list_2)
while True:
    count += 1
    if count > 100 and count < 200:
        time.sleep(.200)
        print('sleep == ', count)
        continue
    print('fast == ', count)
    if count >= 250:
        break

# count = 0
# test_list = [1, 2, 3, 4, 5, 6, 34, 72, 32, 14, 52, 92, 36, 57]
# test_list_2 = []
# print('test_list_2_before = ', test_list_2)
# while True:
#     count += 1
#     if count > 100 and count < 200:
#         time.sleep(.200)
#         print('sleep == ', count)
#         continue
#     print('fast == ', count)
#     if count >= 250:
#         break

# while True:
#     input_data = int(input("Enter BYN money: "))
#     if input_data < 0:
#         print('Enter number grater than 0: ')
#         continue
#     byn_to_usd = int(input_data) / 2.5
#     print('USD = ', byn_to_usd)

# created_list = [value for value in range(0, random.randint(10, 30))]
# print('created_list', created_list)

# created_list = [value for value in range(0, random.randint(10, 30))]
# second_list = []
# random_and_of_list_values = random.randint(10, 30)
# for i in range(0, random_and_of_list_values):
#     second_list.append(i)
# print('created_list', created_list)
# print('second_list', second_list)

created_list = [value for value in range(0, random.randint(10, 30))]
def main():
    input_money = get_money()
    usd_money = exchange(input_money)
    print('usd_money = ', usd_money)


def get_money():
    input_data = input('Enter UAH amount;')
    return input_data


def exchange(money):
    int_money = int(money) / 27
    return  int_money


main()