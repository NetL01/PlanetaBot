from config import yoomoney_token, bot
from yoomoney import Client
import os
from console_methods import console_asay_method

def check():
    print('check working')
    file_path = "C:\\Users\\razuv\\PycharmProjects\\PlanetaBot_main\\bank_operations\\transaction_ids.txt"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            last_transaction_id = int(file.read().strip())
    else:
        last_transaction_id = 0

    token = yoomoney_token
    client = Client(token)
    history = client.operation_history()
    count = 0
    for operation in history.operations:
        if int(operation.operation_id) > int(last_transaction_id):
            text = f"Found new transactions:\n"
            text += f"\t--> Date: {operation.datetime}\n"
            text += f"\t--> Title: {operation.title}\n"
            text += f"\t--> Amount: {operation.amount}\n"
            text += f"\t--> Status: {operation.status}"
            bot.send_message(-1002114955301, text=text)
            last_transaction_id = operation.operation_id
            with open(file_path, "w") as file:
                file.write(str(last_transaction_id))
            count += 1
    if count == 0:
        #bot.send_message(-1002114955301, text=f'За прошедшее время не было новых пополнений.')
        pass
