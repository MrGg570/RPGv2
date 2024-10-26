from random import randint, uniform

class Character:
    """
    Classe de base pour définir des personnages
    """
    def __init__(self, name:str, pv:int, atk:int, arm: int, lvl:int, number: int = 1, f:int = 1) -> None:
        if len(name)>25:
            raise Exception('Specified name is too long')
        
        self.lvl = lvl
            
        self.name = name

        self.f = f # Facteur de difficulté, f < 1 difficulté réduite, f > 1 augmentation de la difficulté
        self.pv = round((self.calc_stat(pv, 'pv') * self.f) / number)

        self.maxpv = self.pv
        self.atk = atk
        self.arm = arm

        self.isplayer = False

        self.attacks = dict()

    def calc_stat(self, base: int, stat: str = 'atk') -> int:
        """
        Permet de calculer les statistiques selon le niveau à partir des statistiques de base (modèle exponentiel)
        """
        match stat:
            case 'atk':
                r = .05 # Modifier la vitesse de la croissance exponentielle
                return round(base * (1 + r) ** (self.lvl - 1))
            
            case 'pv':
                r = .05
                return round(base * self.f * (1 + r) ** (self.lvl - 1))

        
    def attack(self, other: 'Character', attack: str) -> bool:
        """
        Permet de gérer une attaque d'un personnage sur un autre
        """
        if randint(0,100) > self.attacks[attack][1]:
            return False
        else:
            attackvalue = (self.calc_stat(self.atk, 'atk') * (self.attacks[attack][0]/100)) * (1 + uniform(-0.1, 0.1)) * 0.5

            other.pv -= round(max(0, attackvalue - attackvalue * (other.arm / 100)))
            if other.pv < 0:
                other.pv = 0 
            return True

    def is_alive(self) -> bool:
        """
        Permet de savoir si le personnage est encore en vie
        Retourne un booléen: True si le personnage est vie, sinon False
        """
        return self.pv > 0