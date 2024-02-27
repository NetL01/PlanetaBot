from config import bot


def news_send_command(command):
    try:
        _, chat_id = command.split(maxsplit=2)
        # send_message_to_chat(chat_id, text)
        # print(f"{chat_id, text}")
        with open('/data/pictures/news/razriv_anusa.jpg', 'rb') as photo:
            caption = input('Caption: ')
            bot.send_photo(chat_id, photo, caption=caption)
    except Exception as e:
        print("Ошибка при отправке сообщения:", e)