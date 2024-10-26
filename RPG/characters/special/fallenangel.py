from ..character import Character

class Fallen_angel(Character):
    def __init__(self, lvl: int = 1, enemies: int = 1, f: int = 1) -> None:
        super().__init__(name='Fallen angel', pv=90, atk=35, arm=0, lvl=lvl, number=enemies, f=f)
        self.attacks.update({'Curse':(100, 100, 'magic')})