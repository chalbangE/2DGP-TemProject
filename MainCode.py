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
            mouse.handle_event(event)
        elif event.type == SDL_MOUSEBUTTONUP:
            mouse.handle_event(event)

class Mouse():
    def __init__(self):
        self.ready_img = load_image('PNG\\chalk.png')
        self.ready_on_img = load_image('PNG\\chalk_on.png')
        self.ready_state = 0
        self.ready_ok = 0

    def draw(self):
        if background.state.now_state == Ready:
            if self.ready_state == 1 or self.ready_state == 3:
                self.ready_on_img.draw(175, 325)
            if self.ready_state == 2 or self.ready_state == 3:
                self.ready_on_img.draw(580, 325)
            if self.ready_state == 3 and get_time() - self.ready_ok >= 2.0:
                background.state.now_state = GameStart
            else:
                self.ready_img.draw(mx, my)

    def update(self):
        pass

    def handle_event(self, e):
        if e.type == SDL_MOUSEBUTTONDOWN and background.state.now_state == Ready:
            if mx >= 160 and mx <= 200 and my >= 300 and my <= 339:
                if self.ready_state == 2:
                    self.ready_state = 3
                    self.ready_ok = get_time()
                elif self.ready_state == 1 or self.ready_state == 0:
                    self.ready_state = 1
            if mx >= 565 and mx <= 605 and my >= 300 and my <= 339:
                if self.ready_state == 1:
                    self.ready_state = 3
                    self.ready_ok = get_time()
                elif self.ready_state == 2 or self.ready_state == 0:
                    self.ready_state = 2


def reset_game():
    global GameOn, background, world, mouse

    GameOn = True
    world = []
    mx, my = -100, -100

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
