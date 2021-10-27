# b, q, n = int(input('1 число последовательности ')),\
#           int(input('знаменатель прогрессии ')), int(input("n-ый член прогрессии "))
# number = b * q ** (n - 1)
# print(number)

# a = int(input())
# a = a // 100
# print(a)

# n = int(input())
# k = int(input())
# print(k // n)
# print(k % n)

# print((int(input()) + 1) // 2)

# t = int(input())
# print(t, 'мин - это', t // 60, 'час', t % 60, 'минут.')

# n = int(input())
# print(n)
# print('Сумма цифр =', (n // 100) + ((n % 100) // 10) + (n % 10))
# print('Произведение цифр =', (n // 100) * ((n % 100) // 10) * (n % 10))

# n = int(input())
# a = n // 100
# b = (n % 100) // 10
# c = n % 10
# print(a, b, c, sep='')
# print(a, c, b, sep='')
# print(b, a, c, sep='')
# print(b, c, a, sep='')
# print(c, a, b, sep='')
# print(c, b, a, sep='')

# n = int(input())
# print('Цифра в позиции тысяч равна', n // 1000)
# print('Цифра в позиции сотен равна', (n % 1000) // 100)
# print('Цифра в позиции десятков равна', (n % 100) // 10)
# print('Цифра в позиции единиц равна', n % 10)

"""
Сохраню на потом
l, _range = list(input()), ['тысяч', 'сотен', 'десятков', 'единиц']
[print('Число ' + _range[i] + ' равно ' + l[i]) for i in range(4)]
print(*(f'Цифра в позиции {a[0]} равна {a[1]}' for a in zip(('тысяч', 'сотен', 'десятков', 'единиц'), input())), sep='\n')
"""

# todo 2.5 Номер купе
# while True:
#     number = n = int(input())
#     coupe_count = c = 9
#     seat_count = s = 4
#     print(n // s + 1)

# s = input()
# print(input(), input(), input(), sep=s)

# n = int(input())
# print(n, n + 1, sep='\n')
# n = n + 1
# print(n + 1)

# print(int(input()) + int(input()) + int(input()))

# r = int(input())
# print('Объем =', r ** 3)
# print('Площадь полной поверхности =', 6 * r ** 2)

a, b = int(input()), int(input())
print(3 * (a + b) ** 3 + 275 * b ** 2 - 127 * a - 41)
