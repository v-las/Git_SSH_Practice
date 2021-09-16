import random
import time


def func(x, e, y):
    while e:
        if x < e < y:
            print('Вы загадали число {0}, которое больше случайного числа {1}, но меньше случайного числа {2}. '
                  'Осталось попыток: {3}'.format(str(e), str(x), str(y), str(count)))
        elif x > e > y:
            print('Вы загадали число {0}, которое меньше случайного числа {1}, но больше случайного числа {2}. '
                  'Осталось попыток: {3}'.format(str(e), str(x), str(y), str(count)))
        elif x < e > y:
            print('Вы загадали число {0}, которое больше случайных чисел {1} и {2}. Осталось попыток: {3}'.format(
                  str(e), str(x), str(y), str(count)))
        elif x > e < y:
            print('Вы загадали число {0}, которое меньше случайных чисел {1} и {2}. Осталось попыток: {3}'.format(
                  str(e), str(x), str(y), str(count)))
        elif x < e == y:
            print('Вы загадали число {0}, которое больше случайного числа {1}, и равно случайному числу {2}. '
                  'Осталось попыток: {3}'.format(str(e), str(x), str(y), str(count)))
        elif x == e < y:
            print('Вы загадали число {0}, которое равно случайному числу {1}, и меньше случайного числа {2}. '
                  'Осталось попыток: {3}'.format(str(e), str(x), str(y), str(count)))
        elif x > e == y:
            print('Вы загадали число {0}, которое меньше случайного числа {1}, и равно случайному числу {2}. '
                  'Осталось попыток: {3}'.format(str(e), str(x), str(y), str(count)))
        elif x == e > y:
            print('Вы загадали число {0}, которое равно случайному числу {1}, и больше случайного числа {2}. '
                  'Осталось попыток: {3}'.format(str(e), str(x), str(y), str(count)))
            continue
        if x == e == y:
            print('Оу, Удача! Поздравляю! Вы загадали число {0}, которое равно случайным числам {1} и {2}! '
                  'Количество попыток: {3}'.format(str(e), str(x), str(y), str(10 - count)))
            break
        pass


while True:
    print('Испытайте удачу у нас!', 'Пока бесплатно!', 'У Вас есть 10 попыток угадать случайное число.',
          'Загадайте число от 1 до 5: ', sep='\n')
    x = random.randint(1, 5)
    y = random.randint(1, 5)
    e = int(input())
    count = 10
    start = time.time()
    for i in range(9):
        count -= 1
        func(x, e, y)
        x = random.randint(1, 5)
        y = random.randint(1, 5)
        e = int(input())
    else:
        print('К сожалению, Вам не удалось угадать случайное число :(',
              'Не везет в питоне - повезёт в любви!', sep='\n')
    stop = time.time()
    duration = stop - start
    print('Ушло времени на игру:', int(duration), 'секунд.')
    print('---', '---', sep='\n')
