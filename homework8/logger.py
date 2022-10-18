# символ разделитель
separator = ';;'

# добавляем одного работника в базу данных
def log_employee(employee_info):
    with open('employee.txt', 'a', encoding='utf=8') as file:
        file.write(f'{employee_info}\n')

# возвращаем список со всей базой данных
def get_employee_list():
    with open('employee.txt', 'r', encoding='utf=8') as file:
        employee_list = [line for line in file]
        return employee_list

# заменяем информацию в базе данных на основе нового списка
def log_new_data(data):
    with open('employee.txt', 'w', encoding='utf=8') as file:
        for line in data:
            file.write(f'{line}')