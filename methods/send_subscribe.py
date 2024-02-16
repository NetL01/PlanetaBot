from config import bot
from telebot import types

def send_sub_message(chat_id, message_text):
    bot.send_message(int(chat_id), text=message_text, reply_markup=create_button())

def create_button():
    button = types.InlineKeyboardMarkup()
    button.add(types.InlineKeyboardButton(text="Кто это!?", callback_data="subscribe"))
    return button

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "subscribe":
        bot.send_message(call.message.chat.id, "Чтобы узнать имя, нужно купить подписку за 150 рэ\n"
                                               "Оплата через @netl01")