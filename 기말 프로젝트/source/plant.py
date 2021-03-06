from pico2d import *
import gfw
import gobj
from sun import Sun
from bullet import Bullet
from collision import check_collision_cherrybomb

STATE_NEW = 0
STATE_MOUNT = 1
COLLISION_TIME = 0.3
class Plant:
    PLANT_TYPE = ['SunFlower', 'Peashooter', 'SnowPea', 'WallNut', 'CherryBomb']

    images = {}
    bb_WIDTH, bb_HEIGHT = 20, 70
    def __init__(self, pos, name):
        if len(Plant.images) == 0:
            Plant.load_all_images()

        self.pos = pos
        self.name = name
        self.fidx = 0
        self.time = 0
        self.state = STATE_NEW
        self.hp = 100
        self.Att = 0
        self.fps = 10
        self.event_start = 0
        self.cherrybombtime = 0
        self.cherryBomb = False
        self.collisiontime = 0.2

        if name == 'SunFlower':
            self.event_time = 15
        elif name == 'Peashooter':
            self.event_time = 5
        elif name == 'SnowPea':
            self.event_time = 5
        elif name == 'CherryBomb':
            self.event_time = 3
        elif name == 'WallNut':
            self.event_time = 10
            self.hp = 300

    @staticmethod
    def load_all_images():
        Plant.load_images('SunFlower')
        Plant.load_images('Peashooter')
        Plant.load_images('SnowPea')
        Plant.load_images('CherryBomb')
        Plant.load_images('Peashooter')
        Plant.load_images('WallNut')

    @staticmethod
    def load_images(char):
        if char in Plant.images:
            return Plant.images[char]

        count = 0
        file_fmt = '../res/plants/%s/%s_%d.png'

        type_images = []
        n = 0
        while True:
            n += 1
            fn = file_fmt % (char, char, n)
            if os.path.isfile(fn):
                type_images.append(gfw.image.load(fn))
            else:
                break
            count += 1
        Plant.images[char] = type_images

        print('%d images loaded for %s' % (count, char))

    def update(self):
        # state가 STATE_NEW이면 마우스 따라다니도록한다.
        if self.state == STATE_MOUNT:
            self.event_start += gfw.delta_time
            self.collisiontime += gfw.delta_time
            if self.event_start > self.event_time:
                if self.name != 'CherryBomb':
                    self.event_start = 0
                if self.name == 'SunFlower':
                    m = Sun((self.pos[0], self.pos[1]), (self.pos[0], self.pos[1]))
                    gfw.world.add(gfw.layer.sun, m)
                elif self.name == 'Peashooter':
                    m = Bullet((self.pos[0], self.pos[1]), 'Normal')
                    gfw.world.add(gfw.layer.bullet, m)
                elif self.name == 'SnowPea':
                    m = Bullet((self.pos[0], self.pos[1]), 'snow')
                    gfw.world.add(gfw.layer.bullet, m)
                elif self.name == 'CherryBomb' and self.cherryBomb == False:
                    self.time += gfw.delta_time
                    self.fidx = round(self.time * self.fps)
                elif self.name == 'WallNut':
                    pass


        if self.name != 'CherryBomb':
            self.time += gfw.delta_time
            self.fidx = round(self.time * self.fps)
        else: # 체리의 인덱스가 터짐이면 좀비와 충돌체크해서 주변 좀비 죽인다. 그리고 삭제된다.
            if self.fidx >= 6:
                self.cherryBomb = True
                if self.cherrybombtime == 0:
                    check_collision_cherrybomb(self.pos)
                self.cherrybombtime += gfw.delta_time
                if self.cherrybombtime > 1:
                    self.remove()



    def remove(self):
        gfw.world.remove(self)

    def collision_event(self, Att):
        if self.collisiontime > COLLISION_TIME:
            self.collisiontime = 0
            self.hp -= Att
            print("체력감소")
            if self.hp < 0:
                self.remove()

    def handle_event(self, e):
        if e.type == SDL_MOUSEBUTTONDOWN and e.button == SDL_BUTTON_LEFT:
            self.state = STATE_MOUNT

            return True
        if self.state == STATE_NEW:
            self.pos = e.x, get_canvas_height() - e.y
            return True

        return False

    def draw(self):
        images = self.images[self.name]
        image = images[self.fidx % len(images)]
        image.draw(*self.pos)

    def Sunflower_event(self):
        # 일정시간마다 햇살 뱉어냄
        pass

    def PeaShooter_event(self):
        # 일정시간마다 공격 총알 발사
        pass

    def Snowpea_event(self):
        # 일정시간마다 얼음 총알 발사
        pass

    def CherryBomb_evnet(self):
        # 설치 후 일정 시간 후 프레임이 바뀌고 프레임 마지막번째에서 터짐
        # 마지막 프레임이 지속됨 그 후 삭제
        # 폭발 시 근접 좀비 공격
        pass

    def WallNut_event(self):
        # 체력이 매우 쎄다
        # 체력이 줄면서 이미지가 먹힌걸로 바뀐다
        pass

    def get_bb(self):
        l = -Plant.bb_WIDTH // 2
        b = -Plant.bb_HEIGHT // 2
        r = Plant.bb_WIDTH // 2
        t = Plant.bb_HEIGHT // 2
        x, y = self.pos
        return x + l, y + b, x + r, y + t


