import json

def print_persons_data():
    try:
        with open('persons.json', 'r') as file:
            chats = json.load(file)
            print("Persons Data:")
            print(json.dumps(chats, indent=4))
    except Exception as E:
        print("Exception:", E)