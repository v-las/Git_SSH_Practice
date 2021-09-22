def main():
    input_money = get_money()
    usd_money = exchange(input_money)
    print('usd_money =', usd_money)


def get_money():
    input_data = input('Enter UAH amount: ')
    return input_data


def exchange(money):
    int_money = int(money) / 27
    return int_money


main()