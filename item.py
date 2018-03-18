# what needs to be in an item class?
# 
# name, description, buy/sell value, +/- HP, edible?, 
# magic/enchanted, container?, bind/no-bind

class Item:
    def __init__(self, name, description, value):
        name = name
        description = description
        value = value    