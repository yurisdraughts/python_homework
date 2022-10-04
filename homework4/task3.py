# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def input_list_num(log = 'Введите числа, разделённые пробелами: '):
    try:
        list_num = list(map(float, input(log).split()))
    except:
        list_num = input_list_num('Попробуйте ещё раз: ')
    return list_num

def remove_duplicates(lst):
    new_lst = [i for i in lst if lst.count(i) == 1]
    for i in range(len(new_lst)):
        if new_lst[i] % 1 == 0:
            new_lst[i] = int(new_lst[i])
    return new_lst

lst = input_list_num()
print(remove_duplicates(lst))