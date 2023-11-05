from pico2d import *
from BackGround import *
import random

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

turn = 1

class Mouse():
    def __init__(self):
        self.ready_img = load_image('PNG\\chalk.png')
        self.ready_on_img = load_image('PNG\\chalk_on.png')
        self.play_img = load_image('PNG\\Character_mouse.png')
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
        if background.state.now_state == GameStart:
            if turn == 1:
                self.play_img.clip_draw(player.p1_select * 80, 0, 80, 70, mx, my, 80, 70)
            elif turn == 2:
                self.play_img.clip_draw(player.p2_select * 80, 0, 80, 70, mx, my, 80, 70)

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
                    hide_cursor()


class Player:
    def __init__(self):
        self.Character_img = load_image("PNG\\Character.png")
        self.p1_select = 3
        self.p2_select = 3
    def draw(self):
        if background.state.now_state == GameStart:
            self.Character_img.clip_draw(self.p2_select * 100, 0, 100, 100, back_W - 130, back_H - 130, 280, 280)
            self.Character_img.clip_composite_draw(self.p1_select * 100, 0, 100, 100, 0, 'h', 130, back_H - 130, 280, 280)
        pass

    def update(self):
        pass

    def handle_event(self, e):
        pass

#class Ball:

class Ball:
    img = None
    def __init__(self):
        if Ball.img == None:
            Ball.img = load_image("PNG\\ball26x26.png")
        self.whatball = 0
        self.x = random.randint(90, 680)
        self.y = random.randint(100, 326)
        self.ani = 0
        self.dis_x = 0
        self.dis_y = 0
        self.theta = 0
    def draw(self):
        if background.state.now_state == GameStart:
            self.img.clip_composite_draw((self.ani // 5) * 26, self.whatball * 26, 26, 26, self.theta, 'v', self.x, self.y, 30, 30)

    def update(self):
        self.x += self.dis_x
        self.y += self.dis_y
        if self.dis_x > 0 or self.dis_y > 0 or self.dis_x < 0 or self.dis_y < 0:
            self.ani += 1
            if self.ani == 75:
                self.ani = 0
        pass

    def handle_event(self, e):
        pass


def reset_game():
    global GameOn, background, world, mouse, player, mainball, ball

    GameOn = True
    world = []

    background = BackGround()
    world.append(background)
    mouse = Mouse()
    world.append(mouse)
    player = Player()
    world.append(player)

    mainball = Ball()
    mainball.x = 100
    mainball.y = 215
    world.append(mainball)

    ball = [Ball() for i in range(6)]

    for i in range(6):
        world.append(ball[i])
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
