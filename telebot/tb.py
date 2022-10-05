# 5547159872:AAENXbQARhFotlAVyh2it8hMADGWKqX00nw
import telebot
import mysql.connector
import requests
from bs4 import BeautifulSoup
import time
import smtplib
class Currency:
    BTC_USD = 'https://www.coingecko.com/en/coins/bitcoin'
    ETH_USD = 'https://www.coingecko.com/en/coins/ethereum'
    BNB_USD = 'https://www.coingecko.com/en/coins/bnb'
    polkadot = 'https://cryptorank.io/price/polkadot/arbitrage'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

    current_price_BTC = 0
    dif_BTC = 0.3

    def __init__(self):
        self.current_price_BTC = float(self.get_currency_BTC())

    def get_currency_BTC(self):
        full_page = requests.get(self.BTC_USD, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "no-wrap","data-target": "price.price"})
        real_price = convert[0].text.replace('$','').replace(',','')
        return real_price

    def get_currency_ETH(self):
        full_page = requests.get(self.ETH_USD, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "no-wrap","data-target": "price.price"})
        real_price = convert[0].text.replace('$','').replace(',','')
        return real_price

    def get_currency_BNB(self):
        full_page = requests.get(self.BNB_USD, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "no-wrap","data-target": "price.price"})
        real_price = convert[0].text.replace('$','').replace(',','')
        return real_price

    def check_currency(self):
        currency = float(self.get_currency_BTC())
        if currency >= self.current_price_BTC + self.dif_BTC:
            self.send_mail()
        elif currency <= self.current_price_BTC - self.dif_BTC:
            self.send_mail()

    def get_DOT(self):
        full_page = requests.get(self.polkadot, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span")[12]
        convert = str(convert).split()[77:78]
        real_price = float(str(convert)[2:6])
        return real_price

    def send_mail(self):
        server = smtplib.SMTP_SSL('smtp.yandex.by', 465)
        server.ehlo()
        fromaddr = email
        toaddrs = email

        server.login('drvictor@tut.by', 'gjlpfobnjq123$%^')

        subject = 'BTC'
        body = 'Changed'
        message = 'It is time. BTC has changed!'
        server.sendmail(fromaddr,toaddrs,message)
        server.quit()

currency = Currency()
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="mydatabase"
)
mycursor = mydb.cursor()
try:
    mycursor.execute("CREATE DATABASE mydatabase")
    mycursor.execute("""CREATE TABLE customers
        (id INT AUTO_INCREMENT PRIMARY KEY, name
        VARCHAR(25), surname VARCHAR(25), email VARCHAR(25))
        """)
except:
    pass

from telebot import types
bot = telebot.TeleBot('5547159872:AAENXbQARhFotlAVyh2it8hMADGWKqX00nw')

def save_users():
    mycursor.execute("INSERT INTO customers (name, surname, email) VALUES (%s, %s, %s)",(name,surname, email))
    mydb.commit()

name = ""
surname = ""
email = ""
flag = False
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if flag:
        currency.check_currency()
        print('2')
    if message.text=='hello':
        mess = f'Здравствуйте, <b>{message.from_user.first_name}.</b>'
        bot.send_message(message.chat.id, mess,parse_mode='html')
        bot.send_message(message.chat.id, 'Выберите режим работы')
        keyboard = types.InlineKeyboardMarkup()
        key_reg = types.InlineKeyboardButton(text='Регистрация', callback_data='reg')
        key_btc = types.InlineKeyboardButton(text='BTC', callback_data='btc')
        key_eth = types.InlineKeyboardButton(text='ETH', callback_data='eth')
        key_bnb = types.InlineKeyboardButton(text='BNB', callback_data='bnb')
        key_track = types.InlineKeyboardButton(text='Track BTC', callback_data='track')
        key_stop = types.InlineKeyboardButton(text='Stop tracking', callback_data='stop')
        key_polcadot = types.InlineKeyboardButton(text='Example', callback_data='DOT')
        keyboard.add(key_btc, key_eth, key_bnb, key_track, key_stop, key_reg, key_polcadot)
        bot.send_message(message.from_user.id, text='Bitcoin is the king!', reply_markup=keyboard)

    elif message.text=='/help':
        bot.send_message(message.chat.id, 'Help yourself!')
    elif message.text=='website':
        website(message)
    else:
        bot.send_message(message.chat.id, 'я тебя не понимаю')
def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.chat.id, "Далее напиши свою фамилию:")
    bot.register_next_step_handler(message,reg_surname)

def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.chat.id, "Напиши свой e-mail:")
    bot.register_next_step_handler(message,reg_email)

def reg_email(message):
    global email
    email = message.text
    save_users()
    bot.send_message(message.chat.id, "Введённые данные сохранены.")

@bot.callback_query_handler(func = lambda call: True)
def callback_worker(call):
    global flag
    if flag:
        currency.check_currency()
        print('1')
    if call.data == 'reg':
        bot.send_message(call.message.chat.id, "Для регистрации введи своё имя:")
        bot.register_next_step_handler(call.message, reg_name)
    elif call.data == 'btc':
        str1 = 'Текущий курс BTC = '+ currency.get_currency_BTC() +'$'
        bot.send_message(call.message.chat.id, str1)
    elif call.data == 'eth':
        str1 = 'Текущий курс ETH = '+ currency.get_currency_ETH() +'$'
        bot.send_message(call.message.chat.id, str1)
    elif call.data == 'bnb':
        str1 = 'Текущий курс BNB = '+ currency.get_currency_BNB() +'$'
        bot.send_message(call.message.chat.id, str1)
    elif call.data == 'track':
        if email != '':
            bot.send_message(call.message.chat.id, 'Включён режим отслеживания.')
            currency.check_currency()
            flag = True
        else:
            bot.send_message(call.message.chat.id, 'Для начала отслеживания необходима регистрация.')
    elif call.data == 'stop':
        flag = False
        bot.send_message(call.message.chat.id, 'Режим отслеживания выключен.')
    elif call.data == 'DOT':
        bot.send_message(call.message.chat.id, f'На монете Polcadot можно заработать {currency.get_DOT()}% прибыли.')

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Подробности по ссылке", url="https://cryptorank.io/price/polkadot/arbitrage"))
    bot.send_message(message.chat.id, 'Перейти на сайт', reply_markup=markup)






bot.polling(none_stop=True, interval=0)



