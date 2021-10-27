# Задача №3
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "конвертированная сумма в USD = int"
#                 "конвертированная сумма в EUR = int"
#                 "конвертированная сумма в CHF = int"
#                 "конвертированная сумма в GBP = int"
#                 "конвертированная сумма в CNY = int"
#
#     3. Скипт должен выдать сообщение
#                 "Введите положительное число." Если число меньше 0.
#                 "Вы ввели не число. Введите число." Если введены буквы.
#                 "Вы ввели пустое поле. Введите число." Если введено пустое значение.
#     4. Валюту пользователя определите сами.
# try:


def main():
    your_money = input_func()
    convert_usd = your_money / 72.88
    convert_eur = your_money / 85.46
    convert_chf = your_money / 78.18
    convert_gbp = your_money / 100.14
    convert_cny = your_money / 11.27
    print('Ты ввёл ', your_money, 'RUB')
    # print('Конвертированная сумма в USD = ', round(convert_usd, 2))
    print('Конвертированная сумма в USD = ', round(convert_usd, 2))
    print('Конвертированная сумма в EUR = ', round(convert_eur, 2))
    print('Конвертированная сумма в CHF = ', round(convert_chf, 2))
    print('Конвертированная сумма в GBP = ', round(convert_gbp, 2))
    print('Конвертированная сумма в CNY = ', round(convert_cny, 2))


def input_func():
    your_money = int(input('Введите количество RUB: '))
    if your_money <= 0:
        print('Введите положительное число.')
        while True:
            your_money = input('Введите количество RUB: ').strip()
            if your_money.isdigit():
                your_money = int(your_money)
                break
            else:
                if not your_money:
                    print('Вы ввели пустое поле. Введите число.')
                else:
                    print('Вы ввели не число. Введите число.')
    return your_money
