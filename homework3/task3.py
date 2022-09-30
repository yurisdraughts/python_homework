# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import f

def list_fractions(list_num):
    fraction_list = []
    for num in list_num:
        try:
            i = str(num).index('.')
            fraction = float(str(num)[i:])
            fraction_list.append(fraction)
        except:
            pass
    return fraction_list

def subtract_max_min_fractions(list_num):
    fraction_list = list_fractions(list_num)
    if len(fraction_list) == 1:
        return fraction_list[0]
    elif len(fraction_list) == 0:
        return 0
    else:
        if max(fraction_list) - min(fraction_list) != 0.0:
            return max(fraction_list) - min(fraction_list)
        else:
            return 0

print(subtract_max_min_fractions([1.1, 1.2, 3.1, 5, 10.01]))
print(subtract_max_min_fractions(f.input_list_num()))