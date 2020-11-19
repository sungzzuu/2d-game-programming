import gfw
from pico2d import *
import game_state

STATE_OFF = 0
STATE_ON = 1
def enter():
    global image, state
    image = load_image('../res/background/menu_state_0.png')
    state = STATE_OFF
def update():
    pass

def draw():
    image.draw(400, 300)

def handle_event(e):
    global image, state
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif(e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        gfw.push(game_state)
    if e.type == SDL_MOUSEMOTION:
        if e.x >= 420 and e.x <= 700 and e.y >= 92 and e.y <= 201:
            image = gfw.image.load('../res/background/menu_state_1.png')
            state = STATE_ON
        else:
            image = gfw.image.load('../res/background/menu_state_0.png')
            state = STATE_OFF
    if e.type == SDL_MOUSEBUTTONDOWN:
        if state == STATE_ON:
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

