# Lesson 1

print(1)    # вывод целого числа
print(2)
print('Vlas')   # вывод строки

a = 6     # обявление переменной а со значением 6

if a > 3:
    print('a =', a)

param = 1
param -= 4
param += 8
print(str(param), 'Vlas', 'Влас', str(True), '*&#@^$')
print(str(param) + 'Vlas' + 'Влас' + str(True) + '*&#@^$')

name_1, name_2, name_3 = 'sergey', 'ilya', 'yulya'
print('name1 = ', name_1)
print('name2 = ', name_2)
print('name3 = ', name_3)
name_list = [name_1, name_2, name_3]
new_list = [new_name + ' is a student' for new_name in name_list if len(new_name) > 4]
for i in name_list:
    print('name = ', i)
for i in new_list:
    print('name = ', i)

count = 0
for x in range(0, 10):
    count += 1
    print('x =', x, type(x))

count = 0
names_list = ['qq', 'qwe', 'rhe', 'wer', 'nhd', 'hgfd', 'sdv', 'sdfwef', 'wef', 'sdf']
for x in names_list:
    count += 1
    print('count #', count, '=', x, type(x))

while True:   # Бесконечный цикл с вводом в консоли
    name = input()
    print('Your input word =', name)
