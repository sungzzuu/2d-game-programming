from pico2d import *
import gfw

MOVE_PPS = 500

class Bullet:
    def __init__(self, pos, type):
        self.pos = pos[0], pos[1] + 20
        self.type = type
        if self.type == 'snow':
            self.image = gfw.image.load('../res/plants/bullet/PeaIce.png')
        else:
            self.image = gfw.image.load('../res/plants/bullet/PeaNormal.png')

        self.bb_l = -self.image.w
        self.bb_b = -self.image.h
        self.bb_r = get_canvas_width() + self.image.w
        self.bb_t = get_canvas_height() + self.image.h

    def update(self):
        x, y = self.pos
        x += MOVE_PPS * gfw.delta_time
        self.pos = x, y
        # 화면 밖 미사일 삭제
        if self.out_of_screen():
            gfw.world.remove(self)

    def out_of_screen(self):
        x, y = self.pos
        if x < self.bb_l: return True
        if x > self.bb_r: return True
        if y < self.bb_b: return True
        if y > self.bb_t: return True


    def draw(self):
        self.image.draw(*self.pos)

