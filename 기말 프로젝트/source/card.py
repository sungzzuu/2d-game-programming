from pico2d import *
import gfw

START_POS = 125, 40
INTERVAL = 4

class Card:
    def __init__(self, order, name):
        if name == 'peashooter':
            image_name = '../res/interface/card/PeashooterSeedPacket0.png'
        elif name == 'sunflower':
            image_name = '../res/interface/card/SunflowerSeedPacket0.png'
        elif name == 'snowshooter':
            image_name = '../res/interface/card/SnowPeaSeedPacket0.png'
        elif name == 'cherrybomb':
            image_name = '../res/interface/card/CherryBombSeedPacket0.png'
        elif name == 'wallnut':
            image_name = '../res/interface/card/Wall-nutSeedPacket0.png'
        self.image = gfw.image.load(image_name)
        self.pos = START_POS[0] + order * (INTERVAL + self.image.w), get_canvas_height() - START_POS[1]

    def update(self):
        pass
    def draw(self):
        self.image.draw(*self.pos)
