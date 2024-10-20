from RPG.utilities import characterbuilder, display, fight

class RPG:
    def __init__(self) -> None:
        self.player = characterbuilder.Build.create_player(name='MoiJeSuisLeJoueurOwO', playerclass='knight')
        self.screen = display.Display()
        self.combat = fight.Combat(player=self.player, display=self.screen)

    def titlescreen(self) -> None:
        selected = self.screen.menu(actions=['Démarrer', 'Quitter'], text=self.screen.get_title('RPG'))
        match selected:
            case 'Démarrer':
                pass

            case 'Quitter':
                self.screen.clear()
                exit(1)

    def battle(self) -> bool:
        enemiesnumber = 1
        enemies = list()
        for i in range(enemiesnumber):
            enemies.append(characterbuilder.Build.create_enemy())
        return self.combat.fight(*enemies)