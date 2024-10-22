from .zone import Zone

class Desert(Zone):
    def __init__(self, name: str, lvl: tuple) -> None:
        super().__init__(name, 'Desert', lvl, ('skeleton', 'mummy'))