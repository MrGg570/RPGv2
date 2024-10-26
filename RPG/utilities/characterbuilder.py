from RPG.characters.desert import mummy, skeleton
from RPG.characters.forest import goblin, spider
from RPG.characters.player import archer, knight, mage, warrior
from RPG.characters.special import fallenangel, souleater

class Build:
    """
    Classe utiliser pour obtenir les monstres et le joueur
    """
    def __init__(self) -> None:
        pass

    @classmethod
    def create_enemy(self, name: str = 'goblin', lvl: int = 1, enemies: int = 1, f: int = 1) -> object:
        """
        Le décorateur permet d'appeler la fonction sans instancier d'objet.
        La fonction retourne l'ennemi demandé avec le niveau précisé 
        """
        name = name.lower()
        match name:
            case 'goblin':
                return goblin.Goblin(lvl=lvl, enemies=enemies, f=f)

            case 'spider':
                return spider.Spider(lvl=lvl, enemies=enemies, f=f)
            
            case 'skeleton':
                return skeleton.Skeleton(lvl=lvl, enemies=enemies, f=f)
            
            case 'mummy':
                return mummy.Mummy(lvl=lvl, enemies=enemies, f=f)
            
            case 'soul eater':
                return souleater.Soul_eater(lvl=lvl, f=f)
            
            case 'fallen angel':
                return fallenangel.Fallen_angel(lvl=lvl, f=f)
            
            case _:
                raise Exception('Specified enemy name does not exist')

    @classmethod 
    def create_player(self, name: str = 'Player', playerclass: str = 'knight') -> object:
        """
        Permet d'instancier le joueur
        Retourne un objet joueur de la classe spécifiée
        """
        playerclass = playerclass.lower()
        match playerclass:

            case 'knight':
                return knight.Knight(name)

            case 'warrior':
                pass

            case 'mage':
                pass

            case 'archer':
                pass

            case _:
                raise Exception('Specified player class does not exist')