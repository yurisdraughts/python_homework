# Реализуйте алгоритм перемешивания списка.

import random

list_original = ['apple', 'banana', '', '4', '8', [15, 16], {23: 42}, False]
list_shuffled = list_original.copy()
random.shuffle(list_shuffled)

print(f'{list_original} -> {list_shuffled}')