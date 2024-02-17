from yoomoney import Client
from config import yoomoney_token, bot


def give_operations(message):
    client = Client(yoomoney_token)
    history = client.operation_history()
    if history.next_record == None:
        bot.reply_to(message, text=f'There are no one operation yet')
    # print("Next page starts with: ", history.next_record)
    # for operation in history.operations:
    #     print()
    #     print("Operation:",operation.operation_id)
    #     print("\tStatus     -->", operation.status)
    #     print("\tDatetime   -->", operation.datetime)
    #     print("\tTitle      -->", operation.title)
    #     print("\tPattern id -->", operation.pattern_id)
    #     print("\tDirection  -->", operation.direction)
    #     print("\tAmount     -->", operation.amount)
    #     print("\tLabel      -->", operation.label)
    #     print("\tType       -->", operation.type)
