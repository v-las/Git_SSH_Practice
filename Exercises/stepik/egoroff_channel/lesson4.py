# поменять местами две переменные, используя знаки + и -

a = int(input('a = '))
b = int(input('b = '))
print('a = ', a)
print('b = ', b)
a = a - b
b = b + a
a = b - a
print('a = ', a)
print('b = ', b)
