# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def input_num(log = 'Введите натуральное число: '):
    try:
        num = int(input(log))
        if num > 0: return num
        else: return int(input_num('Попробуйте ещё раз: '))
    except:
        return int(input_num('Попробуйте ещё раз: '))

def prime_mults(num):
    mults = [1]
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            mults.append(i)
    mults.append(num)
    for m in mults[2:]:
        previous = mults[1:mults.index(m)]
        for p in previous:
            if m % p == 0:
                mults.remove(m)
                break
    return mults

num = input_num()
print(f'Список простых множителей числа {num}:', prime_mults(num))