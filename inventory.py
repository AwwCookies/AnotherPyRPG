from collections import defaultdict
from items.item import Item


class Inventory:
    def __init__(self):
        self._inventory = {}

    def amount_of(self, item_name):
        """
        :param item_name: Item Name. Example: Minor Health Potion
        :return: Int: The amount of `item_name`
        """
        return self._inventory.get(item_name).get("amount")

    def add_item(self, item, amount=1, prnt=False):
        if item.name in self._inventory:
            self._inventory[item.name]["amount"] += amount
        else:
            self._inventory[item.name] = {
                "item": item,
                "amount": amount
            }
        if prnt:
            print("Added %i %s to your inventory" % (amount, item.name))

    def remove_item(self, item_name, amount=1, prnt=False):
        if item_name in self._inventory:
            if self.amount_of(item_name) >= amount:
                self._inventory.get(item_name)["amount"] -= amount
                if prnt:
                    print("Removed %sx%i from your inventory" % (item_name, amount))
                return amount
        if prnt:
            print("Removed %sx%i from your inventory" % (item_name, 0))
        return 0

    def display(self):
        for item in self._inventory:
            print("%s: %i" % (item, self._inventory[item]["amount"]))


########### Tests #############
def test_add_item():
    inv = Inventory()
    inv.add_item(Item(item_name="Test Item"), amount=80, prnt=True)
    inv.add_item(Item(item_name="Test Item"), amount=1, prnt=True)

def test_remove_item():
    inv = Inventory()
    inv.add_item(Item(item_name="Test Item"), amount=80, prnt=True)
    assert inv.remove_item("Test Item", amount=999, prnt=True) == 0
    assert inv.remove_item("Test Item", amount=80, prnt=True) == 80

def test_all():
    print("Testing adding items")
    test_add_item()
    print("Testing removing items")
    test_remove_item()