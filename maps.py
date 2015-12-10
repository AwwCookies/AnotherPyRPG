import os
import json

from tiles.tile import Tile
from tiles.blank import Blank
from anotherpyrpg import settings


class Map:
    def __init__(self, name):
        self.name = name
        self.map = {}
        if os.path.exists("./maps/%s.json" % name):
            self.map = self.parse_map(json.load(open("./maps/%s.json" % name)))
            if settings.get("debug"):
                print("Created new map from ./maps/%s.json" % (name))

    def parse_map(self, map_data):
        map = {}
        for coord in map_data:
            if map_data[coord]["type"] == "Blank":
                map[coord] = Blank(blocking=map_data[coord]["blocking"])
        return map

    def get_tile(self, x, y):
        print(self.map)
        return self.map.get("%i,%i" % (x, y))

    def remove_tile(self, x, y):
        pass

    def run_tile(self, x, y):
        pass

    def save(self):
        pass

