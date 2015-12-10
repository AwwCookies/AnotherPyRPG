import experience
import pool
import inventory
import location
import gear


class Player:
    def __init__(self):
        self.level = experience.Manager()
        self.health = pool.Pool()
        self.location = location.Manager()
        self.inventory = inventory.Inventory()
        self.stats = None
        self.mana = pool.Pool()
        self.spellbox = None
        self.gear = gear.Manager()

    def use_item(self, item_name):
        """
        :param item_name: Item Name
        :return: True if player used item and False is they did not.
        """
        if self.inventory.amount_of(item_name):
            if self.inventory[item_name]["item"].props.get("useable"):
                return True
            else:
                print("%s is not a useable item." % item_name)
        else:
            print("You do not have any %s" % item_name)
        return False
