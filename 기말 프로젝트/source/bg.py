from pico2d import *
import gfw

def init():
   global image
   image = gfw.image.load('../res/background/bg_01.png')

def draw():
    x, y = get_canvas_width() // 2, get_canvas_height() // 2
    image.draw(image.w//2 - 220, y)

def update():
    pass