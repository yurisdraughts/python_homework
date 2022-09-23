#Напишите программу для проверки истинности
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for i in range(8):
    values = []

    for number in [i % 2, int(i / 2) % 2, int(i / 4) % 2]:
        if number == 0:
            values.append(False)
        else:
            values.append(True)

    print(f'not ({values[0]} or {values[1]} or {values[2]}) == (not {values[0]} and not {values[1]} and not {values[2]})')
    print(f'{not (values[0] or values[1] or values[2]) == (not values[0] and not values[1] and not values[2])}\n')