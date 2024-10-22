class Zone:
    def __init__(self, name: str, type: str, lvl: tuple, monsters: tuple) -> None:
        self.name = name

        self.type = type

        self.lvl = lvl
        self.monsters = monsters