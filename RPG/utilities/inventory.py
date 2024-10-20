class Bag:
    def __init__(self, playerclass: str) -> None:
        starterbag = {'knight':{}}
        self.items = starterbag[playerclass]