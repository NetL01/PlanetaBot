from config import bot


def say_command(command):
    try:
        _, chat_id, text = command.split(maxsplit=2)
        # send_message_to_chat(chat_id, text)
        # print(f"{chat_id, text}")
        bot.send_message(chat_id, text=text)
    except Exception as e:
        print("Ошибка при отправке сообщения:", e)