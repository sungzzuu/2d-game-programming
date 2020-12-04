from pico2d import *
import gfw

FINAL_WAVE = False

def init():
   global card_slot, item_slot, final_wave, shovel, zombie_gage, flag
   card_slot = gfw.image.load('../res/interface/9_Seed_Slots.png')
   item_slot = gfw.image.load('../res/interface/ground.png')
   final_wave = gfw.image.load('../res/interface/finalwave.png')
   shovel = gfw.image.load('../res/interface/shovel.png')
   zombie_gage = gfw.image.load('../res/interface/FlagMeterEmpty.png')
   flag = gfw.image.load('../res/interface/FlagMeterParts2.png')
def draw():
    x, y = get_canvas_width() // 2, get_canvas_height() // 2
    card_slot.draw(x - 98, y + 258)
    item_slot.draw(x + 210, y + 268)
    shovel.draw(609, get_canvas_height() - 33)
    zombie_gage.draw(650, 12)
    flag.draw(588, 17)
    if FINAL_WAVE:
        final_wave.draw(x, y)

def update():
    pass

