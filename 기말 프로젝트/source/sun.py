from pico2d import *
import gfw
import random

MOVE_PPS = 50

# x 값 랜덤하게 100 ~ 700 사이 y 값은 캔버스 사이즈만큼부터 -=
STATE_ARRIVED = 1
STATE_MOVING = 0
class Sun:
    def __init__(self, pos, target):
        self.state = STATE_MOVING
        self.pos = pos
        self.target = target
        self.image = gfw.image.load('../res/interface/Sun.png')

    def update(self):
        if self.state == STATE_MOVING:
            x, y = self.pos
            y -= MOVE_PPS * gfw.delta_time
            self.pos = x, y
            # 타겟보다 y가 작아지면
            targetX, targetY = self.target
            if y < targetY:
                y = targetY
                self.pos = x, y
                self.state = STATE_ARRIVED

    def draw(self):
        self.image.draw(*self.pos)


