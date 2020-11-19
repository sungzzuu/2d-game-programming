from pico2d import *
import gfw
import sun

START_POS = 125, 40
INTERVAL = 4

STATE_ON = 1
STATE_OFF = 0

class Card:
    def __init__(self, order, name):
        self.state = STATE_OFF
        if name == 'peashooter':
            self.image_name = '../res/interface/card/PeashooterSeedPacket'
            self.score = 100
        elif name == 'sunflower':
            self.image_name = '../res/interface/card/SunflowerSeedPacket'
            self.score = 50
        elif name == 'snowshooter':
            self.image_name = '../res/interface/card/SnowPeaSeedPacket'
            self.score = 175
        elif name == 'cherrybomb':
            self.image_name = '../res/interface/card/CherryBombSeedPacket'
            self.score = 150
        elif name == 'wallnut':
            self.image_name = '../res/interface/card/Wall-nutSeedPacket'
            self.score = 50
        self.image = gfw.image.load(self.image_name + '0' + '.png')
        self.pos = START_POS[0] + order * (INTERVAL + self.image.w), get_canvas_height() - START_POS[1]

    def update(self):
        if sun.sun_score >= self.score:
            self.image = gfw.image.load(self.image_name + '1' + '.png')
            self.state = STATE_OFF

    def draw(self):
        self.image.draw(*self.pos)
