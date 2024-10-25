from ..character import Character

class Mummy(Character):
    def __init__(self, lvl: int = 1, enemies: int = 1, f: int = 1) -> None:
        super().__init__(name='Mummy', pv=50, atk=round((50/enemies)*f), arm=0, lvl=lvl, number=enemies, f=f)

        self.attacks.update({'Bandage attack':(100, 80, 'physic')})