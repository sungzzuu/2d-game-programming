from pico2d import *
import gfw

FINAL_WAVE = False

def init():
   global card_slot, item_slot, final_wave
   card_slot = gfw.image.load('../res/interface/9_Seed_Slots.png')
   item_slot = gfw.image.load('../res/interface/ground.png')
   final_wave = gfw.image.load('../res/interface/finalwave.png')

def draw():
    x, y = get_canvas_width() // 2, get_canvas_height() // 2
    card_slot.draw(x - 98, y + 258)
    item_slot.draw(x + 210, y + 268)
    if FINAL_WAVE:
        final_wave.draw(x, y)

def update():
    pass

