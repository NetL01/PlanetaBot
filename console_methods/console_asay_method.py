from config import bot


def say_command(command):
    try:
        # send_message_to_chat(chat_id, text)
        # print(f"{chat_id, text}")
        text = command[6::]
        bot.send_message(-1002114955301, text=text)
    except Exception as e:
        print("Ошибка при отправке сообщения:", e)