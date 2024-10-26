from keyboard import is_pressed
from time import sleep

class Input:
    """
    Classe qui gère les appuis sur le clavier
    """
    def __init__(self) -> None:
        pass

    @classmethod
    def get_keyboard_input(self) -> str:
        """
        Retourne la première touche pressée parmis flèche du haut, du bas et entrer
        """
        while is_pressed('haut') or is_pressed('bas') or is_pressed('enter'):
            sleep(0.05)
        input = False
        while not input:
            if is_pressed('haut'):
                input = 'haut'
            elif is_pressed('bas'):
                input = 'bas'
            elif is_pressed('enter'):
                input = 'enter'
        return input
    
    @classmethod
    def wait_input(self) -> None:
        """
        Permet d'attendre jusqu'à ce que la touche entrer soit pressée
        """
        wait = True if self.get_keyboard_input() != 'enter' else False
        while wait:
                    wait = True if self.get_keyboard_input() != 'enter' else False