from .character import Character

class Goblin(Character):
    def __init__(self, lvl: int = 1) -> None:
        super().__init__(name='Goblin', pv=30, atk=5, arm=0, lvl=lvl)

        self.attacks.update({'Punch':(100, 90, 'physic')})