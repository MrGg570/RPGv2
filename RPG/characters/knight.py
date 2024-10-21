from .character import Character
from RPG.utilities import inventory

class Knight(Character):
    def __init__(self, name: str) -> None:
        super().__init__(name=name, pv=100, atk=10, arm=0, lvl=1)
        self.attacks.update({'Charge':(100, 95, 'physic'),'Sword attack': (150, 80, 'physic')})
        self.isplayer = True

        self.xp = 0
        self.maxxp = 1000

        self.bag = inventory.Bag('knight')