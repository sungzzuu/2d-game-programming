import gfw
from pico2d import *
from gobj import *
import bg
import static_ui
import card
import generator
import sun

def enter():
    global stage
    stage = 1
    gfw.world.init(['bg', 'ui', 'card', 'sun'])

    bg.init()
    gfw.world.add(gfw.layer.bg, bg)

    static_ui.init()
    gfw.world.add(gfw.layer.ui, static_ui)
    generator.init(stage)




def change_stage():
    global stage
    generator.init(stage)

def update():
    gfw.world.update()
    generator.update()

def draw():
    gfw.world.draw()

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
    if e.type == SDL_MOUSEBUTTONDOWN:
        print(e.x, " ", e.y)

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()