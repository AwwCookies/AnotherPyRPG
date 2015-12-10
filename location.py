class Manager:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.map = None
        self.last = None

    def go_up(self):
        tile = self.map.get_tile(self.x, self.y - 1)
        if tile and not tile.props.get("blocking"):
            self.y -= 1
        else:
            print("You can not go that way.")

    def go_down(self):
        tile = self.map.get_tile(self.x, self.y + 1)
        if tile and not tile.props.get("blocking"):
            self.y += 1
        else:
            print("You can not go that way.")
            print(tile)

    def go_right(self):
        tile = self.map.get_tile(self.x + 1, self.y)
        if tile and not tile.props.get("blocking"):
            self.x += 1
        else:
            print("You can not go that way.")

    def go_left(self):
        tile = self.map.get_tile(self.x - 1, self.y)
        if tile and not tile.props.get("blocking"):
            self.x -= 1
        else:
            print("You can not go that way.")