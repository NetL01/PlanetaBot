from datetime import datetime, timedelta
from yoomoney import Client
from config import yoomoney_token, bot, admin_chat_id


def get_daily_transactions_sum():
    token = yoomoney_token
    client = Client(token)
    history = client.operation_history()
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    tomorrow = today + timedelta(days=1)
    daily_transactions_sum = 0
    for operation in history.operations:
        if today <= operation.datetime < tomorrow:
            daily_transactions_sum += operation.amount
    bot.send_message(admin_chat_id, text=f'Стастистика за день: \n\tПолучено: \n\t-->{daily_transactions_sum} руб.')