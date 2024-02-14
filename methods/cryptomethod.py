import requests
from config import bot


def get_crypto_data(coin):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data[coin]["usd"]

def give_crypto_data(message):
    coins = ["bitcoin", "ethereum", "ripple", "bitcoin-cash", "litecoin"]
    response_text = ""
    for coin in coins:
        price = get_crypto_data(coin)
        response_text += f"{coin.capitalize()}: ${price:.2f}\n"
    bot.reply_to(message, response_text)
    print(message.chat.id)