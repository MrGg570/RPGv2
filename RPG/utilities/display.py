from RPG.inputs import inputs

from rich.console import Console
from os import system

class Display:
    def __init__(self) -> None:
        # system('mode con: cols=2000 lines=300')
        self.get_key = lambda: inputs.Input.get_keyboard_input()
        self.wait = lambda: inputs.Input.wait_input()
        self.clear = lambda: system('cls||clear')
        self.console = Console()

    def print(self, string: str, style: str | None = None, justify: str | None = None) -> None:
        """
        Permet d'afficher du texte à l'écran
        """
        self.console.print(string, style=style, highlight=False, justify=justify)

    def menu(self, actions: list, text: str = "") -> str:

        assert actions != [] and type(actions) == list, 'Specified list of actions is not valid'

        cursor = 0
        key = None
        while key != 'enter':
            self.clear()
            self.print(text + '\n')
            cursor = cursor%len(actions)
            for i, e in enumerate(actions):
                if cursor == i:
                    self.console.print('> ' + e, justify='left')
                else:
                    self.console.print('  ' + e, justify='left')

            key = self.get_key()
            if key == 'haut':
                cursor -= 1
                if cursor<0:
                    cursor = len(actions) - 1
            elif key == 'bas':
                cursor += 1
        return actions[cursor%len(actions)]
    
    def get_healthbar(self, other: object) -> str:
        namecolor = 'green' if other.isplayer else 'bright_red'
        pvcolor = "bright_green" if other.pv > 50/100*other.maxpv else "orange3" if other.pv > 20/100*other.maxpv else "bright_red"
        bar_length = 30
        fullbarlength = round(other.pv / other.maxpv * bar_length)
        return f'[bold {namecolor}]{other.name}[/bold {namecolor}]{(25 - len(other.name)) * ' '} [gold1]Lvl. [/gold1] [green on green]{fullbarlength * ' '}[/green on green][grey19 on grey19]{(bar_length - fullbarlength) * ' '}[/grey19 on grey19] [bold {pvcolor}]{other.pv}[/bold {pvcolor}]/[bold white]{other.maxpv}[/bold white]'
    
    def get_(self, player: object, enemy: object) -> str:
        return self.get_healthbar(player) + "\n\n" + self.get_healthbar(enemy)