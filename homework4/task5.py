# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def get_coefs(equation):
    coefs = []
    parts = equation.split(' + ')
    for i in parts:
        try:
            coefs.append(i[:i.index('*')])
        except:
            coefs.append(i)
    return coefs

equation1 = open('task5_1.txt', 'r').readline()
equation2 = open('task5_2.txt', 'r').readline()

coefs1 = get_coefs(equation1)
coefs2 = get_coefs(equation2)

coefs = [f'{int(coefs1[i]) + int(coefs2[i])}' for i in range(3)]

data = open('task5_res.txt', 'w')
data.write(f'{coefs[0]}*x^2 + {coefs[1]}*x + {coefs[2]}')