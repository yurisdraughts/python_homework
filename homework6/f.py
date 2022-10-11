def input_list_num(log = 'Введите целые числа, разделённые пробелами: '):
    try:
        list_num = list(map(int, input(log).split()))
    except:
        list_num = input_list_num('Введено не число или не целое число. Попробуйте ещё раз: ')
    return list_num

def input_two_num(log = 'Введите 2 целых числа, разделённые пробелами: '):
    try:
        two_num = list(map(int, input(log).split()))
        if len(two_num) != 2:
            two_num = input_two_num('Должно быть введено два числа. Попробуйте ещё раз: ')
    except:
        two_num = input_two_num('Введено не число или не целое число. Попробуйте ещё раз: ')
    return two_num

def input_num(log = 'Введите целое положительное число: '):
    try:
        num = int(input(log))
        if num < 0:
            num = input_num('Должно быть введено положительное число. Попробуйте ещё раз: ')
    except:
        num = input_num('Введено не число или не целое число. Попробуйте ещё раз: ')
    return num