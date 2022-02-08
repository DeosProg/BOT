import time
import telebot
import os
import traceback
from telebot import types
import datetime
from datetime import datetime, date
from concurrent.futures import ThreadPoolExecutor
import threading

# мои зависимости
from notifications import check_settings
import timetable_processing
import config
import texts
import homework0
import homework1
from homework_processing import processing

# from cal import cal

texxt = '''

██████╗░░█████╗░████████╗  ░██████╗████████╗░█████╗░██████╗░████████╗███████╗██████╗░
██╔══██╗██╔══██╗╚══██╔══╝  ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██████╦╝██║░░██║░░░██║░░░  ╚█████╗░░░░██║░░░███████║██████╔╝░░░██║░░░█████╗░░██║░░██║
██╔══██╗██║░░██║░░░██║░░░  ░╚═══██╗░░░██║░░░██╔══██║██╔══██╗░░░██║░░░██╔══╝░░██║░░██║
██████╦╝╚█████╔╝░░░██║░░░  ██████╔╝░░░██║░░░██║░░██║██║░░██║░░░██║░░░███████╗██████╔╝
╚═════╝░░╚════╝░░░░╚═╝░░░  ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░
'''

codeA = config.codeA
codeB = config.codeB

bot = telebot.TeleBot(config.token)

months = ['', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября',
          'декабря']
lessons = [34200,40800,47400,55500,62100]
path = os.getcwd()


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, texts.welcome_text)


@bot.message_handler(commands=['update'])
def update(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(text="Главная страница💥")
    keyboard.add(button)
    bot.send_message(message.chat.id, texts.update, reply_markup=keyboard)
    print('\033[2;35;40m ' + str(message.text) + ' ' + message.from_user.first_name)


@bot.message_handler(content_types=["text"])
def text_handler(message):
    # ИНИЦИАЛИЗАЦИЯ КНОПОК, КЛАВИАТУР--------------------------------------------
    c_date = date.today()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)  # основная
    keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard=True)  # экран приветствия
    keyboard3 = types.ReplyKeyboardMarkup(resize_keyboard=True)  # главный экран
    markup_n = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_t = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_s = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup2 = types.InlineKeyboardMarkup(row_width=2)
    markup3 = types.InlineKeyboardMarkup(row_width=7)

    button_5 = types.KeyboardButton(text="Главная страница💥")
    button_6 = types.KeyboardButton(text="Полезные ссылки🔗")
    button_7 = types.KeyboardButton(text="Домашнее задание📚")
    button_8 = types.KeyboardButton(text="Расписание📅")
    button_9 = types.KeyboardButton(text='Настройки уведомлений⚙')
    button_10 = types.KeyboardButton(text='Учеба🎓')

    item_n1 = types.InlineKeyboardButton('Изменить время уведомления', callback_data='n1')
    item_n2 = types.InlineKeyboardButton('Включить/выключить уведомления', callback_data='n2')

    item = types.InlineKeyboardButton('Текущая', callback_data='0')
    item2 = types.InlineKeyboardButton('Следующая', callback_data='1')

    item3 = types.InlineKeyboardButton('Сегодня', callback_data='today')
    item4 = types.InlineKeyboardButton('Завтра', callback_data='tomorrow')
    item34 = types.InlineKeyboardButton('На неделю', callback_data='default')
    item43 = types.InlineKeyboardButton('На следующую неделю', callback_data='next')

    item5 = types.InlineKeyboardButton('Понедельник', callback_data='01')
    item6 = types.InlineKeyboardButton('Вторник', callback_data='02')
    item7 = types.InlineKeyboardButton('Среда', callback_data='03')
    item8 = types.InlineKeyboardButton('Четверг', callback_data='04')
    item9 = types.InlineKeyboardButton('Пятница', callback_data='05')
    item10 = types.InlineKeyboardButton('Суббота', callback_data='06')
    item11 = types.InlineKeyboardButton('Понедельник', callback_data='11')
    item12 = types.InlineKeyboardButton('Вторник', callback_data='12')
    item13 = types.InlineKeyboardButton('Среда', callback_data='13')
    item14 = types.InlineKeyboardButton('Четверг', callback_data='14')
    item15 = types.InlineKeyboardButton('Пятница', callback_data='15')
    item16 = types.InlineKeyboardButton('Суббота', callback_data='16')
    item_t5 = types.KeyboardButton('5 мин')
    item_t10 = types.KeyboardButton('10 мин')
    item_t15 = types.KeyboardButton('15 мин')
    item_t1 = types.KeyboardButton('1 мин')


    item_n1 = types.KeyboardButton('Изменить время уведомления')
    item_n2 = types.KeyboardButton('Включить/выключить уведомления')

    item_s1 = types.KeyboardButton('Вкл',)
    item_s0 = types.KeyboardButton('Выкл',)

    keyboard.add(button_8)
    keyboard.add(button_7)
    keyboard.add(button_6)
    keyboard.add(button_5)

    keyboard2.add(button_5)

    keyboard3.add(button_9)
    keyboard3.add(button_10)

    markup_t.add(item_t1, item_t15, item_t10, item_t5)
    markup_s.add(item_s1, item_s0)

    markup.add(item, item2)

    markup2.add(item3, item4, item34, item43)

    markup3.add(item5, item6, item7)
    markup3.add(item8, item9, item10)

    markup_n.add(item_n1, item_n2)
    a = datetime.now().strftime("%d.%m %H:%M")
    path = os.getcwd()
    print('\033[2;35;40m ' + str(a) + ' ' + str(message.text) + ' ' + message.from_user.first_name)
    if len(message.text) == 4:
        try:
            IDpath = path + '/ID'
            filelist = []
            for root, dirs, files in os.walk(IDpath):
                for file in files:
                    n = (os.path.join(file))
                    filelist.append(n)
            text = message.text
            for i in filelist:
                if i == text:
                    with open('ID/' + i, 'a+', encoding='utf-8') as f:
                        f.write('\n' + str(message.from_user.first_name) + '\n' + str(message.from_user.id))
                        f.close()
                    with open('ID/' + i, 'r', encoding='utf-8') as f:
                        name = f.readlines()[0]
                        name = name.replace('\n', '')
                        name = name.split(' ')
                        name = name[1] + ' ' + name[2]
                        f.close()
                    os.rename('ID/' + i, 'ID/' + i + '_a')
                    img = open('bot.gif', 'rb')
                    bot.send_video(message.chat.id, img)
                    img.close()
                    print('\033[2;32;40m [LOG] Пользователь', message.from_user.first_name, '/', message.from_user.id,
                          'зарегестрирован.')
                    bot.send_message(message.chat.id, texts.welcome_text_access.format(name=name))
                    bot.send_message(message.chat.id, texts.main, reply_markup=keyboard2)
        except Exception as exc:
            print(exc)
            traceback.print_exc()
            bot.send_message(message.chat.id, texts.welcome_text_access2)
            try:
                with open('ID/' + i, 'r', encoding='utf-8') as f:
                    id = f.readlines()[2]
                    print('\033[2;32;40m [LOG] Ошибка с пользователем ', id, 'решена')
                    bot.send_message(message.chat.id, texts.tr)
                    bot.send_message(message.chat.id, texts.main, reply_markup=keyboard2)
            except Exception as exc:
                print(exc)
                traceback.print_exc()
                print('\033[2;32;40m [LOG] Ошибка с пользователем ', id, 'не решена')
                bot.send_message(message.chat.id, texts.fl, )
    if "Полезные ссылки" in message.text:
        bot.send_message(message.chat.id, texts.urls, reply_markup=keyboard2)
    if "Домашнее задание" in message.text:
        bot.send_message(message.chat.id, 'На какую неделю хотите узнать домашнее задание?', reply_markup=markup)
    if "Учеба" in message.text:
        bot.send_message(message.chat.id, 'Что вас интересует?', reply_markup=keyboard)
    if "Настройки уведомлений⚙" in message.text:
        bot.send_message(message.chat.id, 'Что вы хотите изменить?', reply_markup=markup_n)
    if "Расписание" in message.text:
        bot.send_message(message.chat.id, 'На какой день вы хотите узнать расписание?', reply_markup=markup2)
    if 'Главная страница' in message.text:
        try:
            bot.send_message(message.chat.id, texts.main_text, reply_markup=keyboard3)
        except Exception as exc:
            print(exc)
            traceback.print_exc()

    if message.text == "Изменить время уведомления":
        path = os.getcwd() + '/ID'
        filelist = os.listdir(path)
        for i in filelist:
            if i != '.git' and i != '.idea':
                with open(path + '/' + str(i), 'r+', encoding='utf-8') as f:
                    line = f.readlines()
                    if str(message.from_user.id) in str(line[2]):
                        bot.send_message(chat_id=message.chat.id,
                                              text='Текущее время: ' + str(int(line[3]) // 60) + ' мин. На какое изменить?',
                                              reply_markup=markup_t)
    if message.text == "Включить/выключить уведомления":

        path = os.getcwd() + '/ID'
        filelist = os.listdir(path)
        for i in filelist:
            if i != '.git' and i != '.idea':
                with open(path + '/' + str(i), 'r+', encoding='utf-8') as f:
                    line = f.readlines()
                    if str(message.from_user.id) in str(line[2]):
                        if '1' in str(line[4]):
                            bot.send_message(chat_id=message.chat.id,
                                                  text='Сейчас уведомления включены.',
                                                  reply_markup=markup_s)
                        elif '0' in str(line[4]):
                            bot.send_message(chat_id=message.chat.id,
                                                  text='Сейчас ведомления выключены.',
                                                  reply_markup=markup_s)
    if message.text == "Вкл":
        path = os.getcwd() + '/ID'
        filelist = os.listdir(path)
        for i in filelist:
            if i != '.git' and i != '.idea':
                with open(path + '/' + str(i), 'r+', encoding='utf-8') as f:
                    line = f.readlines()
                    if str(message.from_user.id) in str(line[2]):
                        l0 = str(line[0])
                        l1 = str(line[1])
                        l2 = str(line[2])
                        l3 = str(line[3])
                        l4 = str(1)
                        f.seek(0)
                        f.truncate()
                        f.write(l0 + l1 + l2 + l3 + l4)
                        f.close()
                        bot.send_message(message.chat.id, 'Уведомления включены', reply_markup=keyboard2)
    if message.text == "Выкл":
        path = os.getcwd() + '/ID'
        filelist = os.listdir(path)
        for i in filelist:
            if i!='.git' and i!='.idea':
                with open(path + '/' + str(i), 'r+', encoding='utf-8') as f:
                    line = f.readlines()
                    if str(message.from_user.id) in str(line[2]):
                        l0 = str(line[0])
                        l1 = str(line[1])
                        l2 = str(line[2])
                        l3 = str(line[3])
                        l4 = str(0)
                        f.seek(0)
                        f.truncate()
                        f.write(l0 + l1 + l2 + l3 + l4)
                        f.close()
                        bot.send_message(message.chat.id, 'Уведомления выключены', reply_markup=keyboard2)
    if message.text == "1 мин":
        path = os.getcwd() + '/ID'
        filelist = os.listdir(path)
        for i in filelist:
            with open(path + '/' + str(i), 'r+', encoding='utf-8') as f:
                line = f.readlines()
                if str(message.from_user.id) in str(line[2]):
                    l0 = str(line[0])
                    l1 = str(line[1])
                    l2 = str(line[2])
                    l3 = str(60) + '\n'
                    l4 = str(line[4])
                    f.seek(0)
                    f.truncate()
                    f.write(l0 + l1 + l2 + l3 + l4)
                    f.close()
                    bot.send_message(chat_id=message.chat.id,
                                          text='Время изменено на 1 мин.',reply_markup=keyboard2)
    if message.text == "5 мин":
        path = os.getcwd() + '/ID'
        filelist = os.listdir(path)
        for i in filelist:
            with open(path + '/' + str(i), 'r+', encoding='utf-8') as f:
                line = f.readlines()
                if str(message.from_user.id) in str(line[2]):
                    l0 = str(line[0])
                    l1 = str(line[1])
                    l2 = str(line[2])
                    l3 = str(300) + '\n'
                    l4 = str(line[4])
                    f.seek(0)
                    f.truncate()
                    f.write(l0 + l1 + l2 + l3 + l4)
                    f.close()
                    bot.send_message(chat_id=message.chat.id,
                                          text='Время изменено на 5 мин.',reply_markup=keyboard2)
    if message.text == "10 мин":
        path = os.getcwd() + '/ID'
        filelist = os.listdir(path)
        for i in filelist:
            with open(path + '/' + str(i), 'r+', encoding='utf-8') as f:
                line = f.readlines()
                if str(message.from_user.id) in str(line[2]):
                    l0 = str(line[0])
                    l1 = str(line[1])
                    l2 = str(line[2])
                    l3 = str(600) + '\n'
                    l4 = str(line[4])
                    f.seek(0)
                    f.truncate()
                    f.write(l0 + l1 + l2 + l3 + l4)
                    f.close()
                    bot.send_message(chat_id=message.chat.id,
                                          text='Время изменено на 10 мин.',reply_markup=keyboard2)
    if message.text == "15 мин":
        path = os.getcwd() + '/ID'
        filelist = os.listdir(path)
        for i in filelist:
            with open(path + '/' + str(i), 'r+', encoding='utf-8') as f:
                line = f.readlines()
                if str(message.from_user.id) in str(line[2]):
                    l0 = str(line[0])
                    l1 = str(line[1])
                    l2 = str(line[2])
                    l3 = str(900) + '\n'
                    l4 = str(line[4])
                    f.seek(0)
                    f.truncate()
                    f.write(l0 + l1 + l2 + l3 + l4)
                    f.close()
                    bot.send_message(chat_id=message.chat.id,
                                          text='Время изменено на 15 мин.',reply_markup=keyboard2)

    # ОТПРАВКА СООБЩЕНИЙ-------------------------------------------------------------
    if codeA in message.text:
        try:
            a = datetime.today().strftime("%d.%m %H:%M")
            text = str(message.text)
            text = text.replace(codeA, '')
            print('\033[2;32;40m', str(a), ' [LOG]', message.from_user.id, '/', message.from_user.first_name, ' ',
                  'отправил admin сообщение:', text)
            path = os.getcwd() + '/ID'
            filelist = []
            for root, dirs, files in os.walk(path):
                for file in files:
                    n = (os.path.join(file))
                    filelist.append(n)
            for i in filelist:
                if '_a' in i:
                    with open(path + '/' + str(i), 'r+') as f:
                        line = f.readlines()
                        user = line[2]
                        bot.send_message(user, texts.messageA.format(messa=text, dt=str(a)), parse_mode='Markdown')
        except Exception as exc:
            print(i)
            print(exc)
            traceback.print_exc()

    if codeB in message.text:
        try:
            a = datetime.today().strftime("%d.%m %H:%M")
            text = str(message.text)
            text = text.replace(codeB, '')
            print('\033[2;32;40m', str(a), ' [LOG]', message.from_user.id, '/', message.from_user.first_name, ' ',
                  'отправил BOT сообщение:', text)
            path = os.getcwd() + '/ID'
            filelist = []
            for root, dirs, files in os.walk(path):
                for file in files:
                    n = (os.path.join(file))
                    filelist.append(n)
            for i in filelist:
                if '_a' in i:
                    with open(path + '/' + str(i), 'r+') as f:
                        line = f.readlines()
                        user = line[2]
                        try:
                            bot.send_message(user, texts.messageB.format(messb=text, dt=str(a)), parse_mode='Markdown')
                            print('send')
                        except Exception as exc:
                            print(exc)
                            traceback.print_exc()
        except Exception as exc:
            print(exc)
            traceback.print_exc()



# ОБРАБОТКА INLINE КНОПОК--------------------------------------------------------
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup2 = types.InlineKeyboardMarkup(row_width=2)
    markup3 = types.InlineKeyboardMarkup(row_width=7)
    markup31 = types.InlineKeyboardMarkup(row_width=7)

    markupdynamic = types.InlineKeyboardMarkup(row_width=6)

    item = types.InlineKeyboardButton('Текущая', callback_data='0')
    item2 = types.InlineKeyboardButton('Следующая', callback_data='1')



    item3 = types.InlineKeyboardButton('Сегодня', callback_data='today')
    item4 = types.InlineKeyboardButton('Завтра', callback_data='tomorrow')
    item34 = types.InlineKeyboardButton('На неделю', callback_data='default')
    item43 = types.InlineKeyboardButton('На следующую неделю', callback_data='next')

    item5 = types.InlineKeyboardButton('Понедельник', callback_data='01')
    item6 = types.InlineKeyboardButton('Вторник', callback_data='02')
    item7 = types.InlineKeyboardButton('Среда', callback_data='03')
    item8 = types.InlineKeyboardButton('Четверг', callback_data='04')
    item9 = types.InlineKeyboardButton('Пятница', callback_data='05')
    item10 = types.InlineKeyboardButton('Суббота', callback_data='06')
    item11 = types.InlineKeyboardButton('Понедельник', callback_data='11')
    item12 = types.InlineKeyboardButton('Вторник', callback_data='12')
    item13 = types.InlineKeyboardButton('Среда', callback_data='13')
    item14 = types.InlineKeyboardButton('Четверг', callback_data='14')
    item15 = types.InlineKeyboardButton('Пятница', callback_data='15')
    item16 = types.InlineKeyboardButton('Суббота', callback_data='16')




    markup.add(item, item2)
    markup2.add(item3, item4, item34, item43)
    markup3.add(item5, item6, item7)
    markup3.add(item8, item9, item10)
    markup31.add(item11, item12, item13)
    markup31.add(item14, item15, item16)


    if call.message:

        # ДОМАШНЕЕ ЗАДАНИЕ-------------------------------------------------------
        if call.data == '0':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='На какой день вы хотите узнать домашнее задание?', reply_markup=markup3)
        elif call.data == '1':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='На какой день вы хотите узнать домашнее задание?', reply_markup=markup31)
        elif call.data == '01':
            try:
                lst = homework0.Mo
                hw, urls = processing(lst)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.homework.format(a=hw[0], b=hw[1], c=hw[2], d=hw[3], e=hw[4]),
                                      reply_markup=markupdynamic)
                bot.send_document(call.message.chat.id, open(os.getcwd() + urls[0], 'rb'))
                print(lst)
            except Exception as exc:
                traceback.print_exc()
        elif call.data == '02':
            try:
                lst = homework0.Tu
                print(lst)
                print(homework0.Tu)
                hw, urls = processing(lst)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.homework.format(a=hw[0], b=hw[1], c=hw[2], d=hw[3], e=hw[4]),
                                      reply_markup=markupdynamic)
                bot.send_document(call.message.chat.id, open(os.getcwd() + urls[0], 'rb'))
            except Exception as exc:
                traceback.print_exc()
        elif call.data == '03':
            try:
                lst = homework0.We
                hw, urls = processing(lst)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.homework.format(a=hw[0], b=hw[1], c=hw[2], d=hw[3], e=hw[4]),
                                      reply_markup=markupdynamic)
                bot.send_document(call.message.chat.id, open(os.getcwd() + urls[0], 'rb'))
            except Exception as exc:
                traceback.print_exc()
        elif call.data == '04':
            try:
                lst = homework0.Th
                hw, urls = processing(lst)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.homework.format(a=hw[0], b=hw[1], c=hw[2], d=hw[3], e=hw[4]),
                                      reply_markup=markupdynamic)
                bot.send_document(call.message.chat.id, open(os.getcwd() + urls[0], 'rb'))
            except Exception as exc:
                traceback.print_exc()
        elif call.data == '05':
            try:
                lst = homework0.Fr
                hw, urls = processing(lst)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.homework.format(a=hw[0], b=hw[1], c=hw[2], d=hw[3], e=hw[4]),
                                      reply_markup=markupdynamic)
                bot.send_document(call.message.chat.id, open(os.getcwd() + urls[0], 'rb'))
            except Exception as exc:
                traceback.print_exc()
        elif call.data == '06':
            try:
                lst = homework0.Sa
                hw, urls = processing(lst)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.homework.format(a=hw[0], b=hw[1], c=hw[2], d=hw[3], e=hw[4]),
                                      reply_markup=markupdynamic)
                bot.send_document(call.message.chat.id, open(os.getcwd() + urls[0], 'rb'))
            except Exception as exc:
                traceback.print_exc()
        elif call.data == '11':
            try:
                lst = homework1.Mo
                hw, urls = processing(lst)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.homework.format(a=hw[0], b=hw[1], c=hw[2], d=hw[3], e=hw[4]),
                                      reply_markup=markupdynamic)
                bot.send_document(call.message.chat.id, open(os.getcwd() + urls[0], 'rb'))
                print(lst)
            except Exception as exc:
                traceback.print_exc()
        elif call.data == '12':
            try:
                lst = homework1.Tu
                hw, urls = processing(lst)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.homework.format(a=hw[0], b=hw[1], c=hw[2], d=hw[3], e=hw[4]),
                                      reply_markup=markupdynamic)
                bot.send_document(call.message.chat.id, open(os.getcwd() + urls[0], 'rb'))
                print(lst)
            except Exception as exc:
                traceback.print_exc()
        elif call.data == '13':
            try:
                lst = homework1.We
                hw, urls = processing(lst)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.homework.format(a=hw[0], b=hw[1], c=hw[2], d=hw[3], e=hw[4]),
                                      reply_markup=markupdynamic)
                bot.send_document(call.message.chat.id, open(os.getcwd() + urls[0], 'rb'))
                print(lst)
            except Exception as exc:
                traceback.print_exc()
        elif call.data == '14':
            try:
                lst = homework1.Th
                hw, urls = processing(lst)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.homework.format(a=hw[0], b=hw[1], c=hw[2], d=hw[3], e=hw[4]),
                                      reply_markup=markupdynamic)
                bot.send_document(call.message.chat.id, open(os.getcwd() + urls[0], 'rb'))
                print(lst)
            except Exception as exc:
                traceback.print_exc()
        elif call.data == '15':
            try:
                lst = homework1.Fr
                hw, urls = processing(lst)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.homework.format(a=hw[0], b=hw[1], c=hw[2], d=hw[3], e=hw[4]),
                                      reply_markup=markupdynamic)
                bot.send_document(call.message.chat.id, open(os.getcwd() + urls[0], 'rb'))
                print(lst)
            except Exception as exc:
                traceback.print_exc()
        elif call.data == '16':
            try:
                lst = homework1.Sa
                hw, urls = processing(lst)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.homework.format(a=hw[0], b=hw[1], c=hw[2], d=hw[3], e=hw[4]),
                                      reply_markup=markupdynamic)
                bot.send_document(call.message.chat.id, open(os.getcwd() + urls[0], 'rb'))
                print(lst)
            except Exception as exc:
                traceback.print_exc()

        # РАСПИСАНИЕ-------------------------------------------------------------
        elif call.data == 'today':
            try:
                today = datetime.today()
                nn = int(today.strftime("%U")) - 35
                c_date = date.today()
                day = str(c_date.day) + ' '
                month = months[int(c_date.month)]
                pairs = timetable_processing.get_timetable_today()
                try:
                    if pairs[5] == 'Авиамоторная':
                        place = 'на Авиамоторной'
                    elif pairs[5] == 'D':
                        place = 'онлайн 💻'
                    else:
                        place = 'на Октябрьском поле'
                except:
                    place = 'нигде'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.timetables_text.format(day=day + month, place=place, pair1=pairs[0],
                                                                        pair2=pairs[1], pair3=pairs[2], pair4=pairs[3],
                                                                        pair5=pairs[4],
                                                                        nn="\nТекущая неделя - " + str(nn + 1),
                                                                        parse_mode="Markdown"))
            except Exception as exc:
                print(exc)
                traceback.print_exc()

        elif call.data == 'tomorrow':
            try:
                c_date = date.today()
                day = str(int(c_date.day) + 1) + ' '
                month = months[int(c_date.month)]
                pairs = timetable_processing.get_timetable_tomorrow()
                try:
                    if pairs[5] == 'Авиамоторная':
                        place = 'на Авиамоторной'
                    elif pairs[5] == 'D':
                        place = 'онлайн 💻'
                    else:
                        place = 'на Октябрьском поле'
                except:
                    place = 'нигде'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.timetables_text.format(
                                          day=day + month,
                                          place=place,
                                          pair1=pairs[0],
                                          pair2=pairs[1],
                                          pair3=pairs[2],
                                          pair4=pairs[3],
                                          pair5=pairs[4],
                                          nn=" ",
                                          parse_mode="Markdown"))
            except Exception as exc:
                print(exc)
                traceback.print_exc()

        elif call.data == 'next':
            try:
                week_number = timetable_processing.get_week_num
                if week_number == 2:
                    bot.send_photo(chat_id=call.message.chat.id, photo=open('0.png', 'rb'))
                    bot.send_message(call.message.chat.id, "Цветовые обозначения:")
                    bot.send_message(call.message.chat.id, "Лекции - 🟢")
                    bot.send_message(call.message.chat.id, "Практика - 🟠")
                    bot.send_message(call.message.chat.id, "Лабораторные - 🟣")


                else:
                    bot.send_photo(chat_id=call.message.chat.id, photo=open('1.png', 'rb'))
                    bot.send_message(call.message.chat.id, "Цветовые обозначения:")
                    bot.send_message(call.message.chat.id, "Лекции - 🟢")
                    bot.send_message(call.message.chat.id, "Практика - 🟠")
                    bot.send_message(call.message.chat.id, "Лабораторные - 🟣")

            except Exception as exc:
                print(exc)
                traceback.print_exc()

        elif call.data == 'default':
            try:
                week_number = timetable_processing.get_week_num
                if week_number == 2:
                    bot.send_photo(chat_id=call.message.chat.id, photo=open('1.png', 'rb'))
                    bot.send_message(call.message.chat.id, "Цветовые обозначения:")
                    bot.send_message(call.message.chat.id, "Лекции - 🟢")
                    bot.send_message(call.message.chat.id, "Практика - 🟠")
                    bot.send_message(call.message.chat.id, "Лабораторные - 🟣")


                else:
                    bot.send_photo(chat_id=call.message.chat.id, photo=open('0.png', 'rb'))
                    bot.send_message(call.message.chat.id, "Цветовые обозначения:")
                    bot.send_message(call.message.chat.id, "Лекции - 🟢")
                    bot.send_message(call.message.chat.id, "Практика - 🟠")
                    bot.send_message(call.message.chat.id, "Лабораторные - 🟣")

            except Exception as exc:
                print(exc)
                traceback.print_exc()
        
# УВЕДОМЛЕНИЯ--------------------------------------------------------------------
def notif():
    H = datetime.today().strftime("%H")
    M = datetime.today().strftime("%M")
    S = datetime.today().strftime("%S")
    now_time = int(H) * 60 * 60 + int(M) * 60 + int(S)
    path = os.getcwd() + '/ID'
    filelist = os.listdir(path)
    for i in filelist:
        with open(path + '/' + str(i), 'r+', encoding='utf-8') as f:
            try:
                line = f.readlines()
                id = line[2]
                s_time = line[3]
                switch = line[4]
                if '1' in switch:
                    tt = timetable_processing.get_timetable_today()
                    for t in lessons:
                        index = lessons.index(t)
                        if tt[index] != '🚫':
                            if int(t) - int(now_time) == int(s_time):
                                print('notification')
                                bot.send_message(id, text='До начала пары осталось: ' + str(int(s_time) // 60) + ' мин.')
            except Exception as exc:
                print(exc)
                traceback.print_exc()
            f.close()


def main():
    print(texxt)
    try:
        bot.polling(none_stop=True)
    except Exception as exc:
        traceback.print_exc()


def second():
    while True:
        notif()
        time.sleep(1)


with ThreadPoolExecutor(max_workers=2 as pool:
    pool.submit(main)
    pool.submit(second)
