from .character import Character

class Spider(Character):
    def __init__(self, lvl: int = 1) -> None:
        super().__init__(name='Spider', pv=20, atk=15, arm=0, lvl=lvl)

        self.attacks.update({'Spider web':(50, 100, 'physic')})