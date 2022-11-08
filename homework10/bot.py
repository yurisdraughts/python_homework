import telebot
from pytube import YouTube
import pytube.exceptions
from t import token

bot = telebot.TeleBot(token, parse_mode = None)

url = ''
res = ''
state = ['inactive', 'awaits_url', 'awaits_res']
current_state = 0
def next_state(step=1):
    global current_state
    current_state = (current_state + step) % len(state)

# Начнём
@bot.message_handler(func = lambda _: state[current_state] == 'inactive', commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Введите адрес видео на YouTube.')
    next_state()

# Выключим бота до окончания программы
@bot.message_handler(commands = ['end'])
def end(message):
    global url, res, current_state
    if current_state != 0:
        url, res, current_state = '', '', 0
        bot.send_message(message.chat.id, 'Работа бота завершена. Вы можете попробовать ещё раз с помощью команды /start')

# Получим все доступные разрешения...
def get_all_res(url):
    return [res for res in ['720p', '480p', '360p', '240p', '144p']\
        if YouTube(url).streams.get_by_resolution(res) != None]

# ...если их нет -> просим ввести новый адрес;
# если есть только одно -> сразу скачиваем видео и обнуляем current_state;
# если их несколько -> переходим к выбору разрешения.
def check_res(available_res, message):
    global url, res, current_state
    if len(available_res) == 0:
        url = ''
        bot.send_message(message.chat.id, 'Невозможно скачать видео, введите другой адрес.')
    elif len(available_res) == 1:
        res = available_res[0]
        bot.send_message(message.chat.id, f'Единственное доступное разрешение: {res}. Пожалуйста, подождите, когда скачается видео.')
        download(message)
        current_state = 0
    else:
        question = 'Выберите качество видео: '
        for i, res in enumerate(available_res):
            question += res + ', ' if i < len(available_res) - 1 else res + '.'
        bot.send_message(message.chat.id, question)
        next_state()

# Обработаем адрес, используя ф-ции выше
@bot.message_handler(func = lambda _: state[current_state] == 'awaits_url')
def process_url(message):
    global url
    try:
        YouTube(message.text)
        url = message.text
        bot.send_message(message.chat.id, 'Проверяем доступные разрешения. Пожалуйста, подождите.')
        check_res(get_all_res(url), message)
    except pytube.exceptions.RegexMatchError:
        bot.send_message(message.chat.id, 'Неверный URL, попробуйте ещё раз!')

# Выбираем разрешение
@bot.message_handler(func = lambda _: state[current_state] == 'awaits_res')
def process_res(message):
    global res, current_state
    bot.send_message(message.chat.id, 'Проверяем введённое разрешение. Пожалуйста, подождите.')
    available_res = get_all_res(url)
    chosen_res = message.text
    if chosen_res in available_res:
        bot.send_message(message.chat.id, 'Скачиваем видео!')
        res = chosen_res
        download(message)
        current_state = 0
    elif chosen_res + 'p' in available_res:
        bot.send_message(message.chat.id, 'Скачиваем видео!')
        res = chosen_res + 'p'
        download(message)
        current_state = 0
    else:
        bot.send_message(message.chat.id, 'Неверное разрешение. Попробуйте ещё раз.')

# Скачиваем и пересылаем видео
def download(message):
    filename = YouTube(url).streams.get_by_resolution(res).default_filename
    YouTube(url).streams.get_by_resolution(res).download(output_path='./download', filename=filename)
    video = open(f'./download/{filename}', 'rb')
    bot.send_video(message.chat.id, video)
    bot.send_message(message.chat.id, 'Готово! Вы можете скачать ещё одно видео с помощью команды /start')

bot.infinity_polling()