from time import sleep

from RPG.utilities import characterbuilder, display, fight

class RPG:
    def __init__(self) -> None:
        self.screen = display.Display()

        selected = self.screen.menu(actions=['Démarrer', 'Quitter'], text=self.screen.get_title('RPG'))
        match selected:
            case 'Démarrer':
                pass

            case 'Quitter':
                self.screen.clear()
                exit(1)
        validname = False

        input()

        while not validname:
            self.tell("What's your name, adventurer?\n", style='bold gold1')
            name = input('>>> ')
            if len(name)>25:
                self.tell("Oh... I'm afraid that name is too long... Could you try another one?", style='bold gold1')
            elif name == '':
                self.tell("Oh... I'm afraid that name will not work... Could you try another one?", style='bold gold1')
            else:
                validname = True

        self.tell(f"So your name is {name}... And what class do you belong to?", style='bold gold1')
        self.player = characterbuilder.Build.create_player(name=name, playerclass=self.screen.menu(actions=['Knight'], text=f"[bold gold1]So your name is {name}... And what class do you belong to?[/bold gold1]\n"))

        self.combat = fight.Combat(player=self.player, display=self.screen)
            
    def tell(self, string: str, style: str | None = None) -> None:
        fragment = ''
        slowdown = (',','.', '?', '!')
        closing = False
        for i in string:
            if i != "[" and not closing:
                fragment += i
                self.screen.clear()
                # for j in previouslines:
                #     self.screen.print(j, "bold white", justify="center")
                self.screen.print(fragment, style=style)
                sleep(0.05 if i not in slowdown else 0.3)
            else:
                fragment +=i               
                closing = True if i != "]" else False


    def battle(self) -> bool:
        enemiesnumber = 1
        enemies = list()
        for i in range(enemiesnumber):
            enemies.append(characterbuilder.Build.create_enemy())
        return self.combat.fight(*enemies)