import telebot
from telebot import types # для указание типов
import config
from array import *
import os
import scrap
from datetime import datetime
import time
import re
import random
import requests
qwer = False
qwerty = False
qwert = False
create_list = False
TOKEN = '6002401569:AAGjvrcWn6JPWWa4vxRwZhPBsupYFyZ4RGw'
global_admin_password = '123456'
bot = telebot.TeleBot(TOKEN)
check_admin = 0
def log_nb_def(message, list):

    path = os.getcwd()
    path = path + '/Lib/log/' + str(message.chat.id)
    if os.path.isfile(path):
        None
    else:
        f = open(path, 'w', encoding="utf-8")
        f.close()



    f = open(path, 'a', encoding="utf-8")
    g = '\n[' + str(datetime.now()) + ']\n' + '[' + str(message.chat.username) + '] нажал кнопку\n' + '[' + list + ']\n'
    f.write(g)
    f.close()
def log_notbot_def(message, list):

    try:
        path = os.getcwd()
        path = path + '/Lib/log/' + str(message.from_user.id)
        if os.path.isfile(path):
            None
        else:
            f = open(path, 'w', encoding="utf-8")
            f.close()
    except AttributeError:
        path = path + '/Lib/log/' + str(message.id)
    f = open(path, 'a', encoding="utf-8")
    g = '\n[' + str(datetime.now()) + ']\n' +'[' + str(message.from_user.username) + ']\n' + '[' + list + ']\n'
    f.write(g)
    f.close()
def log_bot_def(message, list, botton = None):

    try:
        path = os.getcwd()
        path = path + '/Lib/log/' + str(message.from_user.id)
        if os.path.isfile(path):
            None
        else:
            f = open(path, 'w', encoding="utf-8")
            f.close()
    except AttributeError:
        path = path + '/Lib/log/' + str(message.id)
    f = open(path, 'a', encoding="utf-8")
    if botton == None:
        g = '\n[' + str(datetime.now()) + ']\n' + '[' + 'Бот' + ']\n' +  '[' + list + ']\n'
        f.write(g)
    else:
        tyu = ''
        for line in botton:
            tyu += '[' + line + ']\n'
        g = '[' + 'Бот' + ']\n' + '[' + str(datetime.now()) + ']\n' '[' + list + ']' + tyu
        f.write(g)
    f.close()
@bot.message_handler(commands=['start'])
def start_handler(message):

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
    help = types.KeyboardButton(text='Помощь')
    stop = types.KeyboardButton(text='Старт')
    stop1 = types.KeyboardButton(text='Лист тегов')
    chislo = types.KeyboardButton(text='О рандомном числе')
    keyboard.add(stop, help, stop1, chislo)
    """
    callback_button1 = types.InlineKeyboardButton(text="Помощь", callback_data="/help")
    callback_button2 = types.InlineKeyboardButton(text="Кнопка 2", callback_data="button2")
    callback_button3 = types.InlineKeyboardButton(text="Кнопка 3", callback_data="button3")
    callback_button4 = types.InlineKeyboardButton(text="Кнопка 4", callback_data="button4")
    callback_button5 = types.InlineKeyboardButton(text="Кнопка 5", callback_data="button5")
    callback_button6 = types.InlineKeyboardButton(text="Кнопка 6", callback_data="button6")
    callback_button7 = types.InlineKeyboardButton(text="Кнопка 7", callback_data="button7")
    keyboard.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button5,
                 callback_button6, callback_button7)"""

    bot.send_message(message.chat.id, 'Привет! Я твой бот, и я готов тебе помочь.\n'
                                      'Я бот, при помощи которого ты сможешь читать приготовленные для вас статьи!\n'
                                      'Есть несколько основных команд, которые тебе пригодятся!\n'
                                      '1. Команда */help* поможет тебе разобраться со всеми сложными командами.\n'
                                      '2. При помощи команды * /teglist * можно посмотреть доступные теги статей.\n'
                     , reply_markup=keyboard, parse_mode="html")
    a = 'Привет! Я твой бот, и я готов тебе помочь.\nЯ бот, при помощи которого ты сможешь читать приготовленные для вас статьи!\nЕсть несколько основных команд, которые тебе пригодятся!\n1. Команда */help* поможет тебе разобраться со всеми сложными командами.\n2. При помощи команды * /teglist * можно посмотреть доступные теги статей.\n'
    log_bot_def(message,a)
@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.chat.id, 'Я могу помочь тебе узнать команды.\n')
    a = 'Я могу помочь тебе узнать команды.\n'
    log_bot_def(message, a)
@bot.message_handler(commands=['rand'])
def rand_handler(message):
    g = str(random.randint(0, 2023))

    r = random.randint(1, 4)
    if r == 1:
        BASE_URL = 'http://numbersapi.com/' + g +'/trivia'
    elif r == 2:
        BASE_URL = 'http://numbersapi.com/' + g +'/math'
    elif r == 3:
        q = random.randint(1, 12)
        w = random.randint(1, 28)
        g = str(q) + '/' + str(w)
        BASE_URL = 'http://numbersapi.com/' + g +'/date'

    elif r ==4:
        BASE_URL = 'http://numbersapi.com/' + g +'/year'
    response = requests.get(BASE_URL)
    bot.send_message(message.chat.id,
                     response.text)
    log_bot_def(message, response.text)
@bot.message_handler(commands=['teglist'])
def teglist_handler(message):
    f = open('Lib/teglist/teglist', 'r', encoding="utf-8")
    ff = ''
    i = 1
    for line in f:
        ff = ff + str(i) + '.' + ' ' + line
        i += 1
    f.close()
    keyboard = types.InlineKeyboardMarkup()
    callback_button1 = types.InlineKeyboardButton(text="Да", callback_data="Da")
    callback_button2 = types.InlineKeyboardButton(text="Нет", callback_data="Net")
    keyboard.add(callback_button1, callback_button2)
    bot.send_message(message.chat.id,
                     'Я могу помочь тебе узнать основные направления статей.\n' + ff + '\n' + 'Желаете ли узнать подробности?', reply_markup=keyboard)
    yui = []
    g = 'Я могу помочь тебе узнать основные направления статей.\n' + ff + '\n' + 'Желаете ли узнать подробности?'
    yui.append('Да')
    yui.append('Нет')
    log_bot_def(message, g, yui)
@bot.message_handler(commands=['admin'])
def admin_handler(message):
    keyboard1 = types.InlineKeyboardMarkup()
    callback_button1 = types.InlineKeyboardButton(text="Ввести пароль", callback_data="passwd")
    callback_button2 = types.InlineKeyboardButton(text="Зайти как новый админ", callback_data="newad")
    callback_button3 = types.InlineKeyboardButton(text="Связаться для обсуждения", callback_data="button3")
    keyboard1.add(callback_button1,callback_button2, callback_button3)
    bot.send_message(message.chat.id,
                     'Вы хотите войти как админ. Выберите вариант.',reply_markup=keyboard1)
    yui = []
    g = 'Вы хотите войти как админ. Выберите вариант.'
    yui.append('Ввести пароль')
    yui.append('Зайти как новый админ')
    yui.append("Связаться для обсуждения")
    log_bot_def(message, g, yui)
@bot.message_handler(content_types=['text'])
def blabla(message):
    global check_admin, qwert, qwer, qwerty,create_list
    #Вопрос о создании нового тега
    log_notbot_def(message, message.text)
    if qwert == True:
        qwert = False
        a = message.text
        keyboard2 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="Да", callback_data="createteg")
        callback_button2 = types.InlineKeyboardButton(text="Нет", callback_data="none")
        keyboard2.add(callback_button1,callback_button2)
        bot.send_message(message.chat.id, 'Вы уверены, что хотите назвать новый тег: ' + a + '?'
                         , reply_markup=keyboard2, parse_mode="html")
        yui = []
        g = 'Вы уверены, что хотите назвать новый тег: ' + a + '?'
        yui.append('Да')
        yui.append("Нет")
        log_bot_def(message, g, yui)
    #Запись сообщения и названия в файл
    if qwer == True:
        qwer = False
        qwerty = True
    #Вопрос об уверенности в название
    if create_list == True:
        create_list = False

        keyboard2 = types.InlineKeyboardMarkup()
        f = open('Lib/list/lis', 'w', encoding="utf-8")
        f.write(message.text)
        f.close()
        callback_button2 = types.InlineKeyboardButton(text='Да', callback_data="reggg")
        callback_button3 = types.InlineKeyboardButton(text='Нет', callback_data="None1")
        keyboard2.add(callback_button2, callback_button3 )
        bot.send_message(message.chat.id,
                         "Вы уверены в названии?", reply_markup=keyboard2)
        yui = []
        g = "Вы уверены в названии?"
        yui.append('Да')
        yui.append("Нет")
        log_bot_def(message, g, yui)
    #Запись текста статьи и вопрос о разделе статьи
    if qwerty == True:
        qwerty = False
        f = open('Lib/teglist/teglist', 'r', encoding="utf-8")
        q = ''
        yui = []
        keyboard2 = types.InlineKeyboardMarkup()
        for line in f:
            yui.append(line)
            callback_button3 = types.InlineKeyboardButton(text=line, callback_data="boy_in" + line)
            keyboard2.add(callback_button3)
        f.close()
        f = open('Lib/list/liss', 'w', encoding="utf-8")
        f.write(message.text)
        f.close()
        bot.send_message(message.chat.id,
                         'Выберите в каком разделе вы хотите написать статью:', reply_markup=keyboard2)

        g = "Вы уверены в названии?"

        log_bot_def(message, g, yui)
    if message.text == 'Старт':
        start_handler(message)
    if message.text == 'Лист тегов':
        teglist_handler(message)
    if message.text == 'Помощь':
        help_handler(message)
    if message.text == 'О рандомном числе':
        rand_handler(message)
    if message.text == '123456' and check_admin == 1:
        bot.delete_message(message.chat.id, message.message_id)
        j = 0
        f = open('Lib/admins', 'r', encoding="utf-8")
        a = message.from_user.id
        list = []
        for line in f:
            list.append(line)
        f.close()
        f = open('Lib/admins', 'a', encoding="utf-8")
        for line in list:
            if (str(a ) + '\n') == str(line):
                j = 100
        if j > 0:
            bot.send_message(message.chat.id,
                             'Вы уже админ.')
            g = 'Вы уже админ.'

            log_bot_def(message, g, yui)
        if j == 0:
            f.write(str(a) + '\n' )
        f.close()
        check_admin = 0

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    # Ответ на каждую кнопку
    a = call.data
    #Даёт боту текст выбранной статьи
    if 'dopping' in a:
        w = a[7:17]
        sec = a[17:-2]
        log_nb_def(call.message, w + sec)
        path = os.getcwd()
        path1 = path
        path = path + '/' + 'Lib' + '/' + 'list' + '/' + 'Новости' + '/' + w + '/' + 'teglist'
        f = open(path, 'r', encoding="utf-8")
        for line in f:
            if sec in line:
                sec = line
        f.close()
        asd = re.sub(r'[^\w\s]', '', sec[:-1])
        path1 = path1 + '/' + 'Lib' + '/' + 'list' + '/' + 'Новости' + '/' + w + '/' + asd
        f = open(path1, 'r', encoding="utf-8")
        qwe = ''
        for line in f:
            qwe += line
        bot.send_message(call.message.chat.id,
                         qwe)
        log_bot_def(call.message.chat, qwe)
    #Запись новой статьи, её названия и её места
    if 'boy_in' in a:
        w = a[6:]
        log_nb_def(call.message, w)
        f = open('Lib/list/lis', 'r', encoding="utf-8")
        a = ''
        for line in f:
            a += line
        f.close()
        f = open('Lib/list/liss', 'r', encoding="utf-8")
        b = ''
        for line in f:
            b += line
        f.close()
        f = open('Lib/list/' + w +"/"+ a, 'w', encoding="utf-8")
        f.write(b)
        f.close()
        f = open('Lib/list/' + w + "/teglist", 'a', encoding="utf-8")
        f.write(a)
        f.close()
        bot.send_message(call.message.chat.id,
                         'Статья создана!')
        log_bot_def(call.message.chat, 'Статья создана!')
    #Предоставляет выбор статей или подтверждает их отсутствие
    if 'News' in a:

        q = 0
        w1 =  a[4:]
        w = w1.split('\n')
        log_nb_def(call.message, w[0])
        path = os.getcwd()
        path = path + '/' + 'Lib' + '/' + 'list' + '/' + 'Новости' + '/' + w[0] + '/' + 'teglist'
        f = open( path, 'r', encoding="utf-8")
        q = []
        for i in f:
            q.append(i)
        f.close()
        e = ''
        keyboard = types.InlineKeyboardMarkup()
        l = 0
        yui = []
        for i in q:
            art = w[0] + i[0:10]
            yui.append(i)
            callback_button1 = types.InlineKeyboardButton(text=i, callback_data="dopping" + art)
            keyboard.add(callback_button1)
            l += 1
        if l == 1:
            bot.send_message(call.message.chat.id,
                             'Статей нет')
            log_bot_def(chat.message, 'Статей нет')
        else:
            bot.send_message(call.message.chat.id,
                         'Выберите название статьи', reply_markup=keyboard)
            log_bot_def(call.message.chat, 'Выберите название статьи', yui)
    if 'Okey' in a:
        name = a[4:]
        log_nb_def(call.message, name)

        v = name.split(".")
        path = os.getcwd()
        path = path + '/' + 'Lib' + '/' + 'list' + '/' + v[2] + '/' + v[1]
        f = open(path, 'r', encoding="utf-8")
        u = ""
        i = 0
        for line in f:
            if i == 0:
                u += line + '\n'
            else:
                u += line
        if len(u) > 4095:
            for x in range(0, len(m), 4095):
                bot.send_message(call.message.chat.id,
                                 u[x:x + 4095])
        else:
            bot.send_message(call.message.chat.id,
                             u)

        log_bot_def(call.message.chat, u)

        #Показывает все доступные Новости
    if 'Yes' in a:

        name1 = a[3:]
        name = name1.split('\n')
        log_nb_def(call.message,name[0])
        path = os.getcwd()
        path = path + '/' + 'Lib' + '/' + 'list' + '/' + name[0] + '/' + 'teglist'
        f = open( path, 'r', encoding="utf-8")
        i = 1
        yui = []
        keyboard = types.InlineKeyboardMarkup()
        for line in f:

            if name[0] == "Новости":
                if line == str(datetime.now().date()):
                    yui.append("Today news")
                    callback_button1 = types.InlineKeyboardButton(text="Today news", callback_data="News" + line)
                else:
                    q = 0
                    lines = ''
                    for y in line:
                        if q < 4:
                            lines = lines + y
                        elif q == 4:
                            lines = lines + " года"
                        elif q > 4 and q < 7:
                            lines = lines + y
                        elif q == 7:
                            lines = lines + " месяца"
                        elif q > 7:
                            lines = lines + y
                        q += 1
                    lines = lines + ' дня'
                    yui.append(lines)

                    callback_button1 = types.InlineKeyboardButton(text=lines, callback_data="News" + line)
            else:

                callback_button1 = types.InlineKeyboardButton(text=line, callback_data="Okey" +'.'+ line +'.'+ name[0])
                yui.append(line)
            keyboard.add(callback_button1)
            i += 1
        f.close()
        if i == 1:
            bot.send_message(call.message.chat.id,
                             'Статей нет')
            log_bot_def(call.message.chat, 'Статей нет')
        else:

            bot.send_message(call.message.chat.id,
                         'Выберите название статьи', reply_markup=keyboard)
            log_bot_def(call.message.chat, 'Выберите название статьи', yui)
    if call.data == "None1":
        log_nb_def(call.message, 'Нет')
        f = open('Lib/list/lis', 'w', encoding="utf-8")
        f.write(message.text)
        f.close()
    if call.data == "reggg":
        log_nb_def(call.message, 'Да')
        bot.send_message(call.message.chat.id,
                         'Напишите текст к статье')
        log_bot_def(call.message.chat, 'Напишите текст к статье')
        global qwer
        qwer = True
    if call.data == "newlist":
        log_nb_def(call.message, "Добавить статью")
        global create_list
        create_list = True
        bot.send_message(call.message.chat.id,
                         'Какоe вы дадите название статье?')
        log_bot_def(call.message.chat, 'Какоe вы дадите название статье?')

    if call.data == "createteg":
        log_nb_def(call.message, "Да")
        a = len('Вы уверены, что хотите назвать новый тег: ')
        b = call.message.text[a:]
        c = b[:-1]
        f = open('Lib/teglist/teglist', 'a', encoding="utf-8")
        f.write('\n' + c)
        f.close()

        path = os.getcwd()
        path = path + '/' + 'Lib' + '/' + 'list' + '/' + c
        os.mkdir(path)
        f = open(path + '/teglist', 'a', encoding="utf-8")
        bot.send_message(call.message.chat.id,
                         'Директория создана.')
        log_bot_def(call.message.chat, 'Директория создана.')
        f.close()
    if call.data == "newteg":
        log_nb_def(call.message, "Добавить новый отдел")
        global qwert
        qwert = True
        bot.send_message(call.message.chat.id,
                         'Дайте называние')
        log_bot_def(call.message.chat, 'Дайте называние')
    if call.data == "Da":
        log_nb_def(call.message, "Да")
        f = open('Lib/teglist/teglist', 'r', encoding="utf-8")
        ff = ''
        i = 1
        scrap.scrap()
        keyboard = types.InlineKeyboardMarkup()
        yui = []
        for line in f:
            yui.append(line)
            callback_button1 = types.InlineKeyboardButton(text=line, callback_data="Yes" + line)
            keyboard.add(callback_button1)
            i += 1
        f.close()

        bot.send_message(call.message.chat.id,
                         'Выберите направление', reply_markup=keyboard)
        log_bot_def(call.message.chat, 'Выберите направление',yui)
    if call.data == "passwd":
        log_nb_def(call.message, "Ввести пароль")
        a = call.from_user.id
        user_name = call.from_user.username
        f = open('Lib/admins', 'r', encoding="utf-8")
        i = False
        bot.answer_callback_query(call.id,
                                  'Хз.')
        for line in f:
            if line == str(a)+'\n':
                keyboard2 = types.InlineKeyboardMarkup()
                callback_button1 = types.InlineKeyboardButton(text="Добавить статью", callback_data="newlist")
                callback_button2 = types.InlineKeyboardButton(text="Добавить новый отдел", callback_data="newteg")
                #callback_button3 = types.InlineKeyboardButton(text="Сделать рассылку", callback_data="rassilka")
                keyboard2.add(callback_button1, callback_button2, callback_button3)
                bot.send_message(call.message.chat.id,
                             'Выберите действие.', reply_markup=keyboard2)
                yui = []
                yui.append("Добавить статью")
                yui.append("Добавить новый отдел")
                yui.append("Сделать рассылку")
                log_bot_def(call.message.chat, 'Выберите действие.', yui)
        f.close()

    if call.data == "newad":
        log_nb_def(call.message, "Зайти как новый админ")
        global check_admin
        bot.answer_callback_query(call.id,
                         'Введите глобальный пароль администратора.')
        log_bot_def(call.message.chat, 'Введите глобальный пароль администратора.', yui)
        check_admin = 1
bot.polling()