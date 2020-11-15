import gfw
from pico2d import *
from gobj import *
from player import Player
from background import HorzScrollBackground

def enter():
    gfw.world.init(['bg', 'enemy', 'player'])

    bg = HorzScrollBackground('futsal_court.png')
    gfw.world.add(gfw.layer.bg, bg)

    global player
    player = Player()
    player.bg = bg
    gfw.world.add(gfw.layer.player, player)


def update():
    gfw.world.update()

def draw():
    gfw.world.draw()
    # gobj.draw_collision_box()

def handle_event(e):
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
        return
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
            return

    if player.handle_event(e):
        return

def exit():
    pass



if __name__ == '__main__':
    gfw.run_main()
