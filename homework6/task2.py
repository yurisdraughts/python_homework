# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

from f import input_num as inp
from math import factorial as fact

n = inp()
list_factorials = lambda n: [fact(i) for i in range(1, n + 1)]

print(list_factorials(n))