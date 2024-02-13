import telebot

# Создаем второй бот
worker_bot = telebot.TeleBot('5849840132:AAHpp7xjRYhhmB4HwZArZCpJ6_9BMEJpLJY')

# Определяем обработчики команд для второго бота
@worker_bot.message_handler(commands=['start'])
def handle_start(message):
    worker_bot.reply_to(message, "Hello! I'm the worker bot.")

@worker_bot.message_handler(commands=['stop'])
def handle_stop(message):
    worker_bot.reply_to(message, "Goodbye! I'm stopping now.")

# Запускаем второго бота в отдельном потоке
worker_bot.polling(none_stop=True)
