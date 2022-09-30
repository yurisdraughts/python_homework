def input_list_int(log = 'Введите целые числа, разделённые пробелами: '):
    try:
        list_num = list(map(int, input(log).split()))
    except:
        list_num = input_list_int('Введено не число или не целое число. Попробуйте ещё раз: ')
    return list_num

def str_to_num(string):
    if float(string) % 1 != 0:
        return float(string)
    else:
        return int(string)

def input_list_num(log = 'Введите вещественные числа, разделённые пробелами: '):
    try:
        list_num = list(map(str_to_num, input(log).split()))
    except:
        list_num = input_list_num('Введено не число, или формат неверен. Попробуйте ещё раз: ')
    return list_num

def input_int(log = 'Введите целое число: '):
    try:
        return int(input(log))
    except:
        return int(input('Введено не число или не целое число. Попробуйте ещё раз: '))