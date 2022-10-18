# Создать иформационную систему позволяющую работать с
# сотрудниками некой компании \ студентами вуза \ учениками школы.

import ui
import model as m
import logger as l

ui.print_modes()
mode = input()

if mode == '1':
    employee = m.new_employee(ui.input_employee_info)
    l.log_employee(employee)
elif mode == '2':
    for employee in m.find_employees(l.get_employee_list()):
        ui.print_employee(employee[:-1]) # удаляем срезом '\n' в конце строки
elif mode == '3':
    for employee in l.get_employee_list():
        ui.print_employee(employee[:-1])
elif mode == '4':
    all_employees = l.get_employee_list()
    found_employees = m.find_employees(all_employees)

    employee = ui.choose_employee(found_employees)
    employee_index = all_employees.index(employee)

    field_to_edit = ui.get_field_index()
    all_employees[employee_index] = m.edit_employee_info(employee, field_to_edit)

    l.log_new_data(all_employees)
else:
    print('Введено неверное значение!')