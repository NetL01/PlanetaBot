import json

import data.lists_methods.jsons_viewer
from data.lists_methods import dump_active
from methods import cryptomethod, encode, graphix, send_subscribe, checkstatus
from console_methods import console_say_method, console_asay_method, console_persons_method, console_chats_method, console_send_love_method
from config import bot
import threading
from data.lists_methods.dump_active import check_chat_type
global chats
global persons


@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    bot.reply_to(message, f'Hello, {name}, you can work with me.')
    check_chat_type(message)

@bot.message_handler(commands=['check', 'status'])
def timecheck(message):
    checkstatus.timetest(message)

@bot.message_handler(commands=['coins'])
def coins(message):
    cryptomethod.give_crypto_data(message)

@bot.message_handler(commands=['encode'])
def handle_encode(message):
    encode.go_encode(message)

@bot.message_handler(commands=['decode'])
def handle_decode(message):
    encode.go_decode(message)

@bot.message_handler(commands=['send'])
def send(message):
    send_subscribe.send_message(message)

@bot.message_handler(commands=['graphix'])
def send_graph(message):
    graphix.graphix(message)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Выводим сообщение в консоль
    print(f'From {message.from_user.username}, chatid: {message.chat.id}, text: {message.text}')


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def console_commands_realisator():
    while True:
        command = input()
        if command.startswith("/say"):
            console_say_method.say_command(command)
        if command.startswith("/asay"):
            console_asay_method.say_command(command)
        if command.startswith("/chats"):
            console_chats_method.give_chats()
        if command.startswith("/persons"):
            console_persons_method.give_persons()
        if command.startswith("/send_love"):
            console_send_love_method.send_love(command)
        if command.startswith("/r"):
            print('|Success|')
        #else:
        #    print("unknown command.")


console_thread = threading.Thread(target=console_commands_realisator)
console_thread.start()


bot.polling(none_stop=True)
