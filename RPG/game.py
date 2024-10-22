from time import sleep

from RPG.utilities import characterbuilder, display, fight, zonebuilder
from random import randint, choice

class RPG:
    def __init__(self, skipintro: bool) -> None:
        self.screen = display.Display()

        self.region = list()
        zonetype = ('forest', 'forest')
        zonename = {'forest':['Deep forest', 'Scary forest', 'Death forest', 'Spooky forest', 'Unpleasant forest']}
        for i in range(5):
            chosentype = choice(zonetype)
            self.region.append(zonebuilder.Build.create_zone(name=choice(zonename[chosentype]), type=chosentype, lvl=(i*10, i*10+10)))
            zonename[chosentype].pop(zonename[chosentype].index(self.region[-1].name)) # Pour que chaque zone ai un nom différent
        # self.region.append(boss)
        self.currentzone = self.region[0]

        if skipintro:
            self.player = characterbuilder.Build.create_player(name='ImThePlayerOwO')

            self.combat = fight.Combat(player=self.player, display=self.screen)

            self.currentzone = zonebuilder.Build.create_zone(name='Starter forest', type='forest', lvl=(1, 10))

            return None

        selected = self.screen.menu(actions=['Démarrer', 'Quitter'], text=self.screen.get_title('RPG'))
        match selected:
            case 'Démarrer':
                pass

            case 'Quitter':
                self.screen.clear()
                exit(1)
        validname = False

        while not validname:
            self.tell("What's your name, adventurer?\n", style='bold gold1')
            name = input('>>> ')
            if len(name)>25:
                self.tell("Oh... I'm afraid that name is too long... Could you try another one?", style='bold gold1')
                self.screen.menu(actions=['OK'], text="[bold gold1]Oh... I'm afraid that name is too long... Could you try another one?[/bold gold1]")
            elif name == '':
                self.tell("Oh... I'm afraid that name will not work... Could you try another one?", style='bold gold1')
                self.screen.menu(actions=['OK'], text="[bold gold1]Oh... I'm afraid that name will not work... Could you try another one?[/bold gold1]")
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
        enemiesnumber = randint(1, 3)
        enemies = list()
        for i in range(enemiesnumber):
            enemies.append(characterbuilder.Build.create_enemy(name=self.get_enemy(), lvl=self.get_level()))
        return self.combat.fight(*enemies)
    
    def get_enemy(self) -> str:
        return choice(self.currentzone.monsters)
    
    def get_level(self) -> int:
        chosenlvl = 100
        while chosenlvl > self.player.lvl+1:
            chosenlvl = randint(*self.currentzone.lvl)
        return chosenlvl