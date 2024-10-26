from random import choice

class Combat:
    """
    Classe qui permet de gérer les combats
    """
    def __init__(self, player: object, display: object) -> None:
        self.player = player
        self.display = display

    def fight(self, *enemies: object) ->  tuple:
        """
        Gère un combat entre le joueur et les ennemies donnés en arguments
        """
        enemiesalive = True
        slayer = enemies[0]
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
                                enemieslist = list()
                                for i, e in enumerate(enemies):
                                    if e.is_alive():
                                        enemieslist.append(e.name + ' ({})'.format(i+1))
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
                    backed = True

                case 'Flee':
                    return 'flee', self.get_battle_data(enemies=enemies)

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
                        elif not self.player.is_alive():
                            slayer = e
                if number == len(enemies):
                    enemiesalive = False
        result = self.lose(self.display.get_multiple_healthbars(player=self.player, enemies=enemies), slayer) if enemiesalive else self.win(self.display.get_multiple_healthbars(player=self.player, enemies=enemies), enemies)
        return result, self.get_battle_data(enemies=enemies)
    
    def win(self, lastbar: str, enemies) -> bool:
        """
        Appelé quand le joueur gagne un combat, permet de calculer les récompenses
        """
        self.display.menu(actions = ['OK'], text = lastbar, info = ':tada: Vous avez gagné le combat!')

        exp = 0
        gold = 0

        for i in enemies:
            if i.name in ('Fallen angel', 'Soul eater'):
                exp += i.lvl * 300
            else:
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
        
        return True

    def lose(self, lastbar: str, slayer: object) -> bool:
        """
        Appelé quand le joueur meurt
        """
        self.display.menu(actions = ['OK'], text = lastbar, info = f':skull: Vous avez été terrassé par {slayer.name} Lvl. {slayer.lvl}!')
        return False

    def get_battle_data(self, enemies: tuple) -> tuple:
        """
        A la fin du combat, calcule les dégats et le nombre d'ennemies tués et renvoi les valeurs
        """
        kills = 0
        dmg = 0
        for i in enemies:
            if not i.is_alive():
                kills += 1
                dmg += i.maxpv
            else:
                dmg += i.maxpv - i.pv
        return kills, dmg