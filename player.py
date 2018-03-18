class Player:
    def __init__(self, inv=[], health = 100, score = 0):
        self.inventory = inv
        # not sure we'll use health or score, or what values are correct here yet

    def list_inventory(self):
        print("Checking inventory...")
        if len(self.inventory) > 0:
            self.inventory.sort()
            print("You're carrying: ")
            for item in self.inventory:
                print("-", self.add_article(item))
        else:
            print("You're empty-handed.")

    def add_item(self, item):
        # add item to player's inventory
        if not(item in self.inventory):
            self.inventory.append(item)
        else:
            print("You already have " + self.add_article(item) + ".")

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