# Lesson 3

# count = 1
# while True:
#     print("count =", count)
#     count += 1

# while count < 100:
#     print("count =", count)
#     count += 1

# while count < 100:
#     print("count =", count)
#     count = count + 1

# while count <= 100:
#     print("count =", count)
#     count = count + 1

# while count <= 100:
#     print("count =", count, count <= 100)
#     if count > 50:
#         print('--count', count)
#     count = count + 1

# for i in range(0, 100):
#     print('i =', i)

# for i in range(0, 100, 5):  # шаг 5
#     print('i =', i)

# for i in range(0, 100, 5):  # шаг 5
#     print('count =', count, 'i = ', i)
#     count += 1

# test_list = [1, 2, 3, 4, 5, 6, 34, 72, 32, 14, 52, 92, 36, 57, 'ee', True, 4.2, [11, 22], {"item": 111}]
# for i in test_list:
#     print('count =', count, 'i = ', i)
#     count += 1

# test_list = [1, 2, 3, 4, 5, 6, 34, 72, 32, 14, 52, 92, 36, 57]
# test_list_2 = []
# print('test_list_2_before = ', test_list_2)
# for i in test_list:
#     print('count =', count, 'i = ', i)
#     test_list_2.append(str(i + count) + ' years')
#     count += 1
# print('test_list_2_after = ', test_list_2)

# test_list = [1, 2, 3, 4, 5, 6, 34, 72, 32, 14, 52, 92, 36, 57]
# test_list_2 = []
# print('test_list_2_before = ', test_list_2)
# for i in test_list:
#     print('count =', count, 'i = ', i)
#     test_list_2.append(str(i + count) + ' years')
#     count += 1
# print('test_list_2_after = ', test_list_2)
import time

count = 0
test_list = [1, 2, 3, 4, 5, 6, 34, 72, 32, 14, 52, 92, 36, 57]
test_list_2 = []
print('test_list_2_before = ', test_list_2)
while True:
    count += 1
    if 100 < count <= 150:
        time.sleep(.200)
        print('slow:', count)
        continue
    print('fast:', count)
    if count >= 200:
        break
