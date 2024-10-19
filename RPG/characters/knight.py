from .character import Character

class Knight(Character):
    def __init__(self, name: str) -> None:
        super().__init__(name, 100, 10)
        self.attacks.update({'Charge':(100, 95, 'physic'),'Sword attack': (150, 90, 'physic')})
        self.isplayer = True