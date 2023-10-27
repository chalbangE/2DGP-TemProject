from pico2d import *
from BackGround import *

def handle_events():
    global GameOn, mx, my

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GameOn = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            GameOn = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, back_H - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            background.handle_event(event)

class Mouse():
    def __init__(self):
        self.image = load_image('PNG\\chalk.png')

    def draw(self):
        if background.state.now_state == Ready:
            self.image.draw(mx, my)

    def update(self):
        pass

def reset_game():
    global GameOn, background, world, mouse

    GameOn = True
    world = []

    background = BackGround()
    world.append(background)
    mouse = Mouse()
    world.append(mouse)
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
