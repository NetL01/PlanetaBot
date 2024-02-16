from config import persons


def give_persons():
    try:
        #print(f"{persons}")
        print(f'Dictionary of: {len(persons)} elements')
        for i, (chat_id, chat_name) in enumerate(persons.items(), start=1):
            print(f"{i}. Chat ID: {chat_id}, Chat Name: {chat_name}")
    except Exception as e:
        print("Exception give_chats console method:", e)