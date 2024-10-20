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

    def menu(self, actions: list, text: str | None = None, info: str | None = None) -> str:

        assert actions != [] and type(actions) == list, 'Specified list of actions is not valid'

        cursor = 0
        key = None
        while key != 'enter':
            self.clear()
            if text != None:
                self.print(text)
            if info != None:
                self.print(info)
            cursor = cursor%len(actions)
            for i, e in enumerate(actions):
                if cursor == i:
                    self.console.print('\u2192 ' + e, justify='left')
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
    
    def get_healthbar(self, other: object, number: int | None = None) -> str:
        namecolor = 'green' if other.isplayer else 'bright_red'
        pvcolor = "bright_green" if other.pv > 50/100*other.maxpv else "orange3" if other.pv > 20/100*other.maxpv else "bright_red"
        bar_length = 30
        fullbarlength = round(other.pv / other.maxpv * bar_length)
        return f'[bold {namecolor}]{other.name}[/bold {namecolor}] {f'n°{number+1}' if number != None else ''} {(22 - len(other.name)) * ' ' if number != None else (25 - len(other.name)) * ' '} [gold1]Lvl. [/gold1] [green on green]{fullbarlength * ' '}[/green on green][grey19 on grey19]{(bar_length - fullbarlength) * ' '}[/grey19 on grey19] [bold {pvcolor}]{other.pv}[/bold {pvcolor}]/[bold white]{other.maxpv}[/bold white]'
    
    def get_multiple_healthbars(self, player: object, enemies: tuple) -> str:
        string = self.get_healthbar(player) + "\n\n"
        for i, e in enumerate(enemies):
            string += self.get_healthbar(e, i if len(enemies)>1 else None) + "\n\n"
        return  string
    
    def get_title(self, title: str) -> str:
        horizontalch = "\u2500"
        maintitle = "\u250c"
        for i in range(len(title)+4):
            maintitle += horizontalch
        maintitle += "\u2510\n"
        maintitle += "\u2502  "
        maintitle += title
        maintitle += "  \u2502\n"
        maintitle += "\u2514"
        for i in range(len(title)+4):
            maintitle += horizontalch
        maintitle += "\u2518\n"
        return maintitle
    