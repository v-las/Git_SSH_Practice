import random
import time


def check_input(input_number):
    try:
        input_number = int(input_number)
    except ValueError:
        return "not num", False
    if 0 < input_number:
        return "less 0", False
    elif input_number > 6:
        return "more 6", False
    else:
        return input_number, True


def compare_function(x, y, e, count):
    """
    Функция сравнивает введенное значение 'e' с двумя случайными - 'x' и y'.
    Значение 'count' передаётся для подсчёта и вывода.
    На выходе ожидается строка с результатом сравнения для вывода,
    прерывание при 'x=e=y' и продолжение ввода при других значениях
    """
    if x < e < y:
        result = ('Вы загадали число {0}, которое больше случайного числа {1}, но меньше случайного числа {2}. '
                  'Осталось попыток: {3}'.format(str(e), str(x), str(y), str(count)))
        return result, False
    elif x > e > y:
        result = ('Вы загадали число {0}, которое меньше случайного числа {1}, но больше случайного числа {2}. '
                  'Осталось попыток: {3}'.format(str(e), str(x), str(y), str(count)))
        return result, False
    elif x < e > y:
        result: str = ('Вы загадали число {0}, которое больше случайных чисел {1} и {2}. '
                       'Осталось попыток: {3}'.format(str(e), str(x), str(y), str(count)))
        return result, False
    elif x > e < y:
        result: str = ('Вы загадали число {0}, которое меньше случайных чисел {1} и {2}. '
                       'Осталось попыток: {3}'.format(str(e), str(x), str(y), str(count)))
        return result, False
    elif x < e == y:
        result: str = ('Вы загадали число {0}, которое больше случайного числа {1}, и равно случайному числу {2}. '
                       'Осталось попыток: {3}'.format(str(e), str(x), str(y), str(count)))
        return result, False
    elif x == e < y:
        result: str = ('Вы загадали число {0}, которое равно случайному числу {1}, и меньше случайного числа {2}. '
                       'Осталось попыток: {3}'.format(str(e), str(x), str(y), str(count)))
        return result, False
    elif x > e == y:
        result: str = ('Вы загадали число {0}, которое меньше случайного числа {1}, и равно случайному числу {2}. '
                       'Осталось попыток: {3}'.format(str(e), str(x), str(y), str(count)))
        return result, False
    elif x == e > y:
        result: str = ('Вы загадали число {0}, которое равно случайному числу {1}, и больше случайного числа {2}. '
                       'Осталось попыток: {3}'.format(str(e), str(x), str(y), str(count)))
        return result, False
    elif x == e == y:
        result: str = ('Оу, Удача! Поздравляю! Вы загадали число {0}, которое равно случайным числам {1} и {2}! '
                       'Количество попыток: {3}'.format(str(e), str(x), str(y), str(10 - count)))
        return result, True


while True:
    print('Испытайте удачу у нас!', 'Пока бесплатно!', 'У Вас есть 10 попыток угадать случайное число.',
          'Загадайте число от 1 до 5: ', sep='\n')
    start = time.time()
    for i in range(9):
        a, b = random.randint(1, 5), random.randint(1, 5)
        c = check_input(input())
        if c[1]:
            compare_function(a, b, c, 9 - i)
        else:
            c = check_input(input())
        if compare[1]:
            print(compare[0])
            break
        else:
            print(compare[0])
    else:
        print('К сожалению, Вам не удалось угадать случайное число :(',
              'Не везет в питоне - повезёт в любви!', sep='\n')
    stop = time.time()
    print('Ушло времени на игру:', int(stop - start), 'секунд.')
    print('---', '---', sep='\n')
