# Lesson 3

# count = 1
# while True:
#     print("count =", count)
#     count += 1

# count = 1
# while count < 100:
#     print("count =", count)
#     count += 1

# count = 1
# while count < 100:
#     print("count =", count, count < 100)
#     count = count + 1

# count = 1
# while count <= 100:
#     print("count =", count, count <= 100)
#     if count > 50:
#         print('--count', count)
#     count = count + 1

# count = 1
# for i in range(0, 100):
#     print('i =', i)

# count = 1
# for i in range(0, 100, 5):  # шаг 5
#     print('count =', count, 'i = ', i)
#     count += 1

# count = 1
# test_list = [1, 2, 3, 4, 5, 6, 34, 72, 32, 14, 52, 92, 36, 57, 'ee', True, 4.2, [11, 22], {'item': 111}]
# for i in test_list:
#     print('count =', count, 'i = ', i)
#     count += 1

# count = 1
# test_list = [1, 2, 3, 4, 5, 6, 34, 72, 32, 14, 52, 92, 36, 57]
# test_list_2 = []
# print('test_list_2_before = ', test_list_2)
# for i in test_list:
#     print('count =', count, 'i = ', i)
#     test_list_2.append(str(i + count) + ' years')
#     count += 1
# print('test_list_2_after = ', test_list_2)

# count = 1
# test_list = [1, 2, 3, 4, 5, 6, 34, 72, 32, 14, 52, 92, 36, 57]
# print('test_list.no_sort = ', test_list)
# test_list.sort()
# print('test_list.sort = ', test_list)
# # test_list = [1, 2, 3, 4, 5, 6, 34, 72, 32, 14, 52, 92, 36, 57]
# test_list_2 = []
# print('test_list_2_before = ', test_list_2)
# for i in test_list:
#     # print('count =', count, 'i = ', i)
#     item_index = test_list.index(i)
#     print('i = ', i, '| item_index = ', item_index)
#     count += 1
# # print('test_list_2_after = ', test_list_2)


# def sum_function(a, b):
#     c = a + b
#     return c
#
#
# count = 1
# test_list = [1, 2, 3, 4, 5, 6, 34, 72, 32, 14, 52, 92, 36, 57]
# for i in test_list:
#     f_result = sum_function(i, count)
#     print('function result = ', f_result)
#     count += 1

import time


def sum_function(a, b, d='vlas', e='masty'):
    c = str(a + b) + d + e
    time.sleep(.500)
    return c


count = 1
test_list = [1, 2, 3, 4, 5, 6, 34, 72, 32, 14, 52, 92, 36, 57]
start = time.time()
for i in test_list:
    f_result = sum_function(i, count, 'super', 'chill')
    print('function result = ', f_result)
    count += 1
stop = time.time()
duration = stop - start
print('duration = ', duration)
