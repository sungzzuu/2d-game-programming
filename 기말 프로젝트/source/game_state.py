import gfw
from pico2d import *
from gobj import *
import bg
import static_ui
import card
import generator
import sun
from zombie import Zombie
from collision import check_collision_bullet_zombie, check_collision_plant_zombie, check_collision_zombie_car
import random
import over_state
import clear_state

from car import Car

ZOMBIE_TIME = 5
ZOMBIE_NUM = 15
START_TIME = 0
FINAL_GAP_TIME = 0

def enter():
    global stage
    stage = 1
    gfw.world.init(['bg', 'ui', 'car', 'card', 'plant', 'bullet', 'zombie', 'sun'])

    bg.init()
    gfw.world.add(gfw.layer.bg, bg)

    static_ui.init()
    gfw.world.add(gfw.layer.ui, static_ui)
    generator.init(stage)

    for i in range(5):
        car = Car((10, i*100 + 70))
        gfw.world.add(gfw.layer.car, car)

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
    if Zombie.GAME_OVER == True:
        gfw.world.clear()
        Zombie.GAME_OVER = False
        gfw.change(over_state)
        return

    gfw.world.update()
    generator.update()

    check_collision_bullet_zombie()
    check_collision_plant_zombie()
    check_collision_zombie_car()

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
    global FINAL_GAP_TIME
    if start == True and gfw.world.count_at(gfw.layer.zombie) == 0 and FINAL_GAP_TIME <= 5 :
        FINAL_GAP_TIME += gfw.delta_time
        if FINAL_GAP_TIME > 5:
            for i in range(20):
                type = random.choice(['ConeheadZombie', 'BucketheadZombie', 'FlagZombie', 'Zombie'])
                z = generator.generate_zombie(type)
        static_ui.FINAL_WAVE = True
    if FINAL_GAP_TIME > 5 and gfw.world.count_at(gfw.layer.zombie) == 0:
        gfw.change(clear_state)
    if static_ui.FINAL_WAVE and gfw.world.count_at(gfw.layer.zombie) != 0:
        static_ui.FINAL_WAVE = False


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


def pause():
    pass


def resume():
    pass

if __name__ == '__main__':
    gfw.run_main()