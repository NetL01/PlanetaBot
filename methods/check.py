from datetime import time
from config import bot


def timetest(message):
    start_time = time.time()
    msg = bot.send_message(message.chat.id, "Проверяется состояние соединения с серверами Telegram [0/5]")
    for i in range(1, 6):
        time.sleep(1)
        bot.edit_message_text(f"Проверяется состояние соединения с серверами Telegram [{i}/5]", message.chat.id,
                              msg.message_id)
    end_time = time.time()
    delay = str(end_time - start_time - 5)[:3]
    bot.edit_message_text(f"Статус работы: стабильный. Задержка: {delay} cек.", message.chat.id,
                          msg.message_id)