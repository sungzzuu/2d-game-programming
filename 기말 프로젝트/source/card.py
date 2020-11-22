from pico2d import *
import gfw
import sun
import gobj
from plant import Plant

START_POS = 125, 40
INTERVAL = 4

STATE_ON = 1
STATE_OFF = 0

class Card:
    WIDTH, HEIGHT = 50, 70
    def __init__(self, order, name):
        self.state = STATE_OFF
        self.name = name
        if name == 'Peashooter':
            self.image_name = '../res/interface/card/PeashooterSeedPacket'
            self.score = 100
        elif name == 'SunFlower':
            self.image_name = '../res/interface/card/SunflowerSeedPacket'
            self.score = 50
        elif name == 'SnowPea':
            self.image_name = '../res/interface/card/SnowPeaSeedPacket'
            self.score = 175
        elif name == 'CherryBomb':
            self.image_name = '../res/interface/card/CherryBombSeedPacket'
            self.score = 150
        elif name == 'WallNut':
            self.image_name = '../res/interface/card/Wall-nutSeedPacket'
            self.score = 50
        self.image = gfw.image.load(self.image_name + '0' + '.png')
        self.pos = START_POS[0] + order * (INTERVAL + self.image.w), get_canvas_height() - START_POS[1]

    def update(self):
        if sun.sun_score >= self.score:
            self.image = gfw.image.load(self.image_name + '1' + '.png')
            self.state = STATE_ON
        else:
            self.image = gfw.image.load(self.image_name + '0' + '.png')
            self.state = STATE_OFF


    def draw(self):
        self.image.draw(*self.pos)

    def handle_event(self, e):
        if self.state != STATE_ON or sun.sun_score < self.score:
            return
        if e.type == SDL_MOUSEBUTTONDOWN and e.button == SDL_BUTTON_LEFT:
            pos = gobj.mouse_xy(e)
            if gobj.pt_in_rect(pos, self.get_bb()):
                # 식물 추가하기
                m = Plant((e.x, get_canvas_height() - e.y), self.name)
                gfw.world.add(gfw.layer.plant, m)
                sun.sun_score -= self.score
                return True
        return False

    def get_bb(self):
        hw = Card.WIDTH // 2
        hh = Card.HEIGHT // 2
        x, y = self.pos
        return x - hw, y - hh, x + hw, y + hh

    def remove(self):
        gfw.world.remove(self)