def input_list_int(log = 'Введите целые числа, разделённые пробелами: '):
    try:
        list_num = list(map(int, input(log).split()))
    except:
        list_num = input_list_int('Введено не число или не целое число. Попробуйте ещё раз: ')
    return list_num

def input_list_num(log = 'Введите вещественные числа, разделённые пробелами: '):
    try:
        list_num = list(map(float, input(log).split()))

        for i in range(len(list_num)):
            if list_num[i] == float(int(list_num[i])):
                list_num[i] = int(list_num[i]) # заменяем тип целых чисел с float на int
    except:
        list_num = input_list_num('Введено не число, или формат неверен. Попробуйте ещё раз: ')
    return list_num

def input_int(log = 'Введите целое число: '):
    try:
        return int(input(log))
    except:
        return int(input('Введено не число или не целое число. Попробуйте ещё раз: '))