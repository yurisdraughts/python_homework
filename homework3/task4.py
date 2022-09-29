# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

import f

def to_binary_str(num):
    return str(bin(num))[2:]

def to_binary_str2(num):
    res = str()
    i = 0
    while num >= 2 ** i:
        digit = int(num / 2 ** i) % 2
        res = str(digit) + res
        i += 1        
    return res

print(to_binary_str(45))
print(to_binary_str(3))
print(to_binary_str(2))
print()

print(to_binary_str2(45))
print(to_binary_str2(3))
print(to_binary_str2(2))
print()

print(to_binary_str(f.input_int()))
print()

print(to_binary_str2(f.input_int()))