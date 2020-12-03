from pico2d import *
import gfw
from card import Card
from sun import Sun
import random
from plant import Plant
from zombie import  Zombie

SUN_TIME_TERM = 5
sun_time = 0
Zombie_Generate_num = 0

def init(stage):

    generate_start(stage)

def update():
    global sun_time
    sun_time += gfw.delta_time
    if sun_time > SUN_TIME_TERM:
        sun_time = 0
        generate_sun()


def generate_start(stage):
    if stage == 1:
        m = Card(0, 'Peashooter')
        gfw.world.add(gfw.layer.card, m)
        m = Card(1, 'SunFlower')
        gfw.world.add(gfw.layer.card, m)
        m = Card(2, 'SnowPea')
        gfw.world.add(gfw.layer.card, m)
        m = Card(3, 'WallNut')
        gfw.world.add(gfw.layer.card, m)
        m = Card(4, 'CherryBomb')
        gfw.world.add(gfw.layer.card, m)

def generate_sun():
    x = random.randrange(100, get_canvas_width() - 100)
    y = get_canvas_height()
    targetX = x
    targetY = random.randrange(200, get_canvas_height()//2)
    m = Sun((x, y), (targetX, targetY))
    gfw.world.add(gfw.layer.sun, m)

def generate_plant(pos, name):
    m = Plant(pos, name)
    gfw.world.add(gfw.layer.plant, m)

def generate_zombie_start():
    global Zombie_Generate_num

    for i in range(1, 6):
        m = Zombie((get_canvas_width() + random.randint(0, 5) * 10, get_canvas_height() - i * 100), 'Zombie')
        gfw.world.add(gfw.layer.zombie, m)
        Zombie_Generate_num += 1

def generate_zombie(name):
    global Zombie_Generate_num
    m = Zombie((get_canvas_width() + random.randint(0, 5) * 10, get_canvas_height() - random.randint(1, 5) * 100), name)
    gfw.world.add(gfw.layer.zombie, m)
    Zombie_Generate_num += 1

def generate_zombie_final():
    pass