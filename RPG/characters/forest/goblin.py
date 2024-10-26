from ..character import Character

class Goblin(Character):
    def __init__(self, lvl: int = 1, enemies: int = 1, f: int = 1) -> None:
        super().__init__(name='Goblin', pv=50, atk=round((50/enemies)*f), arm=0, lvl=lvl, number=enemies, f=f)
        self.attacks.update({'Punch':(100, 90, 'physic')})