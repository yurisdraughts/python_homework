import telebot
from t import token
from random import randint

bot = telebot.TeleBot(token, parse_mode = None)

# На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.

is_game_on = False
candies = 2021

def bots_move(message):
    global candies, is_game_on
    n = randint(1, 28)
    if n < candies:
        candies -= n
        bot.send_message(message.chat.id, f'Бот забрал {n} конфет. Осталось {candies} конфет.')
    else:
        is_game_on = False
        bot.send_message(message.chat.id, 'Игра окончена. Бот выиграл!')

@bot.message_handler(commands = ['start'])
def start_game(message):
    global is_game_on
    if not is_game_on:
        global candies
        is_game_on = True
        is_players_turn = bool(randint(0, 1))
        bot.send_message(message.chat.id, f'Сначало было {candies} конфет. {"Игрок" if is_players_turn else "Бот"} делает первый ход')
        bot.send_message(message.chat.id,  'Введите число, не большее 28.') if is_players_turn else bots_move(message)
        if is_game_on: is_players_turn = not is_players_turn

@bot.message_handler(func = lambda _: is_game_on)
def players_move(message):
    global candies, is_game_on
    try:
        n = int(message.text)
        if n > 28:
            bot.send_message(message.chat.id, 'Число должно быть не больше 28. Попытайтесь ещё раз.')
        else:
            if n < candies:
                candies -= n
                bot.send_message(message.chat.id, f'Осталось {candies} конфет.')
                bots_move(message)
                if is_game_on: bot.send_message(message.chat.id,  'Введите число, не большее 28.')
            else:
                candies = 0
                is_game_on = False
                bot.send_message(message.chat.id, 'Игра окончена. Вы выиграли!')
    except:
        bot.send_message(message.chat.id, 'Введено не целое число или не число. Попытайтесь ещё раз.')

bot.infinity_polling()