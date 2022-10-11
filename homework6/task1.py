# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from f import input_list_num as inp

lst = inp()
sum_odds = lambda lst: sum([lst[i] for i in range(len(lst)) if i % 2 == 1])

print(sum_odds(lst))