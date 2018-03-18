from room import Room
from player import Player
#from item import Item

# __author__ = 'alex' 

# Trial intfic project w/ kids
# just to see what they can do

#room_num = 0

world = []
theRoom = Room(0, "Your starting point. It's kind of dark here.", ['n', 's'],
               ["apple", "banana", "cat", "dog", "egg", "fox"])
player = Player([])

def add_article(name):
    # simple plural test
    if len(name) > 1 and name[len(name)-1] == 's' and name[len(name)-2] != 's':
        return name
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"
    if name and (name[0] in vowels):
        article = "an "
    elif name and (name[0] in consonants):
        article = "a "
    else:
        article = ""
    return "%s%s" % (article, name)


def get_room(room):
    print(room.display_description())
    print(room.list_directions())
    if len(room.inventory) > 0:
        room.list_inventory()


def process_cmd(cmd):
    if cmd[:3] == "get":
        item2add = cmd[4:]
        if item2add == "all":
            for item in theRoom.inventory:
                player.add_item(item)
            player.list_inventory()
            theRoom.inventory = []
        elif item2add in player.inventory:
            print("You already have " + add_article(item2add) + "!")
        else:
            if item2add in theRoom.inventory:
                player.add_item(item2add)
                theRoom.del_item(item2add)
                print(add_article(item2add), "has been added!")
            else:
                print("There isn't " + add_article(item2add) + " here.")
    elif cmd[:4] == "drop":
        item2drop = cmd[5:]
        if item2drop == "all":
            for item in player.inventory:
                theRoom.add_item(item)
            theRoom.list_inventory()
            player.inventory = []
        elif item2drop not in player.inventory:
            print("You don't have " + add_article(item2drop) + " to drop.")
        else:
            player.del_item(item2drop)
            theRoom.add_item(item2drop)
            print(add_article(item2drop), "has been dropped!")
    elif cmd[:3] == "inv":
        player.list_inventory()
    elif cmd[:4] == "look":
        get_room(theRoom)
        # if len(theRoom.inventory) > 0:
        #     theRoom.list_inventory()
        # else:
        #     print("I don't see anything important here right now.")
    elif cmd[:5] == "score":
        print("Your score so far:", player.score)
    elif cmd[:4] == "exam":
        if cmd[:7] == "examine":
            itemtoExam = cmd[8:]
        else:
            itemtoExam = cmd[5:]
        if itemtoExam in player.inventory:
            print("There's nothing special about the", itemtoExam + "...yet.")
        elif itemtoExam not in theRoom.inventory:
            print("I don't see any", itemtoExam, "here.")
        else:
            print("You can't examine the", itemtoExam,
                  "unless you're holding it.")
    elif cmd[:3] == "eat":
        itemtoEat = cmd[4:]
        if itemtoEat not in player.inventory:
            if itemtoEat in theRoom.inventory:
                print("You'd have to pick it up first.")
            else: 
                print("You can't eat what you don't have.")
        else:
            print("You have eaten", add_article(itemtoEat) +". Congratulations.")
            player.del_item(itemtoEat)
    elif cmd[:1] == "q":
        print("Thanks for playing!")
        print("Your final score was:", player.score)
        exit()

    return


running = True

get_room(theRoom)  # print room description the first time

while running:
    cmd = input("What's next? ")
    player.score = len(player.inventory)
    process_cmd(cmd)
    # get_room(theRoom)
