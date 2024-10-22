from RPG.zones import forest, desert, jungle

class Build:
    def __init__(self) -> None:
        pass

    @classmethod
    def create_zone(self, name: str, type: str, lvl: tuple) -> object:
        type = type.lower()
        match type:
            case 'forest':
                return forest.Forest(name=name, lvl=lvl)
            case 'desert':
                return desert.Desert(name=name, lvl=lvl)
            case _:
                raise Exception(f'<{type}> is not a valid zone type')