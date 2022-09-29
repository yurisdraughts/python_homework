# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import f

def mult_pairs(list_num):
    len_result = int(len(list_num) / 2)
    if len(list_num) % 2 == 1: len_result += 1

    result = [list_num[i] * list_num[-(i + 1)] for i in range(0, len_result)]
    return result

print(mult_pairs([2, 3, 4, 5, 6]))
print(mult_pairs([2, 3, 5, 6]))
print(mult_pairs(f.input_list_int()))