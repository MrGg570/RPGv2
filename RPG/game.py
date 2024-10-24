from time import sleep

from RPG.utilities import characterbuilder, display, fight, zonebuilder
from random import randint, choice

class RPG:
    def __init__(self, skipintro: bool = False) -> None:
        self.screen = display.Display()

        self.region = list()
        zonetype = ('forest', 'desert')
        zonename = {
            'forest': ['Deep forest', 'Scary forest', 'Death forest', 'Spooky forest', 'Unpleasant forest'],
            'desert': ['Dry desert', 'Creepy desert', 'Torrid desert', 'Burning desert', 'Unpleasant desert'] 
                    }
        for i in range(5):
            chosentype = choice(zonetype)
            self.region.append(zonebuilder.Build.create_zone(name=choice(zonename[chosentype]), type=chosentype, lvl=(i*10+1, i*10+10)))
            zonename[chosentype].pop(zonename[chosentype].index(self.region[-1].name)) # Pour que chaque zone ai un nom différent
        # self.region.append(boss)
        self.currentzone = self.region[0]

        self.quests = {1:['Vaincre 10 ennemies', 0, 10, 'kill'], 2: ['Infliger 500 points de dégat', 0, 500, 'dmg']}

        start = False
        while not start:
            selected = self.screen.menu(actions=['Démarrer', 'Options', 'Quitter'], text=self.screen.get_title('RPG'))
            match selected:
                case 'Démarrer':
                    start = True

                case 'Options':
                    selected =self.screen.menu(actions=[f'Skip intro : {skipintro}', 'Langue : ', 'Retour'], text=self.screen.get_title('RPG'))
                    match selected:
                        case 'Skip intro : True':
                            skipintro = False
                        case 'Skip intro : False':
                            skipintro = True
                        
                        case _:
                            pass

                case 'Quitter':
                    self.screen.clear()
                    exit(1)

        if skipintro:
            self.player = characterbuilder.Build.create_player(name='ImThePlayerOwO')

            self.combat = fight.Combat(player=self.player, display=self.screen)

            return None
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

        self.tell(f'Seems like you have awaken in a {self.currentzone.type}...', style='bold gold1')

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


    def battle(self) -> tuple:
        enemiesnumber = randint(1, 3)
        enemies = list()
        for i in range(enemiesnumber):
            enemies.append(characterbuilder.Build.create_enemy(name=self.get_enemy(), lvl=self.get_level()))
        return self.combat.fight(*enemies)
    
    def get_enemy(self) -> str:
        return choice(self.currentzone.monsters)
    
    def get_level(self) -> int:
        if self.currentzone.lvl[0] > self.player.lvl:
            return randint(self.currentzone.lvl[0], self.currentzone.lvl[0]+4)
        chosenlvl = 100
        while chosenlvl > self.player.lvl+1:
            chosenlvl = randint(*self.currentzone.lvl)
        return chosenlvl
    
    def global_menu(self):
        selected = self.screen.menu(actions=['Combattre', 'Sac', 'Boutique', 'Eglise', 'Carte', 'Quêtes'], text=self.screen.get_title('MENU'))

        match selected:
            case 'Combattre':
                result,  data = self.battle()
                if result == 'flee':
                    self.tell('Vous fuyez le combat...')
                    self.screen.menu(actions=['OK'], text='Vous fuyez le combat...')
                elif result:
                    pass
                else:
                    self.respawn()
                self.update_quests(data)

            case 'Sac':
                pass

            case 'Boutique':
                pass

            case 'Eglise':
                self.eglise()

            case 'Carte':
                actions = ['Zone suivante', 'Retour'] if self.currentzone == self.region[0] else ['Zone précédente', 'Retour'] if self.currentzone == self.region[-1] else ['Zone suivante', 'Zone précédente', 'Retour']
                selected = self.screen.menu(actions=actions, text=self.screen.get_map(self.region, self.currentzone))
                match selected:
                    case 'Zone suivante':
                        if self.is_quest_done(self.quests[self.region.index(self.currentzone)+1]):
                            self.currentzone = self.region[self.region.index(self.currentzone)+1]
                            self.screen.menu(actions=['OK'], text=self.screen.get_map(self.region, self.currentzone), info=f'Vous entrez dans {self.currentzone.name}')
                        else: 
                             self.screen.menu(actions=['OK'], text=self.screen.get_map(self.region, self.currentzone), info=f"[bold bright_red]Vous devez d'abord terminer la quête {self.region.index(self.currentzone)+1}: {self.quests[self.region.index(self.currentzone)+1][0]}")

                    case 'Zone précédente':
                        self.currentzone = self.region[self.region.index(self.currentzone)-1]
                        self.screen.menu(actions=['OK'], text=self.screen.get_map(self.region, self.currentzone), info=f'Vous entrez dans {self.currentzone.name}')

                    case _:
                        pass

            case 'Quêtes':
                self.screen.menu(actions=['OK'], text=self.screen.get_quests(self.quests))

    def is_quest_done(self, quest: list) -> bool:
        return quest[1] >= quest[2]
    
    def update_quests(self, data: tuple):
        kills, dmg = data
        for quest in self.quests.keys():
            if self.quests[quest][3] == 'kill':
                self.quests[quest][1] += kills
            elif self.quests[quest][3] == 'dmg':
                self.quests[quest][1] += dmg

    def eglise(self) -> None:
        self.tell(string="Vous vous rendez à l'église pour prier...")
        self.screen.menu(actions=['OK'], text='Vos [bold green]PV[/bold green] ont été restaurés!')
        self.player.pv = self.player.maxpv

    def respawn(self) -> None:
        pass