import json
from config import chats, persons


def check_chat_type(message, filename=None):
    chat_id = message.chat.id
    chat_name = message.chat.title
    chat_type = message.chat.type

    if chat_type == 'group' or chat_type == 'supergroup':
        check_chat(message)
    elif chat_type == 'private':
        check_person(message)
    else:
        print(f'warning! chatid: {chat_id}, chatname: {chat_name}, chat_type: {chat_type} \n exception in check chat type')
def check_person(message):
    try:
        name = message.from_user.first_name
        surname = message.from_user.last_name
        username = message.from_user.username
        language_code = message.from_user.language_code
        if username in persons:
            return True
        else:
            persons[username] = (message.chat.id, name, surname, language_code)
            print(f'new person: {username, message.chat.id, persons[username]}')
            dumppersons()
    except Exception as e:
        print('Exception check person: ', e)

def check_chat(message):
    try:
        chat_id = message.chat.id
        chat_title = message.chat.title if message.chat.title else "Unnamed"
        if str(chat_id) in chats:
            return True
        else:
            chats[chat_id] = f"{chat_title}"
            print(f"new chat: {chat_id, chats[chat_id]}")
            dumpchats()
    except Exception as e:
        print('Exception check chat: ', e)

def dumpchats():
    with open('chats.json', 'w') as file:
        json.dump(chats, file)
    print('chats.json DUMP')

def dumppersons():
    with open('persons.json', 'w') as file:
        json.dump(persons, file)
    print('persons.json DUMP')
    #chats[123] = "Chat 123"
    #persons[321] = "Person 321"

