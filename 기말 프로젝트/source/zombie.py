from pico2d import *
import gfw
import gobj

from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

class Zombie:
    WIDTH, HEIGHT = 166, 144
    bb_WIDTH, bb_HEIGHT = 84, 120
    ACTIONS = ['Attack', '', 'Die']
    images = {}

    def __init__(self):
        if len(Zombie.images) == 0:
            Zombie.load_all_images()

        self.pos = get_canvas_width(), get_canvas_height() // 2
        self.char = 'ConeheadZombie'
        self.images = Zombie.load_images(self.char)
        self.action = ''
        self.fidx = 0
        self.time = 0
        self.speed = 5
        self.hp = 100
        self.fps = 12


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

    def update(self):
        self.time += gfw.delta_time
        self.fidx = round(self.time * self.fps)
        x, y = self.pos
        x -= self.speed * gfw.delta_time
        self.pos = x, y
        if self.action == 'Die' and self.fidx > 8:
            self.remove()

    def draw(self):
        images = self.images[self.action]
        image = images[self.fidx % len(images)]
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
        if self.hp <= 0 and self.action != 'Die':
            self.action = 'Die'
            self.fidx = 0
            self.time = 0
            self.fps = 8