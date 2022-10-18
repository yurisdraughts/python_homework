from logger import separator

# создаем строку с информацией о работнике для базы данных
def new_employee(input_employee_info):
    return separator.join(input_employee_info())

# ищем работника в списке
def find_employees(employee_list):
    data = input('Введите данные для поиска: ')
    employees = list(filter(lambda employee: data in employee, employee_list))
    return employees

# редактируем информацию о работнике
def edit_employee_info(employee, field_index):
    employee = employee.split(separator)
    employee[field_index] = input('Введите новую информацию: ')
    employee = separator.join(employee)
    return employee