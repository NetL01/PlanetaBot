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