import random
import time


def compare_function(x, y, e, c):
    """
    Функция сравнивает между собой значения 'x', 'y', 'e',
    и забирает 'c' для счёта и добавления в результат.
    Строка результата генерируется из списка my_order.
    :param x: случайное значение
    :param y: случайное значение
    :param e: введенное значение
    :param c: номер итерации цикла
    :return: результат сравнения для вывода и bool для верной работы внешнего цикла
    """
    my_order = [str(e), str(x), str(y), str(c), 'Вы загадали число ', ', которое ', 'больше ', 'меньше ', 'равно ',
                ' и ', ', но ', 'случайного числа ', 'случайному числу ', 'случайных чисел ', '. Осталось попыток: ']
    # for i in enumerate(my_order):  # Вывод в консоль значений списка my_order с порядковой нумерацией
    #     print(i)
# todo не осталось попыток
# if c == 9:
#     my_order[14] = ['У Вас Закончились']
    if x < e < y:
        result = ('{4}{0}{5}{6}{11}{1}{10}{7}{11}{2}{14}{3}'.format(*my_order))
        return result, False
    elif x > e > y:
        result = ('{4}{0}{5}{7}{11}{1}{10}{6}{11}{2}{14}{3}'.format(*my_order))
        return result, False
    elif x < e > y:
        result = ('{4}{0}{5}{6}{13}{1}{9}{2}{14}{3}'.format(*my_order))
        return result, False
    elif x > e < y:
        result = ('{4}{0}{5}{7}{13}{1}{9}{2}{14}{3}'.format(*my_order))
        return result, False
    elif x < e == y:
        result = ('{4}{0}{5}{6}{11}{1}{9}{8}{12}{2}{14}{3}'.format(*my_order))
        return result, False
    elif x == e < y:
        result = ('{4}{0}{5}{8}{12}{1}{9}{7}{11}{2}{14}{3}'.format(*my_order))
        return result, False
    elif x > e == y:
        result = ('{4}{0}{5}{7}{11}{1}{9}{8}{12}{2}{14}{3}'.format(*my_order))
        return result, False
    elif x == e > y:
        result = ('{4}{0}{5}{8}{12}{1}{9}{6}{11}{2}{14}{3}'.format(*my_order))
        return result, False
    elif x == e == y:
        my_order[3] = str(10 - c)
        result = ('Оу, Удача! Поздравляю! {4}{0}{5}{8}случайным числам {1}{9}{2}! '
                  'Количество попыток: {3}'.format(*my_order))
        return result, True


while True:
    print('Игра началась!', 'Испытайте удачу у нас!', 'Пока бесплатно!',
          'У Вас есть 10 попыток угадать случайное число.',
          'Загадайте число от 1 до 5: ', sep='\n')
    start = time.time()
    for i in range(10):
        a, b = random.randint(1, 5), random.randint(1, 5)
        c = int(input())
        compare = compare_function(a, b, c, 9 - i)
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
