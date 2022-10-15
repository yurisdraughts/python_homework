# имя файла

file_name = 'phone_book.txt'

# добавляем строку с именем и номером в файл

def add_line(line):
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{line}\n')

# находим номер(а) в файле по имени

def find_number(name):
    number_list = []
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if name in line:
                number_list.append(line[line.find('||') + 3 : -1])
    return number_list