import gfw
from pico2d import *
import game_state

def enter():
    global image
    image = load_image('../res/background/menu_state_0.png')

def update():
    pass

def draw():
    image.draw(400, 300)

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif(e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        gfw.push(game_state)
    elif e.type == SDL_MOUSEBUTTONDOWN:
        gfw.push(game_state)
    # 마우스가 버튼 위치에 있으면 사진 바꾸기
    # 마우스가 버튼 위치에서 벗어나면 또 사진 바꾸기
    # 버튼 수업한 것을 참고


def exit():
    global image
    del image

def pause():
     pass

def resume():
    pass

if __name__ == '__main__':
    gfw.run_main()

