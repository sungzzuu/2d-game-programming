from pico2d import *
import gfw

# 자동차와 좀비 충돌 시 좀비 자동차 모두 삭제하는데 자동차는 달려나가면서 삭제됨
# 자동차 모두 삭제 시 게임 오버



class Car:
    bb_WIDTH = 70
    bb_HEIGHT = 50
    def __init__(self, pos):
        self. pos = pos
        self.image = gfw.image.load('../res/interface/LawnCleaner.png')
        self.speed = 0

    def update(self):
        x, y = self.pos
        x -= self.speed * gfw.delta_time
        self.pos = x, y
        if x < - Car.bb_WIDTH // 2:
            self.remove()

    def draw(self):
        self.image.draw(*self.pos)

    def get_bb(self):
        l = -Car.bb_WIDTH // 2
        b = -Car.bb_HEIGHT // 2
        r = Car.bb_WIDTH // 2
        t = Car.bb_HEIGHT // 2
        x, y = self.pos
        return x + l, y + b, x + r, y + t

    def remove(self):
        gfw.world.remove(self)

    def collision_event(self):
        self.speed = 100