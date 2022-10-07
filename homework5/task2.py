# Создайте программу для игры в "Крестики-нолики".

board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def print_board(board):
    print(' '.join(board[:3]))
    print(' '.join(board[3:6]))
    print(' '.join(board[6:]))

def get_line(i):
    if 0 <= i <= 2:
        return [3*i, 3*i + 1, 3*i + 2]
    elif 3 <= i <= 5:
        i -= 3
        return [i, i + 3, i + 6]
    elif i == 6:
        return [0, 4, 8]
    elif i == 7:
        return [2, 4, 6]

def is_game_over(board):
    for i in range(8):
        line = get_line(i)
        if board[line[0]] == board[line[1]] == board[line[2]]:
            return board[line[0]]
    for square in board:
        if square != 'X' and square != '0':
            return False
    return True

def input_square(board, log = 'Введите номер клетки: '):
    num = input(log)
    if num not in board:
        num = input_square(board, 'Это не номер клетки, или эта клетка занята. Попробуйте ещё раз: ')
    return num

def make_move_player(board):
    num = input_square(board)
    board[board.index(num)] = 'X'

def make_move_program(board):
    available_squares = [i for i in range(len(board)) if board[i] != 'X' and board[i] != '0']
    for i in range(8):
        line_i = get_line(i)
        line = [board[i] for i in line_i]
        for square in available_squares:
            if square in line_i and line.count('X') == 2:
                board[square] = '0'
                print(f'Программа сделала ход (клетка {square + 1}):')
                return
    board[available_squares[0]] = '0'
    print(f'Программа сделала ход (клетка {available_squares[0] + 1}):')

def play(board):
    while not is_game_over(board):
        print_board(board)
        make_move_player(board)
        if not is_game_over(board):
            print_board(board)
            make_move_program(board)
        else: break
    print_board(board)
    result = is_game_over(board)
    if result == '0':
        print('Вы проиграли.')
    elif result == 'X':
        print('Вы выиграли!')
    else:
        print('Ничья.')

play(board)