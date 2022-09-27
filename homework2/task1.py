# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

try:
    n = float(input('Введите вещественное число: '))
except:
    print('Это не вещественное число!')
    n = 0

n_sum = 0
for digit in str(n):
    try:
        n_sum += int(digit)
    except:
        n_sum += 0

print(f'Сумма цифр числа {n} равна {n_sum}')