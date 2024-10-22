from .zone import Zone

class Forest(Zone):
    def __init__(self, name: str, lvl: tuple) -> None:
        super().__init__(name, 'Forest', lvl, ('goblin', 'spider'))