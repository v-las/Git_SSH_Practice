import random
import time


def compare_function(x, e, y):
    if x < e < y:
        result_1: str = ('Вы загадали число ' + str(e) + ', которое больше случайного числа ' + str(x) +
                         ', но меньше случайного числа ' + str(y) + '. Осталось попыток: ' + str(count))
        return result_1
    # elif x > e > y:
    #     result_1: str = ('Вы загадали число ' + str(e) + ', которое меньше случайного числа ' + str(x) +
    #                      ', но больше случайного числа ' + str(y) + '. Осталось попыток: ' + str(count))
    #     return result_1
    # elif x < e > y:
    #     result_1: str = ('Вы загадали число ' + str(e) + ', которое больше случайных чисел ' + str(x) +
    #                      ' и ' + str(y) + '. Осталось попыток: ' + str(count))
    #     return result_1
    # elif x > e < y:
    #     result_1: str = ('Вы загадали число ' + str(e) + ', которое меньше случайных чисел ' + str(x) +
    #                      ' и ' + str(y) + '. Осталось попыток: ' + str(count))
    #     return result_1
    # elif x < e == y:
    #     result_1: str = ('Вы загадали число ' + str(e) + ', которое больше случайного числа ' + str(x) +
    #                      ', и равно случайному числу ' + str(y) + '. Осталось попыток: ' + str(count))
    #     return result_1
    # elif x == e < y:
    #     result_1: str = ('Вы загадали число ' + str(e) + ', которое равно случайному числу ' + str(x) +
    #                      ', и меньше случайного числа ' + str(y) + '. Осталось попыток: ' + str(count))
    #     return result_1
    # elif x > e == y:
    #     result_1: str = ('Вы загадали число ' + str(e) + ', которое меньше случайного числа ' + str(x) +
    #                      ', и равно случайному числу ' + str(y) + '. Осталось попыток: ' + str(count))
    #     return result_1
    # elif x == e > y:
    #     result_1: str = ('Вы загадали число ' + str(e) + ', которое равно случайному числу ' + str(x) +
    #                      ', и больше случайного числа ' + str(y) + '. Осталось попыток: ' + str(count))
    #     return result_1
    # # if x == e == y:
    elif x == e == y:
        result_2: str = ('Оу, Удача! Поздравляю! Вы загадали число ' + str(e) +
                         ', которое равно случайным числам ' + str(x) +
                         ' и ' + str(y) + '! Количество попыток: ' + str(11 - count))
        return result_2


while True:
    # print('Испытайте удачу у нас!', 'Пока бесплатно!', 'У Вас есть 10 попыток угадать случайное число.',
    #       'Загадайте число от 1 до 5: ', sep='\n')
    a = random.randint(1, 5)
    b = random.randint(1, 5)
    c = int(input())
    compare_function(a, b, c)
    count = 10
    start = time.time()
    for attempt in range(9):
        count -= 1
        compare_function(a, b, c)
        while True:
            print(result_1)
            x = random.randint(1, 5)
            y = random.randint(1, 5)
            e = int(input())
            continue
        else:
            print(result_2)
        break
    else:
        print('К сожалению, Вам не удалось угадать случайное число :(',
                  'Не везет в питоне - повезёт в любви!', sep='\n')
    stop = time.time()
    duration = stop - start
    print('Ушло времени на игру:', int(duration), 'секунд.')
    print('---', '---', sep='\n')
