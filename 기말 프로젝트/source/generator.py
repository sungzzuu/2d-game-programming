from pico2d import *
import gfw
from card import Card
from sun import Sun
import random

SUN_TIME_TERM = 10
sun_time = 0
def init(stage):

    generate_start(stage)

def update():
    global sun_time
    sun_time += gfw.delta_time
    print(sun_time)
    if sun_time > SUN_TIME_TERM:
        sun_time = 0
        generate_sun()


def generate_start(stage):
    if stage == 1:
        m = Card(0, 'peashooter')
        gfw.world.add(gfw.layer.card, m)
        m = Card(1, 'sunflower')
        gfw.world.add(gfw.layer.card, m)

def generate_sun():
    x = random.randrange(100, get_canvas_width() - 100)
    y = get_canvas_height()
    targetX = x
    targetY = random.randrange(200, get_canvas_height()//2)
    m = Sun((x, y), (targetX, targetY))
    gfw.world.add(gfw.layer.sun, m)
