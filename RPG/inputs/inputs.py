from keyboard import is_pressed
from time import sleep

class Input:
    def __init__(self) -> None:
        pass

    @classmethod
    def get_keyboard_input(self) -> str:
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
        wait = True if self.get_keyboard_input() != 'enter' else False
        while wait:
                    wait = True if self.get_keyboard_input() != 'enter' else False