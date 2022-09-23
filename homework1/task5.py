# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

try:
    print('Введите координаты 1-й точки (два числа, разделённые пробелом):')
    a_coord = list(map(float, input().split()))

    print('Введите координаты 2-й точки (два числа, разделённые пробелом):')
    b_coord = list(map(float, input().split()))

    distance = int((((a_coord[0] - b_coord[0]) ** 2 + (a_coord[1] - b_coord[1]) ** 2) ** 0.5) * 100) / 100

    print(f'A ({a_coord[0]}, {a_coord[1]}); B ({b_coord[0]}, {b_coord[1]}) -> {distance}')
except:
    print('Что-то пошло не так...')