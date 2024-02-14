import requests
import telebot

token = '6817773118:AAEZme_6IpKdWIU8lQUUIbi31lbluPzQj3k'

bot = telebot.TeleBot(token)
def check_bot_token(token):
    url = f"https://api.telegram.org/bot{token}/getMe"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200 and data["ok"]:
        print("API ключ действителен.")
        print(data["result"])

    else:
        print("API ключ недействителен или произошла ошибка.")

# Замените 'YOUR_BOT_TOKEN' на свой токен бота
check_bot_token(token)