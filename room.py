class Room:
    def __init__(self, num, desc, dirs, inv=[]):
        self.number = num
        self.description = desc
        self.directions = dirs
        self.inventory = inv

    def display_description(self):
        if self.description != "":
            return self.description

    def list_directions(self):
        if len(self.directions) > 0:
            dir_string = "You can go the following directions: "
            ret_string = ""
            for dx in self.directions:
                ret_string = ret_string + str(dx) + " "
            ret_string = dir_string + ret_string
            return ret_string

    def list_inventory(self):
        print("You see: ")
        if len(self.inventory) > 0:
            self.inventory.sort()
            for item in self.inventory:
                print("-", self.add_article(item))
        else:
            print("You're empty-handed.")
        
    def add_item(self, item):
        # add item to room's inventory
        if not(item in self.inventory):
            self.inventory.append(item)
        else:
            print("You can't drop what you don't have.")

    def del_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            self.list_inventory()

    def add_article (self, name):
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