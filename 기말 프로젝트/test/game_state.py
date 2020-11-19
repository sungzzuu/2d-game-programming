import gfw
from pico2d import *
from gobj import *


def enter():
    pass

def update():
    pass

def draw():
    pass

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()


def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()