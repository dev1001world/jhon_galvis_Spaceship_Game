from game.components.powerup.powerup import PowerUp
from game.utils.constants import TNT, TNT_TYPE
class Tnt(PowerUp):
    def __init__(self):
        super().__init__(TNT, TNT_TYPE)