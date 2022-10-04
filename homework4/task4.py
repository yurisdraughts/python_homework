#Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.

import random

def input_data(log = 'Задайте натуральную степень многочлена k: '):
    try:
        k = int(input(log))
    except:
        k = input_data('Введено не натрульное число, или не число. Попробуйте ещё раз: ')
    equation = str()
    for i in range(k, -1, -1):
        equation += str(random.randint(0,101))
        if i > 0:
            equation += '*x'
            if i > 1: equation += f'^{i}'
        if i != 0: equation += ' + '
    equation += ' = 0'
    return equation

equation = input_data()
print(equation)
file = open('task4.txt', 'w')
file.write(equation)