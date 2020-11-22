from pico2d import *
import gfw


class Plant:
    PLANT_TYPE = ['SunFlower', 'Peashooter', 'SnowPea', 'WallNut', 'CherryBomb']
    images = {}
    FPS = 10
    def __init__(self, pos, name):
        if len(Plant.images) == 0:
            Plant.load_all_images()

        self.pos = pos
        self.name = name
        self.fidx = 0
        self.time = 0

    @staticmethod
    def load_all_images():
        Plant.load_images('SunFlower')
        Plant.load_images('Peashooter')

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
        self.time += gfw.delta_time
        self.fidx = round(self.time * Plant.FPS)

    def remove(self):
        gfw.world.remove(self)

    def draw(self):
        images = self.images[self.name]
        image = images[self.fidx % len(images)]
        image.draw(*self.pos)