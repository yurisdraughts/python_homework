# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

try:
    n = int(input('Введите целое положительное число: '))
    if n <= 0:
        print('Введённое значение не является целым положительным числом!')
        n = 6
except:
    print('Введённое значение не является целым положительным числом!')
    n = 6

numbers = []
for i in range(1, n + 1):
    numbers.append((1 + 1/i) ** i)

numbers_sum = sum(numbers)

result = f'Для n = {n}: [ '
for number in numbers:
    result += str(number)
    if number != numbers[-1]:
        result += ', '
result += ' ], sum = ' + str(numbers_sum)

print(result)