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
        with open('C:\\Users\\razuv\\PycharmProjects\\PlanetaBot_main\\data\\pictures\\girls\\photo2.jpg', 'rb') as photo:
            caption = input('Caption: ')
            print('work')
            bot.send_photo(chat_id, photo, caption=caption, reply_markup=create_button1())

    except Exception as e:
        print("Ошибка при отправке сообщения:", e)


def create_button1():
    button = types.InlineKeyboardMarkup()
    button.add(types.InlineKeyboardButton(text="Кто это!?", callback_data="subscribe_pic"))
    return button

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    print(f'{call.message.from_user.username} нажал кнопку.')
    if call.data == "subscribe_pic":
        print(call.message.chat.id)
        if str(call.message.chat.id) == str(387170502):
            bot.send_message(call.message.chat.id, "ты и так знаешь кто это, милашка) <3")
        else:
            bot.send_message(call.message.chat.id, "Вам нужно приобрести подписку.")
            get_bankAccount_quickform.give_quickpay(call.message)