from config import bot
from telebot import types
from bank_operations import get_bankAccount_quickform
def send_sub_message(chat_id, message_text):
    bot.send_message(int(chat_id), text=message_text, reply_markup=create_button())

def create_button():
    button = types.InlineKeyboardMarkup()
    button.add(types.InlineKeyboardButton(text="Кто это!?", callback_data="subscribe"))
    return button

# @bot.callback_query_handler(func=lambda call: True)
# def callback_query(call):
#     print(f'{call.message.from_user.username} нажал кнопку.')
#     if call.data == "subscribe":
#         bot.send_message(call.message.chat.id, "Чтобы узнать имя, нужно купить подписку.")
#         get_bankAccount_quickform.give_quickpay(call.message)