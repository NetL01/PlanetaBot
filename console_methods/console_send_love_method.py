from telebot import types
from bank_operations import get_bankAccount_quickform
from config import bot
from methods.send_subscribe import send_sub_message

def send_love(command):
    try:
        _, chat_id = command.split(maxsplit=2)
        message_text = input('Enter text: ')
        send_sub_message(chat_id, message_text)
        print('|Success|')
    except Exception as e:
        print("Ошибка при отправке сообщения:", e)

def send_love_pic(command):
    try:
        _, chat_id = command.split(maxsplit=2)
        with open('C:\\Users\\razuv\\PycharmProjects\\PlanetaBot_main\\data\\pictures\\photo1.jpg', 'rb') as photo:
            caption = input('Caption: ')
            print('work')
            bot.send_photo(chat_id, photo, caption=caption, reply_markup=create_button())

    except Exception as e:
        print("Ошибка при отправке сообщения:", e)


def create_button():
    button = types.InlineKeyboardMarkup()
    button.add(types.InlineKeyboardButton(text="Кто это!?", callback_data="subscribe"))
    return button

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "subscribe":
        bot.send_message(call.message.chat.id, "Чтобы узнать имя, нужно купить подписку.")
        get_bankAccount_quickform.give_quickpay(call.message)