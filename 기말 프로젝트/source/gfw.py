
import time
from pico2d import *

running = True          # 게임이 돌아감을 나타내는 변수
stack = None            # 게임 오브젝트 스택 초기화
frame_interval = 0.01   # 프레임 간격.얼마마다 업데이트?
delta_time = 0          # 사이 시간. 사이 시간이 frame_interval이 되면 업데이트하고 0으로 초기화


def quit():
    # global : 전역변수를 사용할 때 global 선언을 해서
    # 전역변수를 사용함을 알려준다.

    global running
    running = False

def run(start_state):
    global running, stack
    running = True
    stack = [start_state]   # list

    open_canvas()

    # 이거 왜하는거?
    start_state.enter()

    global delta_time
    last_time = time.time()     #현재 시간
    while running:
        now = time.time()
        delta_time = now - last_time
        last_time = now

        # event handling
        evts = get_events()
        for e in evts:
            stack[-1].handle_event(e)

        # game logic
        stack[-1].update()

        # game rendering
        clear_canvas()
        stack[-1].draw()
        update_canvas()

        delay(frame_interval)

    while len(stack) > 0 :      # 다끝나면 뺀다.
        stack[-1].exit()
        stack.pop()


    close_canvas()

def change(state):
    global stack

    if len(stack) > 0 :
        stack.pop().exit()  # pop : 맨마지막 요소 돌려주고 삭제함

    stack.append(state)
    state.enter()

def push(state):
    global stack
    if len(stack) > 0 :
        stack[-1].pause()
    stack.append(state)
    state.enter()

def pop():
    global stack
    size = len(stack)
    if size == 1:
        quit()
    elif size > 1:
        # execute the current state's exit function
        stack[-1].exit()
        # remove the current state
        stack.pop()

        # execute resume function of the previous state
        stack[-1].resume()

def run_main():
    import sys
    main_module = sys.modules['__main__']
    run(main_module)




