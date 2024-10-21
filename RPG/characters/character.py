from random import randint

class Character:
    """
    Classe de base pour définir des personnages
    """
    def __init__(self, name:str, pv:int, atk:int, arm: int, lvl:int) -> None:
        if len(name)>25:
            raise Exception('Specified name is too long')
        self.name = name
        self.pv = pv
        self.maxpv = pv
        self.atk = atk
        self.arm = arm

        self.lvl = lvl

        self.isplayer = False

        self.attacks = dict()

    def attack(self, other: object, attack: str) -> bool:
        if randint(0,100) > self.attacks[attack][1]:
            return False
        else:
            damage = (self.atk*(self.attacks[attack][0]/100))
            other.pv -= round(damage - damage * (other.arm/100))
            if other.pv < 0:
                other.pv = 0 
            return True

    def is_alive(self) -> bool:
        """
        Permet de savoir si le personnage est encore en vie
        Retourne un booléen: True si le personnage est vie, sinon False
        """
        return self.pv > 0