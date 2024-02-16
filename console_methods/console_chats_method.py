from config import chats, persons


def give_chats():
    try:
        #print(f"{chats}")
        print(f'Dictionary of: {len(chats)} elements')
        for i, (chat_id, chat_name) in enumerate(chats.items(), start=1):
            print(f"{i}. Chat ID: {chat_id}, Chat Name: {chat_name}")
    except Exception as e:
        print("Exception give_chats console method:", e)