from pico2d import *
import gfw
from card import Card
from sun import Sun
import random
from plant import Plant

SUN_TIME_TERM = 5
sun_time = 0

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
        m = Card(0, 'peashooter')
        gfw.world.add(gfw.layer.card, m)
        m = Card(1, 'sunflower')
        gfw.world.add(gfw.layer.card, m)
        m = Plant((300, 300), 'SunFlower')
        gfw.world.add(gfw.layer.plant, m)
        m = Plant((400, 300), 'Peashooter')
        gfw.world.add(gfw.layer.plant, m)

def generate_sun():
    x = random.randrange(100, get_canvas_width() - 100)
    y = get_canvas_height()
    targetX = x
    targetY = random.randrange(200, get_canvas_height()//2)
    m = Sun((x, y), (targetX, targetY))
    gfw.world.add(gfw.layer.sun, m)
