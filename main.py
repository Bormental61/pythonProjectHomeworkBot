import telebot
import random
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(mes):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton('гороскоп')
    item2 = telebot.types.KeyboardButton('наперстки')
    item3 = telebot.types.KeyboardButton('заново')
    markup.add(item1, item2, item3)

    bot.send_message(mes.chat.id, 'Привет, выбери чем займемся', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(mes):
    if mes.text == 'заново':
        welcome(mes)
    elif mes.text == 'гороскоп':
        markup = telebot.types.InlineKeyboardMarkup(row_width=3)
        item_1 = telebot.types.InlineKeyboardButton('Овен', callback_data='0')
        item_2 = telebot.types.InlineKeyboardButton('Телец', callback_data='1')
        item_3 = telebot.types.InlineKeyboardButton('Близнецы', callback_data='2')
        item_4 = telebot.types.InlineKeyboardButton('Рак', callback_data='3')
        item_5 = telebot.types.InlineKeyboardButton('Лев', callback_data='4')
        item_6 = telebot.types.InlineKeyboardButton('Дева', callback_data='5')
        item_7 = telebot.types.InlineKeyboardButton('Весы', callback_data='6')
        item_8 = telebot.types.InlineKeyboardButton('Скорпион', callback_data='7')
        item_9 = telebot.types.InlineKeyboardButton('Стрелец', callback_data='8')
        item_10 = telebot.types.InlineKeyboardButton('Козерог', callback_data='9')
        item_11 = telebot.types.InlineKeyboardButton('Водолей', callback_data='10')
        item_12 = telebot.types.InlineKeyboardButton('Рыбы', callback_data='11')
        markup.add(item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10, item_11, item_12)
        bot.send_message(mes.chat.id, 'Кто ты?', reply_markup=markup)
    elif mes.text == 'наперстки':
        msg = bot.send_message(mes.chat.id, 'Попробуй угадать правильный наперсток!\nВведи номер наперстка от 1 до 3')
        bot.register_next_step_handler(msg, guess_number_game)
    else:
        bot.send_message(mes.chat.id, 'Я не умею читать, если ты хочешь попробовать угадать число снова, запусти угадайку снова кнопкой')

stickers = ['CAACAgIAAxkBAAEHDa5jrXSvG3ppVxDFojwhaA9K_OvABQACKAEAAoe3Gh6YjT7bQrknhywE',
            'CAACAgIAAxkBAAEHDbJjrXaHzFU7AAFQDrBTLEMFlh42LTcAAikBAAKHtxoeZNnQhxum_OgsBA',
            'CAACAgIAAxkBAAEHDbRjrXaevuE_Wup5-32X-eQAAeY2hKkAAioBAAKHtxoeRVoYS2SqUl8sBA',
            'CAACAgIAAxkBAAEHDbZjrXaw4YIxt6F11bV12wZt0KbD3wACKwEAAoe3Gh5pcN58ami5tSwE',
            'CAACAgIAAxkBAAEHDbhjrXa8L5Xdle7eyuLRvvqgssz1EAACLAEAAoe3Gh5T8TgULcRsRywE',
            'CAACAgIAAxkBAAEHDbpjrXbNl2RHvvZqqzNGx72FCAZmEwACLQEAAoe3Gh4zlZeoAfpSBywE',
            'CAACAgIAAxkBAAEHDbxjrXbc7qP_OkqhZ44QECzY25EAAYMAAi4BAAKHtxoexbbiwbYcv4ksBA',
            'CAACAgIAAxkBAAEHDb5jrXbnbuo_kfDJtcuC2OOrcwaISAACLwEAAoe3Gh6pOol2Y_WlTSwE',
            'CAACAgIAAxkBAAEHDcJjrXcFa8d04_FchB-bSpLwS8wZ7AACMAEAAoe3Gh7pweUETjFFASwE',
            'CAACAgIAAxkBAAEHDcRjrXcgdyWFhoJ29YoK0BDYoFlcOQACMQEAAoe3Gh4ZkN_rnVFMXSwE',
            'CAACAgIAAxkBAAEHDcZjrXcsSYiLm78k-ptBEJWVlj1euQACMgEAAoe3Gh6tq7NE4ErScywE',
            'CAACAgIAAxkBAAEHDchjrXc6_V7sBVUQK2d8x-68dLKufwACMwEAAoe3Gh5TI3vaerFxcSwE']
def zod_about(call):
    dict = {}
    with open('zodiac.txt', 'r', encoding='utf-8') as file:
        for i in range(11):
            string = file.readline(). split(' ', 1)
            dict[string[0]] = string[1]
    return dict

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    zod_id = zod_about(call)
    bot.send_sticker(call.message.chat.id, stickers[int(call.data)])
    bot.send_message(call.message.chat.id, zod_id[call.data])
    return zod_id

def guess_number_game(user_num):
    goal_num = random.randint(1, 3)
    if int(user_num.text) == goal_num:
        bot.send_sticker(user_num.chat.id, 'CAACAgIAAxkBAAEHDehjrX6Ok1yanjzbUSfZC1LYLO9VLAACSgIAAladvQrJasZoYBh68CwE')
        bot.send_message(user_num.chat.id, f'УРА!!! Ты угадал! шарик был под наперстком {goal_num}')
    else:
        bot.send_message(user_num.chat.id, f'Не угадал, шарик под наперстком {goal_num}')












bot.polling(none_stop=True)

