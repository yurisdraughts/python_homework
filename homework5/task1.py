# Создайте программу для игры с конфетами человек против человека.

import random as r

def input_candy_num(log = 'Введите N, N <= 28: '):
    try:
        n = int(input(log))
        if n > 28:
            return input_candy_num('N должно быть не больше 28. Попытайтесь ещё раз: ')
        else:
            return n
    except:
        return input_candy_num('Введено не целое число. Попытайтесь ещё раз: ')

def play_candy():
    move_num = 0
    candy_num = 2021
    print('Сначала было', candy_num, 'конфет.\n')
    while candy_num > 0:
        print(f'Игрок {move_num % 2 + 1} берёт N конфет.')
        n = input_candy_num()
        candy_num -= n
        print('Осталось', candy_num, 'конфет.\n')
        move_num += 1

def play_candy_bot():
    move_num = 0
    candy_num = 2021
    print('Сначала было', candy_num, 'конфет.\n')
    while candy_num > 0:
        if move_num % 2 == 0:
            print('Игрок берёт N конфет.')
            n = input_candy_num()
        else:
            n = r.randint(1, 28)
            print(f'Бот берёт {n} конфет.')
        candy_num -= n
        print('Осталось', candy_num, 'конфет.\n')
        move_num += 1

play_candy_bot()