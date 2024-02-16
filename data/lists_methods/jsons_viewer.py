import json


def viewer():
    try:
        with open('C:\\Users\\razuv\\PycharmProjects\\PlanetaBot_main\\chats.json', 'r') as file:
            chats = json.load(file)
            print('chats.json found and loaded')
            # print(chats)
    except:
        chats = {}
        print('chats.json not found')

    try:
        with open('C:\\Users\\razuv\\PycharmProjects\\PlanetaBot_main\\persons.json', 'r') as file:
            persons = json.load(file)
            print('persons.json found and loaded')
            # print(persons)
    except:
        persons = {}
        print('persons.json not found')
    return chats, persons




