from config import yoomoney_token, bot
from yoomoney import Client

def give_balance(message):
    #try:
        client = Client(yoomoney_token)
        user = client.account_info()
        if (len(message.text.split(' ')) > 1):
            flag = message.text.split(' ')[1]
            if(flag == '-all'):
                text = 'Extended balance information:\n'
                for pair in vars(user.balance_details):
                    text += f'\t--> {pair} : {vars(user.balance_details).get(pair)}\n'
                bot.send_message(message.chat.id, text=text)
        else:
            account_number = user.account
            account_balance = user.balance
            bot.send_message(message.chat.id, text=f'Account number: {account_number}\nAccount balance: {account_balance}')
    #except Exception as e:
        #print('Exception give_balance: ', e)



