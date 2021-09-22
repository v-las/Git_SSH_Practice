import random
import time


def compare_function(x, y, e, c):
    if x < e < y:
        result_1 = ('Вы загадали число {0}, которое больше случайного числа {1}, но меньше случайного числа {2}. '
                    'Осталось попыток: {3}'.format(str(e), str(x), str(y), str(c)))
        return result_1, False
    elif x > e > y:
        result_2 = ('Вы загадали число ' + str(e) + ', которое меньше случайного числа ' + str(x) +
                         ', но больше случайного числа ' + str(y) + '. Осталось попыток: ' + str(c))
        return result_2, False
    elif x < e > y:
        result_3: str = ('Вы загадали число ' + str(e) + ', которое больше случайных чисел ' + str(x) +
                         ' и ' + str(y) + '. Осталось попыток: ' + str(c))
        return result_3, False
    elif x > e < y:
        result_4: str = ('Вы загадали число ' + str(e) + ', которое меньше случайных чисел ' + str(x) +
                         ' и ' + str(y) + '. Осталось попыток: ' + str(c))
        return result_4, False
    elif x < e == y:
        result_5: str = ('Вы загадали число ' + str(e) + ', которое больше случайного числа ' + str(x) +
                         ', и равно случайному числу ' + str(y) + '. Осталось попыток: ' + str(c))
        return result_5, False
    elif x == e < y:
        result_6: str = ('Вы загадали число ' + str(e) + ', которое равно случайному числу ' + str(x) +
                         ', и меньше случайного числа ' + str(y) + '. Осталось попыток: ' + str(c))
        return result_6, False
    elif x > e == y:
        result_7: str = ('Вы загадали число ' + str(e) + ', которое меньше случайного числа ' + str(x) +
                         ', и равно случайному числу ' + str(y) + '. Осталось попыток: ' + str(c))
        return result_7, False
    elif x == e > y:
        result_8: str = ('Вы загадали число ' + str(e) + ', которое равно случайному числу ' + str(x) +
                         ', и больше случайного числа ' + str(y) + '. Осталось попыток: ' + str(c))
        return result_8, False
    # if x == e == y:
    elif x == e == y:
        result_9: str = ('Оу, Удача! Поздравляю! Вы загадали число ' + str(e) +
                         ', которое равно случайным числам ' + str(x) +
                         ' и ' + str(y) + '! Количество попыток: ' + str(10 - c))
        return result_9, True


while True:
    # print('Испытайте удачу у нас!', 'Пока бесплатно!', 'У Вас есть 10 попыток угадать случайное число.',
    #       'Загадайте число от 1 до 5: ', sep='\n')
    a = random.randint(1, 5)
    b = random.randint(1, 5)
    c = int(input())
    count = 9
    start = time.time()
    for attempt in range(9):
        compare = compare_function(a, b, c, count)
        if compare[1]:
            print(compare[0])
            break
        else:
            count -= 1
            print(compare[0])
            a = random.randint(1, 5)
            b = random.randint(1, 5)
            c = int(input())

    else:
        print('К сожалению, Вам не удалось угадать случайное число :(',
              'Не везет в питоне - повезёт в любви!', sep='\n')
    stop = time.time()
    duration = stop - start
    print('Ушло времени на игру:', int(duration), 'секунд.')
    print('---', '---', sep='\n')
