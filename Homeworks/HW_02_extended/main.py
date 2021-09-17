import random
import time


def compare_function(x, y, e):
    for i in range(1):
        if x < e < y:
            print('Вы загадали число ' + str(e) + ', которое больше случайного числа ' + str(x) +
                  ', но меньше случайного числа ' + str(y) + '. Осталось попыток: ' + str(count))
            return result1
        elif x > e > y:
            print('Вы загадали число ' + str(e) + ', которое меньше случайного числа ' + str(x) +
                  ', но больше случайного числа ' + str(y) + '. Осталось попыток: ' + str(count))
            return result1
        elif x < e > y:
            print('Вы загадали число ' + str(e) + ', которое больше случайных чисел ' + str(x) +
                  ' и ' + str(y) + '. Осталось попыток: ' + str(count))
            return result1
        elif x > e < y:
            print('Вы загадали число ' + str(e) + ', которое меньше случайных чисел ' + str(x) +
                  ' и ' + str(y) + '. Осталось попыток: ' + str(count))
            return result1
        elif x < e == y:
            print('Вы загадали число ' + str(e) + ', которое больше случайного числа ' + str(x) +
                  ', и равно случайному числу ' + str(y) + '. Осталось попыток: ' + str(count))
            return result1
        elif x == e < y:
            print('Вы загадали число ' + str(e) + ', которое равно случайному числу ' + str(x) +
                  ', и меньше случайного числа ' + str(y) + '. Осталось попыток: ' + str(count))
            return result1
        elif x > e == y:
            print('Вы загадали число ' + str(e) + ', которое меньше случайного числа ' + str(x) +
                  ', и равно случайному числу ' + str(y) + '. Осталось попыток: ' + str(count))
            return result1
        elif x == e > y:
            print('Вы загадали число ' + str(e) + ', которое равно случайному числу ' + str(x) +
                  ', и больше случайного числа ' + str(y) + '. Осталось попыток: ' + str(count))
            continue
            return result1
        if x == e == y:
            print('Оу, Удача! Поздравляю! Вы загадали число ' + str(e) +
                  ', которое равно случайным числам ' + str(x) +
                  ' и ' + str(y) + '! Количество попыток: ' + str(11 - count))
            break
            return result2


while True:
    print('Испытайте удачу у нас!', 'Пока бесплатно!', 'У Вас есть 10 попыток угадать случайное число.',
          'Загадайте число от 1 до 5: ', sep='\n')
    x = random.randint(1, 5)
    y = random.randint(1, 5)
    e = int(input())
    count = 10
    start = time.time()
    for attempt in range(9):
    #     if x < e < y:
            count -= 1
    #         print('Вы загадали число ' + str(e) + ', которое больше случайного числа ' + str(x) +
    #               ', но меньше случайного числа ' + str(y) + '. Осталось попыток: ' + str(count))
            if not attempt:
                compare_function(x, y, e)
                x = random.randint(1, 5)
                y = random.randint(1, 5)
                e = int(input())
            elif attempt:

    #     elif x > e > y:
    #         count -= 1
    #         print('Вы загадали число ' + str(e) + ', которое меньше случайного числа ' + str(x) +
    #               ', но больше случайного числа ' + str(y) + '. Осталось попыток: ' + str(count))
    #         x = random.randint(1, 5)
    #         y = random.randint(1, 5)
    #         e = int(input())
    #     elif x < e > y:
    #         count -= 1
    #         print('Вы загадали число ' + str(e) + ', которое больше случайных чисел ' + str(x) +
    #               ' и ' + str(y) + '. Осталось попыток: ' + str(count))
    #         x = random.randint(1, 5)
    #         y = random.randint(1, 5)
    #         e = int(input())
    #     elif x > e < y:
    #         count -= 1
    #         print('Вы загадали число ' + str(e) + ', которое меньше случайных чисел ' + str(x) +
    #               ' и ' + str(y) + '. Осталось попыток: ' + str(count))
    #         x = random.randint(1, 5)
    #         y = random.randint(1, 5)
    #         e = int(input())
    #     elif x < e == y:
    #         count -= 1
    #         print('Вы загадали число ' + str(e) + ', которое больше случайного числа ' + str(x) +
    #               ', и равно случайному числу ' + str(y) + '. Осталось попыток: ' + str(count))
    #         x = random.randint(1, 5)
    #         y = random.randint(1, 5)
    #         e = int(input())
    #     elif x == e < y:
    #         count -= 1
    #         print('Вы загадали число ' + str(e) + ', которое равно случайному числу ' + str(x) +
    #               ', и меньше случайного числа ' + str(y) + '. Осталось попыток: ' + str(count))
    #         x = random.randint(1, 5)
    #         y = random.randint(1, 5)
    #         e = int(input())
    #     elif x > e == y:
    #         count -= 1
    #         print('Вы загадали число ' + str(e) + ', которое меньше случайного числа ' + str(x) +
    #               ', и равно случайному числу ' + str(y) + '. Осталось попыток: ' + str(count))
    #         x = random.randint(1, 5)
    #         y = random.randint(1, 5)
    #         e = int(input())
    #     elif x == e > y:
    #         count -= 1
    #         print('Вы загадали число ' + str(e) + ', которое равно случайному числу ' + str(x) +
    #               ', и больше случайного числа ' + str(y) + '. Осталось попыток: ' + str(count))
    #         x = random.randint(1, 5)
    #         y = random.randint(1, 5)
    #         e = int(input())
    #         continue
    #     if x == e == y:
    #         print('Оу, Удача! Поздравляю! Вы загадали число ' + str(e) +
    #               ', которое равно случайным числам ' + str(x) +
    #               ' и ' + str(y) + '! Количество попыток: ' + str(11 - count))
    #         break
    # else:
                print('К сожалению, Вам не удалось угадать случайное число :(',
                        'Не везет в питоне - повезёт в любви!', sep='\n')
    stop = time.time()
    duration = stop - start
    print('Ушло времени на игру:', int(duration), 'секунд.')
    print('---', '---', sep='\n')