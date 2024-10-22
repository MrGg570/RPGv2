from .character import Character

class Skeleton(Character):
    def __init__(self, lvl: int = 1) -> None:
        super().__init__(name='Skeleton', pv=30, atk=10, arm=0, lvl=lvl)

        self.attacks.update({'Bone throw':(100, 90, 'physic')})