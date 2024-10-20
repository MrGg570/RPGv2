from .character import Character

class Goblin(Character):
    def __init__(self) -> None:
        super().__init__('Goblin', 30, 5)
        self.attacks.update({'Punch':(100, 90, 'physic')})