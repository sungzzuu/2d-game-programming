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
    gfw.world.init(['bg', 'ui', 'card', 'plant', 'sun'])

    bg.init()
    gfw.world.add(gfw.layer.bg, bg)

    static_ui.init()
    gfw.world.add(gfw.layer.ui, static_ui)
    generator.init(stage)

    global font
    font = gfw.font.load('../res/moris9.ttf', 25)



def change_stage():
    global stage
    generator.init(stage)

def update():
    gfw.world.update()
    generator.update()

def draw():
    gfw.world.draw()
    font.draw(40, get_canvas_height() - 70, '%d' % sun.sun_score)

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
    if e.type == SDL_MOUSEBUTTONDOWN:
        print(e.x, " ", e.y)

    if handle_mouse(e):
        return
    # 마우스 클릭이 일어났을 때 햇살과 충돌체크

capture = None
def handle_mouse(e):
    global capture
    if capture is not None:
        holding = capture.handle_event(e)
        if not holding:
            capture = None
        return True

    for obj in gfw.world.objects_at(gfw.layer.sun):
        if obj.handle_event(e):
            capture = obj
            return True

    return False


def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()