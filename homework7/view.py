# ввод нового фио и номера телефона в консоль

def input_name(log = 'Введите ФИО: '):
    name = input(log)
    return name

def input_number(log = 'Введите номер телефона (номер должен содержать только цифры и знак "+"): '):
    number = input(log)
    digits = '+0123456789'
    if not all(d in digits for d in number):
        number = input_number('Номер должен содержать только цифры и знак "+". Попробуйте ещё раз: ')
    return number

def new_line():
    name = input_name()
    number = input_number()
    return name + ' || ' + number

# вывод в консоль телефона по введенному имени

def print_number(name, find_number):
    number_list = find_number(name)
    for number in number_list:
        print(number)