from random import choice

class Combat:
    def __init__(self, player: object, display: object) -> None:
        self.player = player
        self.display = display

    def fight(self, *enemies) -> str | bool:
        enemiesalive = True
        while self.player.is_alive() and enemiesalive:
            backed = False
            actions = ['Attack', 'Bag', 'Flee']
            selected = self.display.menu(actions=actions, text=self.display.get_multiple_healthbars(player=self.player, enemies=enemies))
            match selected:
                case 'Attack':
                    availableattacks = list(self.player.attacks.keys())
                    availableattacks.append('Back')
                    selected = self.display.menu(actions=availableattacks, text=self.display.get_multiple_healthbars(player=self.player, enemies=enemies))

                    match selected:
                        case 'Back':
                            backed = True
                    
                        case _:
                            if len(enemies) == 1:
                                self.display.menu(actions=['OK'], text=self.display.get_multiple_healthbars(player=self.player, enemies=enemies), info = f'Vous attaquez {enemies[0].name} avec {selected}!')
                                success = self.player.attack(enemies[0], selected)

                            else:
                                enemieslist = [e.name + ' ({})'.format(i+1) if e.is_alive() else None for i, e in enumerate(enemies)]
                                for i in enemieslist:
                                    if i == None:
                                        enemieslist.pop(enemieslist.index(i))
                                enemieslist.append('Cancel')
                                enemy = self.display.menu(actions=enemieslist, text=self.display.get_multiple_healthbars(player=self.player, enemies=enemies))
                                if enemy != 'Cancel':
                                    self.display.menu(actions=['OK'], text=self.display.get_multiple_healthbars(player=self.player, enemies=enemies), info = f'Vous attaquez {enemies[int(enemy[-2])-1].name} ({enemy[-2]}) avec {selected}!')
                                    success = self.player.attack(enemies[int(enemy[-2])-1], selected)
                                
                                else:
                                    backed = True
                                    success = True
                                    
                            if not success:
                                self.display.menu(actions=['OK'], text=self.display.get_multiple_healthbars(player=self.player, enemies=enemies), info = f'Vous ratez votre attaque!')

                case 'Bag':
                    pass

                case 'Flee':
                    pass

            if not backed:
                number = 0
                for i, e in enumerate(enemies):
                    if not e.is_alive():
                        number += 1
                    elif self.player.is_alive():
                        chosen = choice(list(e.attacks.keys()))
                        self.display.menu(actions = ['OK'], text = self.display.get_multiple_healthbars(player=self.player, enemies=enemies), info = f'{e.name} vous attaque avec {chosen}!' if len(enemies) == 1 else f'{e.name} ({i+1}) vous attaque avec {chosen}!')
                        if not e.attack(self.player, chosen):
                            self.display.menu(actions = ['OK'], text = self.display.get_multiple_healthbars(player=self.player, enemies=enemies), info = f'{e.name} rate son attaque!' if len(enemies) == 1 else f'{e.name} ({i+1}) rate son attaque!')
                    else:
                        slayer = e
                if number == len(enemies):
                    enemiesalive = False
        return self.lose(self.display.get_multiple_healthbars(player=self.player, enemies=enemies), slayer) if enemiesalive else self.win(self.display.get_multiple_healthbars(player=self.player, enemies=enemies), enemies)
    
    def win(self, lastbar: str, enemies) -> bool:
        self.display.menu(actions = ['OK'], text = lastbar, info = ':tada: Vous avez gagné le combat!')

        exp = 0
        gold = 0

        for i in enemies:
            exp += i.lvl * 100

        self.display.menu(actions = ['OK'], text = lastbar, info = f':sparkles: [green]Vous[/green] [bold]gagnez[/bold] [bold gold1]{exp} XP[/bold gold1] :sparkler:!')
        self.player.xp += exp
        self.display.menu(actions = ['OK'], text = lastbar, info = self.display.get_xpbar(self.player) + '\n')

        self.player.xp += exp
        while self.player.maxxp <= self.player.xp:
            self.display.menu(actions = ['OK'], text = lastbar, info = f'Vous passez niveau {self.player.lvl + 1}!')
            self.player.lvl += 1
            self.player.xp -= self.player.maxxp
            self.display.menu(actions = ['OK'], text = lastbar, info = self.display.get_xpbar(self.player) + '\n')




    def lose(self, lastbar: str, slayer: object) -> bool:
        self.display.menu(actions = ['OK'], text = lastbar, info = f':skull: Vous avez été terrassé par {slayer.name} Lvl. {slayer.lvl}!')