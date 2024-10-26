from .zone import Zone

class Forest(Zone):
    """
    Permet d'instancier une zone de type 'Forêt'
    """
    def __init__(self, name: str, lvl: tuple) -> None:
        super().__init__(name, 'Forest', lvl, ('goblin', 'spider'))