from .zone import Zone

class Desert(Zone):
    """
    Permet d'instancier une zone de type 'Desert'
    """
    def __init__(self, name: str, lvl: tuple) -> None:
        super().__init__(name, 'Desert', lvl, ('skeleton', 'mummy'))