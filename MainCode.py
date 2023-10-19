from pico2d import *
from BackGround import *

def handle_events():
    global GameOn

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GameOn = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            GameOn = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, 669 - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            points.append((event.x, TUK_HEIGHT - 1 - event.y))

def reset_game():
    global GameOn, background, world

    GameOn = True
    world = []

    background = BackGround()
    world.append(background)
    pass

def update_game():
    for o in world:
        o.update()

def render_game():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas(back_W, back_H)
reset_game()

while GameOn:
    handle_events()
    update_game()
    render_game()
    delay(0.01)

close_canvas()
