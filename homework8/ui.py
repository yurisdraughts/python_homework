from logger import separator

# выводим на экран способы работы с базой данных
def print_modes():
    print('Выберите режим работы с данными сотрудников: ')
    print('1. Внести данные нового сотрудника;')
    print('2. Поиск данных сотрудника по базе;')
    print('3. Вывести всех сотрудников на экран;')
    print('4. Внести изменения.')

# вводим информацию о работнике
def input_employee_info():
    employee = []
    employee.append(input('Введите ID: '))
    employee.append(input('Введите имя: '))
    employee.append(input('Введите фамилию: '))
    employee.append(input('Введите номер телефона: '))
    employee.append(input('Введите должность: '))
    employee.append(input('Введите заработную плату: '))
    return employee

# выводим строку с информацией о работнике на консоль
def print_employee(employee):
    data = employee.split(separator)
    print(' '.join(data))

# выбираем одного работника из списка
def choose_employee(employees):
    if len(employees) > 1:
        for index, employee in enumerate(employees):
            print(f'index = {index}:')
            print_employee(employee[:-1])

        def loop(employees, log = 'Введите индекс работника, информацию о котором вы хотите отредактировать: '):
            index = input(log)
            if index in list(map(str, range(len(employees)))):
                return employees[int(index)]
            else:
                return loop(employees, 'Попробуйте ещё раз')

        return loop(employees)
    else:
        employee = employees[0]
        print_employee(employee[:-1])
        return employee

# выбираем поле для редактирования
field_number = 6

def get_field_index():
    print('Если вы хотите отредактировать ..., введите ...:')
    print('ID -> 1')
    print('Имя -> 2')
    print('Фамилию -> 3')
    print('Номер телефона -> 4')
    print('Должность -> 5')
    print('Заработную плату -> 6')
    return input_field_number() - 1

def input_field_number(log = ''):
    try:
        number = int(input())
    except:
        number = input_field_number('Попробуйте ещё раз: ')
    if number > field_number:
        number = input_field_number('Попробуйте ещё раз: ')
    return number