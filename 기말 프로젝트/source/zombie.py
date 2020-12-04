from pico2d import *
import gfw
import gobj
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode


def set_image_alpha(image, alpha):
    SDL_SetTextureAlphaMod(image.texture, int(alpha))

class Zombie:
    WIDTH, HEIGHT = 166, 144
    bb_WIDTH, bb_HEIGHT = 20, 80
    ACTIONS = ['Attack', '', 'Die']
    images = {}
    GAME_OVER = False


    def __init__(self, pos, char):
        if len(Zombie.images) == 0:
            Zombie.load_all_images()

        self.pos = pos
        self.char = char
        self.images = Zombie.load_images(self.char)
        self.action = ''
        self.fidx = 0
        self.time = 0
        self.speed = 12
        self.hp = 100
        self.fps = 12
        self.Att = 10
        self.alpha = 255
        self.collisionplant = False

    def some_function(self, image):
        set_image_alpha(image, self.alpha)

    @staticmethod
    def load_all_images():
        Zombie.load_images('Zombie')
        Zombie.load_images('ConeheadZombie')
        Zombie.load_images('BucketheadZombie')

    @staticmethod
    def load_images(char):
        if char in Zombie.images:
            return Zombie.images[char]

        images = {}
        count = 0
        file_fmt = '../res/zombies/%s/%s/%s_%d.png'

        for action in Zombie.ACTIONS:
            action_images = []
            n = -1
            while True:
                n += 1
                fn = file_fmt % (char, char+action,char+action, n)
                if os.path.isfile(fn):
                    action_images.append(gfw.image.load(fn))
                else:
                    break
                count += 1
            images[action] = action_images
        Zombie.images[char] = images
        print('%d images loaded for %s' % (count, char))
        return images

    def alpha_decrease(self):
        self.alpha -= 2
        if self.alpha <= 0:
            self.remove()

    def update(self):
        if self.collisionplant == False and self.action == 'Attack':
            self.action = ''
            self.speed = 5

        self.time += gfw.delta_time
        self.fidx = round(self.time * self.fps)
        x, y = self.pos
        x -= self.speed * gfw.delta_time
        self.pos = x, y
        if self.action == 'Die' and self.fidx >= 8:
            self.fidx = 8
            self.alpha_decrease()
        self.collisionplant = False

        # 좀비의 좌표가 풀밭을 벗어나면 게임오버 올스탑
        if x < - Zombie.WIDTH // 2:
            Zombie.GAME_OVER = True

    def draw(self):
        images = self.images[self.action]
        image = images[self.fidx % len(images)]
        self.some_function(image)
        image.draw(*self.pos)

    def get_bb(self):
        l = -Zombie.bb_WIDTH // 2
        b = -Zombie.bb_HEIGHT // 2
        r = Zombie.bb_WIDTH // 2
        t = Zombie.bb_HEIGHT // 2
        x, y = self.pos
        return x + l, y + b, x + r, y + t

    def remove(self):
        gfw.world.remove(self)

    def collision_event(self, Att):
        self.hp -= Att
        if Att < 0:
            self.hp = 0
        if Att == 0:  # 식물과 충돌 시 action Attack으로
            self.collisionplant = True
            if self.action != 'Attack':
                self.action = 'Attack'
                self.fidx = 0
                self.time = 0
                self.speed = 0
        if self.hp <= 0 and self.action != 'Die':
            self.action = 'Die'
            self.fidx = 0
            self.time = 0
            self.fps = 8
            self.speed = 0