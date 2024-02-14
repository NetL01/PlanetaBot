from methods import cryptomethod, encode, graphix, send_subscribe, check
from console_methods import console_say_method, console_asay_method
from config import bot
import threading



@bot.message_handler(commands=['check', 'status'])
def check(message):
    check.timetest(message)

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



# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def console_commands_realisator():
    while True:
        command = input("Command: ")
        if command.startswith("/say"):
            console_say_method.say_command(command)
        if command.startswith("/asay"):
            console_asay_method.say_command(command)

        else:
            print("unknown command.")


console_thread = threading.Thread(target=console_commands_realisator)
console_thread.start()


bot.polling(none_stop=True)
