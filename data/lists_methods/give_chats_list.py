import json

def print_chats_data():
    try:
        with open('chats.json', 'r') as file:
            chats = json.load(file)
            print("Chats Data:")
            print(json.dumps(chats, indent=4))
    except Exception as E:
        print("Exception:", E)
