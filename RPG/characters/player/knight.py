from ..character import Character
from RPG.utilities import inventory

class Knight(Character):
    def __init__(self, name: str) -> None:
        self.basepv = 100
        super().__init__(name=name, pv=self.basepv, atk=75, arm=0, lvl=1)
        self.attacks.update({'Charge':(100, 95, 'physic'),'Sword attack': (150, 80, 'physic')})
        self.isplayer = True

        self.xp = 0
        self.maxxp = 1000

        self.bag = inventory.Bag('knight')