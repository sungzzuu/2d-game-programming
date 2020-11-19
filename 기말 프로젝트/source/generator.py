from pico2d import *
import gfw
from card import Card


def init(stage):
    generate(stage)

def update():
   pass

def generate(stage):
    if stage == 1:
        m = Card(0, 'peashooter')
        gfw.world.add(gfw.layer.card, m)
        m = Card(1, 'sunflower')
        gfw.world.add(gfw.layer.card, m)