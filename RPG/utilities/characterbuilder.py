from RPG.characters import archer, knight, mage, warrior
from RPG.characters import goblin, spider

class Build:
    """
    Classe utiliser pour obtinir les monstres et le joueur
    """
    def __init__(self) -> None:
        pass

    @classmethod
    def create_enemy(self, name: str = 'goblin', lvl: int = 1) -> object:
        """
        Le décorateur permet d'appeler la fonction sans instancier d'objet.
        La fonction retourne le personnage demandé avec le niveau précisé 
        """
        name = name.lower()
        match name:
            case 'goblin':
                return goblin.Goblin(lvl=lvl)

            case 'spider':
                return spider.Spider(lvl=lvl)
            
            case _:
                raise Exception('Specified enemy name does not exist')

    @classmethod 
    def create_player(self, name: str = 'Player', playerclass: str = 'knight') -> object:
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