import tile


class Blank(tile.Tile):
    def __init__(self, blocking=False):
        tile.Tile.__init__(self, "Blank Tile")
        self.props = {
            "blocking": blocking
        }