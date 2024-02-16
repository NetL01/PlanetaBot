import telebot
import json

# Инициализация бота
bot = telebot.TeleBot('6817773118:AAEZme_6IpKdWIU8lQUUIbi31lbluPzQj3k')


# Функция загрузки данных из файла JSON
def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


# Функция сохранения данных в файл JSON
def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


# Обработчик события добавления бота в группу
@bot.chat_member_handler(content_types=['new_chat_members'])
def handle_new_chat_members(message):
    chat_id = message.chat.id
    chat_name = message.chat.title
    filename = "chats.json"

    chat_data = load_data(filename)
    if str(chat_id) not in chat_data:
        chat_data[str(chat_id)] = chat_name
        save_data(chat_data, filename)


# Обработчик новых сообщений в личных чатах
@bot.message_handler(func=lambda message: True, content_types=['text'], private=True)
def handle_new_private_message(message):
    chat_id = message.chat.id
    chat_name = message.chat.first_name  # Для личных чатов бота с пользователями
    filename = "persons.json"
    print('working1')

    chat_data = load_data(filename)
    if str(chat_id) not in chat_data:
        chat_data[str(chat_id)] = chat_name
        save_data(chat_data, filename)


# Запуск бота
bot.polling()


try:
    with open('chats.json', 'r') as file:
        chats = json.load(file)
        print(chats)
except FileNotFoundError:
    chats = {}