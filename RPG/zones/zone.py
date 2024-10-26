class Zone:
    """
    Classe mère pour instancier des zones
    """
    def __init__(self, name: str, type: str, lvl: tuple, monsters: tuple) -> None:
        self.name = name

        self.type = type

        self.lvl = lvl
        self.monsters = monsters