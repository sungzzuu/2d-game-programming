from pico2d import *
import gfw
import gobj

from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

class Zombie:
    WIDTH, HEIGHT = 166, 144
    ACTIONS = ['Attack', '', 'Die']
    images = {}
    FPS = 12

    def __init__(self):
        if len(Zombie.images) == 0:
            Zombie.load_all_images()

        self.pos = get_canvas_width(), get_canvas_height() // 2
        self.char = 'Zombie'
        self.images = Zombie.load_images(self.char)
        self.action = ''
        self.fidx = 0
        self.time = 0
        self.speed = 5

    @staticmethod
    def load_all_images():
        Zombie.load_images('Zombie')
        Zombie.load_images('NewspaperZombie')

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
        self.fidx = round(self.time * Zombie.FPS)
        x, y = self.pos
        x -= self.speed * gfw.delta_time
        self.pos = x, y

    def draw(self):
        images = self.images[self.action]
        image = images[self.fidx % len(images)]
        image.draw(*self.pos)