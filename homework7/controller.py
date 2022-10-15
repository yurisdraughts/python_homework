# спрашиваем у пользователя, что он хочет, и вызываем соответствующие ф-ции

from view import new_line, input_name, print_number
from model import add_line, find_number

def main(log = ''):
    if log != '':
        ctrl_num = input(log)
    else:
        print('Если вы хотите ввести новую строку, введите 1.')
        print('Если вы хотите найти номер по имени, введите 2.')
        ctrl_num = input('>>> ')
    if ctrl_num == '1':
        line = new_line()
        add_line(line)
    elif ctrl_num == '2':
        name = input_name('Введите имя: ')
        print_number(name, find_number)
    else:
        main('Можно ввести только 1 или 2. Попробуйте ещё раз: ')