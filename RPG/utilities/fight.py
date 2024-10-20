from random import choice

class Combat:
    def __init__(self, player: object, display: object) -> None:
        self.player = player
        self.display = display

    def fight(self, *enemies) -> str | bool:
        enemiesalive = True
        while self.player.is_alive() and enemiesalive:
            actions = ['Attack', 'Bag', 'Flee']
            selected = self.display.menu(actions=actions, text=self.display.get_multiple_healthbars(player=self.player, enemies=enemies))
            match selected:
                case 'Attack':
                    availableattacks = list(self.player.attacks.keys())
                    availableattacks.append('Back')
                    selected = self.display.menu(actions=availableattacks, text=self.display.get_multiple_healthbars(player=self.player, enemies=enemies))

                    match selected:
                        case 'Back':
                            pass
                    
                        case _:
                            if len(enemies) == 1:
                                self.display.menu(actions=['OK'], text=self.display.get_multiple_healthbars(player=self.player, enemies=enemies), info = f'Vous attaquez {enemies[0].name} avec {selected}!')
                                success = self.player.attack(enemies[0], selected)

                            else:
                                enemieslist = [e.name + ' (n°{})'.format(i+1) for i, e in enumerate(enemies)]
                                enemy = self.display.menu(actions=enemieslist, text=self.display.get_multiple_healthbars(player=self.player, enemies=enemies))
                                self.display.menu(actions=['OK'], text=self.display.get_multiple_healthbars(player=self.player, enemies=enemies), info = f'Vous attaquez {enemies[int(enemy[-2])-1].name} n°{enemy[-2]} avec {selected}!')
                                success = self.player.attack(enemies[int(enemy[-2])-1], selected)
                                    
                            if not success:
                                self.display.menu(actions=['OK'], text=self.display.get_multiple_healthbars(player=self.player, enemies=enemies), info = f'Vous ratez votre attaque!')

                case 'Bag':
                    pass

                case 'Flee':
                    pass

            number = 0
            for i, e in enumerate(enemies):
                if not e.is_alive():
                    number += 1
                else:
                    chosen = choice(list(e.attacks.keys()))
                    self.display.menu(actions = ['OK'], text = self.display.get_multiple_healthbars(player=self.player, enemies=enemies), info = f'{e.name} vous attaque avec {chosen}!' if len(enemies) == 1 else f'{e.name} n°{i+1} vous attaque avec {chosen}!')
                    if not e.attack(self.player, chosen):
                        self.display.menu(actions = ['OK'], text = self.display.get_multiple_healthbars(player=self.player, enemies=enemies), info = f'{e.name} rate son attaque!' if len(enemies) == 1 else f'{e.name} n°{i+1} rate son attaque!')
            if number == len(enemies):
                enemiesalive = False
        return self.lose(self.display.get_multiple_healthbars(player=self.player, enemies=enemies)) if enemiesalive else self.win(self.display.get_multiple_healthbars(player=self.player, enemies=enemies))
    
    def win(self, lastbar: str) -> bool:
        self.display.menu(actions = ['OK'], text = lastbar, info = 'Vous avez gagné!')

    def lose(self, lastbar: str) -> bool:
        self.display.menu(actions = ['OK'], text = lastbar, info = 'Vous avez perdu!')