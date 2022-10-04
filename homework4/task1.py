# Вычислить число c заданной точностью d

def input_precision(log = 'Введите число, равное 10⁻ⁿ, где 1 ≤ n ≤ 10: '):
    try:
        d = float(input(log))
    except:
        d = float(input_precision('Попробуйте ещё раз: '))
    if d not in [10 ** -i for i in range(1, 10)]:
        d = float(input_precision('Попробуйте ещё раз: '))
    else:
        for i in range(1, 10):
            if d == 10 ** -i:
                return i

def input_num(log = 'Введите число: '):
    try:
        return float(input(log))
    except:
        return float(input_num('Попробуйте ещё раз: '))

def round_down(num, precision):
    num *= 10 ** precision
    num = float(int(num))
    num /= 10 ** precision
    return num

num = input_num()
precision = input_precision()
print(round_down(num, precision))
