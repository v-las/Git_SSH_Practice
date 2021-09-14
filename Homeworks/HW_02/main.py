# Python. Homework_#2

s1 = 'Alex'     # 1) Создать 2 переменных типа String с разными значениями
s2 = 'Kate'

i1 = 123        # 2) Создать 4 переменных типа Integer с разными значениями
i2 = 234
i3 = 345
i4 = 456

f1 = 1.23       # 3) Создать 3 переменных типа Float с разными значениями
f2 = 2.34
f3 = 3.45

# 4) Реализовать 15 варианта сравнения int переменных
# с операторами >, <, >=, <=, !=. Pезультаты весвести в консоль.
print(i1 != i2)     # True
print(i1 >= i2)     # False
print(i1 <= i2)     # True
print(i1 < i2)      # True
print(i1 > i2)      # False
print('---')
print(i1 <= i2 < i3)    # True
print(i1 != i2 > i3)    # False
print(i1 > i2 < i3)     # False
print(i1 < i2 != i3)    # True
print(i1 >= i2 <= i3)   # False
print('---')
print(i1 != i2 < i3 <= i4)      # True
print(i1 > i2 >= i3 != i4)      # False
print(i1 != i2 != i3 != i4)     # True
print(i1 <= i2 != i3 < i4)      # True
print(i1 > i2 > i3 > i4)        # False
print('---', '---', sep='\n')

# 5) Реализовать 9 варианта сравнения Float переменных
# с операторами >, <, >=, <=, !=. Pезультаты весвести в консоль.
print(f1 != f2)     # True
print(f1 >= f2)     # False
print(f1 <= f2)     # True
print(f1 < f2)      # True
print(f1 > f2)      # False
print('---')
print(f1 <= f2 < f3)    # True
print(f1 != f2 > f3)    # False
print(f1 > f2 < f3)     # False
print(f1 < f2 != f3)    # True
print('---', '---', sep='\n')

# 6) Реализовать 10 варианта сравнения int переменных
# с операторами >, <, >=, <=, !=
# и условными выражениями (end, or, not). Pезультаты весвести в консоль.
print(i1 <= i2 < i3 and i1 < i2 != i3)              # True
print(i1 != i2 > i3 or i1 != i2 != i3 != i4)        # True
print(not i1 > i2 < i3)                             # True
print(i1 < i2 != i3 and i1 != i2 < i3 <= i4)        # True
print(i1 >= i2 <= i3 or not i1 > i2 >= i3 != i4)    # True
print('---')
print(i1 and i2 >= i3 and i4)           # False
print(i1 > i2 or i3 >= i4)              # False
print(not i1 != i2 and i3 != i4)        # False
print(not i1 and i2 or not i3 and i4)   # False
print(i1 and i2 > i3 > i4)              # False
print('---', '---', sep='\n')

# 7) Сделать скрипт используя функцию input().
#     1. Функция должна на вход принимать целое число.
#     2. Выводить должна "Вы ввели число = (введённое число)
#     которое (меньше/больше/равно) 30"

e = int(input())
# todo Добавить ошибку нечислового ввода
# if not e:
#     print('Вы ввели не число')
while True:
    if e > 30:
        print('Вы ввели число ' + str(e) + ', которое больше 30.')
        e = int(input())
    elif e < 30:
        print('Вы ввели число ' + str(e) + ', которое меньше 30.')
        e = int(input())
        continue
    if e == 30:
        print('Поздравляем! Вы ввели число ' + str(e) + ', которое равно 30.')
        break
# else:
#     print('Вы ввели не число')
print('---', '---', sep='\n')

# 8) Сделать скрипт используя функцию input().
#     1. Функция должна на вход принимать целое число.
#     2. Внутри функции должно сгенерироваться рандомное целое число
#     (import random)...(random.randint(1, 100))
#     3. Выводить должна "Вы вели число = (введённое число)
#     которое (меньше/больше/равно) сгенерированному числу"

import random

print('У Вас есть 5 попыток угадать случайное число.', 'Загадайте число от 1 до 5: ', sep='\n')
x = random.randint(1, 5)
e = int(input())
count = 5
for attempt in range(4):
    if e > x:
        count -= 1
        print('Вы ввели число ' + str(e) + ', которое больше случайного числа ' +
              str(x) + '. Осталось попыток: ' + str(count))
        x = random.randint(1, 5)
        e = int(input())
    elif e < x:
        count -= 1
        print('Вы ввели число ' + str(e) + ', которое меньше случайного числа ' +
              str(x) + '. Осталось попыток: ' + str(count))
        x = random.randint(1, 5)
        e = int(input())
        continue
    if e == x:
        print('Поздравляю! Вы ввели число ' + str(e) + ', которое равно случайному числу '
              + str(x) + '! Количество попыток: ' + str(6 - count))
        break
else:
    print('К сожалению, Вам не удалось угадать случайное число :(')
print('---', '---', sep='\n')


# todo
# 9) Сделать скрипт используя функцию input().
#     1. Функция должна на вход принимать целое число.
#     2. Внутри функции должно сгенерироваться рандомных 2 целых числа
#     (import random)...(random.randint(1, 100))
#     3. Выводить должна "Вы вели число = (введённое число)
#     которое (меньше/больше/равно и меньше/больше/равно) сгенерированному числу"

import random

print('Испытайте удачу у нас!', 'Пока бесплатно!', 'У Вас есть 10 попыток угадать случайное число.',
      'Загадайте число от 1 до 5: ', sep='\n')
x = random.randint(1, 5)
y = random.randint(1, 5)
e = int(input())
count = 10

for attempt in range(9):
    if x < e < y:
        count -= 1
        print('Вы загадали число ' + str(e) + ', которое больше случайного числа ' + str(x) +
              ', но меньше случайного числа ' + str(y) + '. Осталось попыток: ' + str(count))
        x = random.randint(1, 5)
        y = random.randint(1, 5)
        e = int(input())
    elif x > e > y:
        count -= 1
        print('Вы загадали число ' + str(e) + ', которое меньше случайного числа ' + str(x) +
              ', но больше случайного числа ' + str(y) + '. Осталось попыток: ' + str(count))
        x = random.randint(1, 5)
        y = random.randint(1, 5)
        e = int(input())
    elif x < e > y:
        count -= 1
        print('Вы загадали число ' + str(e) + ', которое больше случайных чисел ' + str(x) +
              ' и ' + str(y) + '. Осталось попыток: ' + str(count))
        x = random.randint(1, 5)
        y = random.randint(1, 5)
        e = int(input())
    elif x > e < y:
        count -= 1
        print('Вы загадали число ' + str(e) + ', которое меньше случайных чисел ' + str(x) +
              ' и ' + str(y) + '. Осталось попыток: ' + str(count))
        x = random.randint(1, 5)
        y = random.randint(1, 5)
        e = int(input())
    elif x < e == y:
        count -= 1
        print('Вы загадали число ' + str(e) + ', которое больше случайного числа ' + str(x) +
              ', но равно случайному числу ' + str(y) + '. Осталось попыток: ' + str(count))
        x = random.randint(1, 5)
        y = random.randint(1, 5)
        e = int(input())
    elif x == e < y:
        count -= 1
        print('Вы загадали число ' + str(e) + ', которое равно случайному числу ' + str(x) +
              ', но меньше случайного числа ' + str(y) + '. Осталось попыток: ' + str(count))
        x = random.randint(1, 5)
        y = random.randint(1, 5)
        e = int(input())
    elif x > e == y:
        count -= 1
        print('Вы загадали число ' + str(e) + ', которое меньше случайного числа ' + str(x) +
              ', но равно случайному числу ' + str(y) + '. Осталось попыток: ' + str(count))
        x = random.randint(1, 5)
        y = random.randint(1, 5)
        e = int(input())
    elif x == e > y:
        count -= 1
        print('Вы загадали число ' + str(e) + ', которое равно случайному числу ' + str(x) +
              ', но больше случайного числа ' + str(y) + '. Осталось попыток: ' + str(count))
        x = random.randint(1, 5)
        y = random.randint(1, 5)
        e = int(input())
        continue
    if x == e == y:
        print('Оу, Удача! Поздравляю! Вы загадали число ' + str(e) +
              ', которое равно случайным числам ' + str(x) +
              ' и ' + str(y) + '! Количество попыток: ' + str(11 - count))
        break
else:
    print('К сожалению, Вам не удалось угадать случайное число :(',
          'Не везет в питоне - повезёт в любви!', sep='\n')

#     ----
# В заданиях 7, 8, 9, сами выберите какие условные операторы и сравнения использовать.
