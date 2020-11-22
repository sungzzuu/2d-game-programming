from pico2d import *
import gfw
import gobj
import random

MOVE_PPS = 100

# x 값 랜덤하게 100 ~ 700 사이 y 값은 캔버스 사이즈만큼부터 -=
STATE_ARRIVED = 1
STATE_MOVING = 0
STATE_SCORED = 2
SUN_SCORE = 25
sun_score = 0
TARGET_X = 64
TARGET_Y = 30


class Sun:
    WIDTH, HEIGHT = 80, 80
    def __init__(self, pos, target):
        self.state = STATE_MOVING
        self.pos = pos
        self.target = target
        self.image = gfw.image.load('../res/interface/Sun.png')
        self.dir = 0, 0

    def update(self):
        global sun_score
        if self.state == STATE_SCORED:
            x, y = self.pos
            dirX, dirY = self.dir
            x += dirX * gfw.delta_time
            y += dirY * gfw.delta_time
            self.pos = x, y
            if x < TARGET_X:
                self.remove()
                sun_score += SUN_SCORE
                return

        elif self.state == STATE_MOVING:
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

    def handle_event(self, e):
        global sun_score
        if self.state != STATE_ARRIVED:
            return
        if e.type == SDL_MOUSEBUTTONDOWN and e.button == SDL_BUTTON_LEFT:
            pos = gobj.mouse_xy(e)
            if gobj.pt_in_rect(pos, self.get_bb()):
                self.state = STATE_SCORED

                # 이동할 햇살 위치
                x, y = self.pos
                targetY = get_canvas_height() - TARGET_Y
                self.dir = TARGET_X - x, targetY - y
                return True
        return False

    def get_bb(self):
        hw = Sun.WIDTH // 2
        hh = Sun.HEIGHT // 2
        x, y = self.pos
        return x - hw, y - hh, x + hw, y + hh

    def remove(self):
        gfw.world.remove(self)


