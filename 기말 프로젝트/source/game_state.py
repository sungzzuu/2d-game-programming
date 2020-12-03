import gfw
from pico2d import *
from gobj import *
import bg
import static_ui
import card
import generator
import sun
from zombie import Zombie
from collision import check_collision_bullet_zombie, check_collision_plant_zombie
import random

ZOMBIE_TIME = 5
ZOMBIE_NUM = 15
START_TIME = 20

def enter():
    global stage
    stage = 1
    gfw.world.init(['bg', 'ui', 'card', 'plant', 'bullet', 'zombie', 'sun'])

    bg.init()
    gfw.world.add(gfw.layer.bg, bg)

    static_ui.init()
    gfw.world.add(gfw.layer.ui, static_ui)
    generator.init(stage)

    global font
    font = gfw.font.load('../res/moris9.ttf', 25)

    global zombie_generate_time
    zombie_generate_time = 0.0

    global start
    start = False

def change_stage():
    global stage
    generator.init(stage)

def update():
    global start

    gfw.world.update()
    generator.update()

    check_collision_bullet_zombie()
    check_collision_plant_zombie()

    global zombie_generate_time
    zombie_generate_time += gfw.delta_time
    if zombie_generate_time > START_TIME and start == False:
        generator.generate_zombie_start()
        zombie_generate_time = 0
        start = True
    elif start == False:
        return




    if zombie_generate_time > ZOMBIE_TIME and generator.Zombie_Generate_num < ZOMBIE_NUM:
        zombie_generate_time = 0
        type = random.choice(['ConeheadZombie', 'BucketheadZombie', 'FlagZombie'])
        generator.generate_zombie(type)

    # 시작했고 좀비가 다 비었으면 5초후에 Final wave 띄우고 마지막 좀비 공격 시작
    

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

    for obj in gfw.world.objects_at(gfw.layer.card):
        if obj.handle_event(e):
            capture = obj
            return True

    for obj in gfw.world.objects_at(gfw.layer.plant):
        if obj.handle_event(e):
            capture = obj
            return True

    return False


def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()