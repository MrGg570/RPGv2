from ..character import Character

class Soul_eater(Character):
    def __init__(self, lvl: int = 1, enemies: int = 1, f: int = 1) -> None:
        super().__init__(name='Soul eater', pv=50, atk=45, arm=0, lvl=lvl, number=enemies, f=f)
        self.attacks.update({'Earthquake':(100, 100, 'physic')})