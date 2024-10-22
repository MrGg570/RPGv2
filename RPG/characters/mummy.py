from .character import Character

class Mummy(Character):
    def __init__(self, lvl: int = 1) -> None:
        super().__init__(name='Mummy', pv=5, atk=20, arm=0, lvl=lvl)

        self.attacks.update({'Bandage attack':(100, 80, 'physic')})