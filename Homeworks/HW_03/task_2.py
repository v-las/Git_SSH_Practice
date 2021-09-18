# Задача №2
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "Конвертированная сумма в USD = int"
#                 "Конвертированная сумма в EUR = int"
#                 "Конвертированная сумма в CHF = int"
#                 "Конвертированная сумма в GBP = int"
#                 "Конвертированная сумма в CNY = int"
#     3. Валюту пользователя определите сами.

your_money = float(input())
convert_USD = your_money / 72.88
convert_EUR = your_money / 85.46
convert_CHF = your_money / 78.18
convert_GBP = your_money / 100.14
convert_CNY = your_money / 11.27
print('Ты ввёл ', your_money, 'RUB')
print('Конвертированная сумма в USD = ', round(convert_USD, 2))
print('Конвертированная сумма в EUR = ', round(convert_EUR, 2))
print('Конвертированная сумма в CHF = ', round(convert_CHF, 2))
print('Конвертированная сумма в GBP = ', round(convert_GBP, 2))
print('Конвертированная сумма в CNY = ', round(convert_CNY, 2))
