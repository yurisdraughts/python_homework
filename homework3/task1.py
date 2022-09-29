# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import f

def sum_odd(list_num):
    sum = 0
    for i in range(1, len(list_num), 2):
        sum += list_num[i]
    return sum

print(sum_odd([2, 3, 5, 9, 3]))
print(sum_odd(f.input_list_int()))