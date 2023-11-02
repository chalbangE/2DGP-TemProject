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
            mouse.handle_event(event)
            background.handle_event(event)
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
        # Ready에서 마우스
        if background.state.now_state == Ready:
            if self.ready_state == 1 or self.ready_state == 3:
                self.ready_on_img.draw(175, 325)
            if self.ready_state == 2 or self.ready_state == 3:
                self.ready_on_img.draw(580, 325)
            if self.ready_state == 3 and get_time() - self.ready_ok >= 1.5:
                background.state.now_state = Select
                show_cursor()
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
            # Select에서 마우스
        elif background.state.now_state == Select:
            if player.p1_select == 3:
                if my >= 90 and my <= 250:
                    background.state.p1whatSelect = 2
                    if e.type == SDL_MOUSEBUTTONDOWN:
                        player.p1_select = 2
                elif my >= 250 and my <= 410:
                    background.state.p1whatSelect = 1
                    if e.type == SDL_MOUSEBUTTONDOWN:
                        player.p1_select = 1
                elif my >= 410 and my <= 570:
                    background.state.p1whatSelect = 0
                    if e.type == SDL_MOUSEBUTTONDOWN:
                        player.p1_select = 0
                else:
                    background.state.p1whatSelect = 3
            elif player.p2_select == 3:
                if my >= 90 and my <= 250:
                    background.state.p2whatSelect = 2
                    if e.type == SDL_MOUSEBUTTONDOWN:
                        player.p2_select = 2
                        self.ready_ok = get_time()
                elif my >= 250 and my <= 410:
                    background.state.p2whatSelect = 1
                    if e.type == SDL_MOUSEBUTTONDOWN:
                        player.p2_select = 1
                        self.ready_ok = get_time()
                elif my >= 410 and my <= 570:
                    background.state.p2whatSelect = 0
                    if e.type == SDL_MOUSEBUTTONDOWN:
                        player.p2_select = 0
                        self.ready_ok = get_time()
                else:
                    background.state.p2whatSelect = 3
            else:
                if get_time() - self.ready_ok >= 1.5:
                    background.state.now_state = GameStart


class Player:
    def __init__(self):
        self.Character_img = load_image("PNG\\Character.png")
        self.p1_select = 3
        self.p2_select = 3
    def draw(self):
        pass

    def update(self):
        pass

    def handle_event(self, e):
        pass

def reset_game():
    global GameOn, background, world, mouse, player

    GameOn = True
    world = []

    background = BackGround()
    world.append(background)
    mouse = Mouse()
    world.append(mouse)
    player = Player()
    world.append(player)
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
mx, my = -100, -100

while GameOn:
    handle_events()
    update_game()
    render_game()
    delay(0.01)

close_canvas()
