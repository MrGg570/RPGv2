from RPG.game import RPG

story = RPG()

from RPG.utilities import characterbuilder, display

player = characterbuilder.Build.create_player(name='MoiJeSuisLeJoueurOwO')
enemy = characterbuilder.Build.create_enemy()
screen = display.Display()

actions = ["Attack", "Flee"]
selected = screen.menu(actions=actions, text=screen.get_(player=player, enemy=enemy))
match selected:
    case 'Attack':
        liste = list(player.attacks.keys())
        liste.append('Back')
        selected = screen.menu(actions=liste, text=screen.get_(player=player, enemy=enemy))
        if selected == "Back":
            pass
        else:
            player.attack(enemy, selected)

    case 'Flee':
        pass

screen.clear()
screen.print(screen.get_(player=player, enemy=enemy))