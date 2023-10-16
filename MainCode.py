from pico2d import *
from BackGround import Background

def handle_events():
    global GameOn

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GameOn = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            GameOn = False



def reset_game():
    global GameOn, background, world

    GameOn = True
    world = []

    background = Background()
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


open_canvas(752, 669)
reset_game()

while GameOn:
    handle_events()
    update_game()
    render_game()
    delay(0.01)

close_canvas()
