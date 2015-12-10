import armor
import weapons


class Manager:
    def __init__(self):
        self._slots = {
            "head": None,
            "ring_1": None,
            "ring_2": None,
            "neck": None,
            "feet": None,
            "legs": None,
            "chest": None,
        }

    def equip(self, gear):
        pass

    def unequip(self, gear):
        pass

    def get_total_stats(self):
        for gear in self._slots:
            pass