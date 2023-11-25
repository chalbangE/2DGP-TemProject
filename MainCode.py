
from pico2d import *
from BackGround import *
import random
import math
import numpy as np

def handle_events():
    global GameOn, mx, my

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GameOn = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            GameOn = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
            player.p2_remain_ball -= 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            mouse.handle_event(event)
            arrow.handle_event(event)
            if background.state.now_state == End:
                reset_game()
                show_cursor()
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, back_H - 1 - event.y
            mouse.handle_event(event)
            background.handle_event(event)
            arrow.handle_event(event)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            background.handle_event(event)
            mouse.handle_event(event)
            arrow.handle_event(event)
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
                        player.p1_skill_turn = 9
                elif my >= 250 and my <= 410:
                    background.state.p1whatSelect = 1
                    if e.type == SDL_MOUSEBUTTONDOWN:
                        player.p1_select = 1
                        player.p1_skill_turn = 5
                elif my >= 410 and my <= 570:
                    background.state.p1whatSelect = 0
                    if e.type == SDL_MOUSEBUTTONDOWN:
                        player.p1_select = 0
                        player.p1_skill_turn = 5
                else:
                    background.state.p1whatSelect = 3
            elif player.p2_select == 3:
                if my >= 90 and my <= 250:
                    background.state.p2whatSelect = 2
                    if e.type == SDL_MOUSEBUTTONDOWN:
                        player.p2_select = 2
                        player.p2_skill_turn = 9
                        self.ready_ok = get_time()
                elif my >= 250 and my <= 410:
                    background.state.p2whatSelect = 1
                    if e.type == SDL_MOUSEBUTTONDOWN:
                        player.p2_select = 1
                        player.p2_skill_turn = 5
                        self.ready_ok = get_time()
                elif my >= 410 and my <= 570:
                    background.state.p2whatSelect = 0
                    if e.type == SDL_MOUSEBUTTONDOWN:
                        player.p2_select = 0
                        player.p2_skill_turn = 5
                        self.ready_ok = get_time()
                else:
                    background.state.p2whatSelect = 3
            else:
                if get_time() - self.ready_ok >= 1.5:
                    background.state.now_state = GameStart
                    if player.p1_skill_turn == 9:
                        ball[(random.randint(0, 2) * 2) + 1].goal = True
                        player.p1_remain_ball = 2
                    if player.p2_skill_turn == 9:
                        ball[(random.randint(0, 2) * 2)].goal = True
                        player.p2_remain_ball = 2
                    hide_cursor()



class Player:
    def __init__(self):
        self.Character_img = load_image("PNG\\Character.png")
        self.p1_select = 3
        self.p2_select = 3
        self.p1_remain_ball = 3
        self.p2_remain_ball = 3
        self.p1_skill_turn = 5
        self.p2_skill_turn = 5
    def draw(self):
        if background.state.now_state == GameStart:
            self.Character_img.clip_draw(self.p2_select * 100, 0, 100, 100, back_W - 130, back_H - 130, 280, 280)
            self.Character_img.clip_composite_draw(self.p1_select * 100, 0, 100, 100, 0, 'h', 130, back_H - 130, 280, 280)
        pass

    def update(self):
        if self.p1_remain_ball == 0:
            background.state.now_state = End
            background.state.win = 1
        elif self.p2_remain_ball == 0:
            background.state.now_state = End
            background.state.win = 2
        pass

    def handle_event(self, e):
        if self.now_state == End and e.type == SDL_KEYDOWN and e.key == SDLK_SPACE:
             self.now_state = Select
        pass

class Gameplaying:
    def __init__(self):
        self.img = load_image("PNG\\arrow.png")
        self.radian = 0
        self.dis_x = 0
        self.dis_y = 0
        self.radian = math.atan2(self.dis_y, self.dis_x)
        self.mod = 'dis'
        self.power = 0
        self.power_font = load_font('ttf\\PF스타더스트 Bold.ttf', 30)
        self.skill_font = load_font('ttf\\Ramche.ttf', 25)

    def draw(self):
        if background.state.now_state == GameStart:
            if self.mod != 'shoot':
                self.img.clip_composite_draw(0, 0, 78, 26, self.radian, '', mainball.x, mainball.y, 78, 26)
            if self.mod == 'power':
                self.power_font.draw(mx + 40, my + 40, f'{self.power // 10}', (255, 255, 255))
            if player.p1_skill_turn == 5:
                self.skill_font.draw(200, back_H - 215, f'스킬 ON!', (255, 255, 255))
                if self.mod == 'skill':
                    self.skill_font.draw(50, back_H // 2, '스킬을 사용하려면 스페이스바 / 넘어가려면 클릭', (255, 255, 255))
            if player.p2_skill_turn == 5:
                self.skill_font.draw(back_W - 290, back_H - 215, f'스킬 ON!', (255, 255, 255))
                if self.mod == 'skill':
                    self.skill_font.draw(50, back_H // 2, '스킬을 사용하려면 스페이스바 / 넘어가려면 클릭', (255, 255, 255))

    def update(self):
        if self.mod == 'dis':
            self.radian = math.atan2(self.dis_y, self.dis_x)
        elif self.mod == 'power':
            self.power += 1
            if self.power == 110:
                self.power = 0
        pass

    def handle_event(self, e):
        global turn
        if e.type == SDL_MOUSEMOTION or e.type == SDL_MOUSEBUTTONDOWN or e.type == SDL_KEYDOWN :
            if background.state.now_state == GameStart and self.mod == 'dis':
                self.dis_x = mx - mainball.x
                self.dis_y = my - mainball.y
                length = math.sqrt(math.pow(self.dis_x, 2) + math.pow(self.dis_y, 2))
                self.dis_x = self.dis_x / length
                self.dis_y = self.dis_y / length

                if e.type == SDL_MOUSEBUTTONDOWN:
                    self.Mod_trans('power')
            elif self.mod == 'power':
                if e.type == SDL_MOUSEBUTTONDOWN:
                    self.Mod_trans('shoot')
                    self.power = self.power / 13
                    mainball.dis_x = self.dis_x * self.power
                    mainball.dis_y = self.dis_y * self.power
                    mainball.power = self.power
                    mainball.face_dis_x = mainball.dis_x
                    mainball.face_dis_y = mainball.dis_y
            elif self.mod == 'skill':
                if e.type == SDL_MOUSEBUTTONDOWN:
                    self.Mod_trans('dis')
                elif e.type == SDL_KEYDOWN and e.key == SDLK_SPACE:
                    if player.p1_skill_turn == 5 and turn == 1:
                        if player.p1_select == 0:
                            pass
                        elif player.p1_select == 1:
                            mainball.x = mainball.save_x
                            mainball.y = mainball.save_y
                            for i in ball:
                                i.x = i.save_x
                                i.y = i.save_y
                            self.Mod_trans('dis')
                            turn = 1
                    if player.p2_skill_turn == 5 and turn == 2:
                        if player.p2_select == 0:
                            pass
                        elif player.p2_select == 1:
                            mainball.x = mainball.save_x
                            mainball.y = mainball.save_y
                            for i in ball:
                                i.x = i.save_x
                                i.y = i.save_y
                            self.Mod_trans('dis')
                            turn = 2

    def Mod_trans(self, trans_mod):
        global turn
        self.mod = trans_mod
        if trans_mod == 'dis':
            self.power = 0
            if turn == 1:
                turn = 2
            else:
                turn = 1
                if player.p1_skill_turn < 5:
                    player.p1_skill_turn += 1
                if player.p2_skill_turn < 5:
                    player.p2_skill_turn += 1
        elif trans_mod == 'power':
            pass
        elif trans_mod == 'shoot':
            mainball.save_x = mainball.x
            mainball.save_y = mainball.y
            for i in ball:
                i.save_x = i.x
                i.save_y = i.y
            pass
        elif trans_mod == 'skill':
            if turn == 1 and player.p1_skill_turn == 9:
                self.Mod_trans('dis')
            elif turn == 2 and player.p2_skill_turn == 9:
                self.Mod_trans('dis')
            pass

class Ball:
    img = None
    def __init__(self):
        if Ball.img == None:
            Ball.img = load_image("PNG\\ball26x26.png")
        self.whatball = 0
        self.x = 0 #random.randint(90, 680)
        self.y = 0 #random.randint(100, 326)
        self.ani = 0
        self.face_dis_x = 0
        self.face_dis_y = 0
        self.radian = 0
        self.power = 0
        self.radius = 13
        self.goal = False

        self.save_x = 0
        self.save_y = 0

    def draw(self):
        if background.state.now_state == GameStart and self.goal == False:
            self.img.clip_composite_draw((self.ani // 5) * 26, self.whatball * 26, 26, 26, self.radian, '', self.x, self.y, 26, 26)
    def update(self):
        self.x += self.face_dis_x * self.power
        self.y += self.face_dis_y * self.power

        if self.power > 0:
            self.Dis_reduce()
            self.Collide_wall()
            self.Collide_ball()
            self.ani += 1
            if self.ani == 75:
                self.ani = 0
            # 공 이동 끝나면 GGG
            if self.power == 0 and self.whatball == 0:
                arrow.Mod_trans('skill')

        self.radian = math.atan2(self.face_dis_y, self.face_dis_x)
        pass

    def handle_event(self, e):
        pass

    def Dis_reduce(self):
        if self.power > 0:
            decay_rate = 0.01
            stop_power = 0.005

            self.power -= decay_rate

            if stop_power >= self.power:
                self.power = 0

    def Collide_wall(self):
        Goal = False
        if ((self.x <= 52 and self.y >= back_H - 309)
            or (self.x >= 708 and self.y >= back_H - 309)
            or (self.y <= back_H - 603 and self.x <= 52)
            or (self.x >= 708 and self.y <= back_H - 603)
            or (self.x >= 371 and self.x <= 390 and self.y >= back_H - 305)
            or (self.x >= 371 and self.x <= 390 and self.y <= back_H - 615)):
            Goal = True

        if Goal:
            if self.whatball == 0:
                if turn == 1: player.p2_remain_ball = 0
                else: player.p1_remain_ball = 0
            elif self.whatball % 2 == 0 and self.goal == False:
                player.p1_remain_ball -= 1
                self.goal = True
            elif self.whatball % 2 == 1 and self.goal == False:
                player.p2_remain_ball -= 1
                self.goal = True

        in_x = True
        in_y = True

        if self.x >= 34 and self.x <= 727 - 13:
            in_x = False
        if self.y >= back_H - 622 + 13 and self.y <= back_H - 289 - 13:
            in_y = False

        if in_x:
            self.x -= self.face_dis_x * self.power
            self.face_dis_x *= -1
            self.power *= 0.9
        if in_y:
            self.y -= self.face_dis_y * self.power
            self.face_dis_y *= -1
            self.power *= 0.9
        pass


    def calculate_collision_angle(self, other_ball):
        relative_velocity_x = other_ball.x - (self.x - (self.face_dis_x * self.power))
        relative_velocity_y = other_ball.y - (self.y - (self.face_dis_y * self.power))

        relative_speed = math.sqrt(relative_velocity_x ** 2 + relative_velocity_y ** 2)
        relative_angle = math.atan2(relative_velocity_y, relative_velocity_x)

        collision_angle = (relative_angle + 2 * math.pi) % (2 * math.pi)
        return collision_angle

    def Collide_ball(self):
        if self.whatball == 0:
            for i in range(6):
                if self.goal == False and ball[i].goal == False:
                    ball_space_x = math.pow(ball[i].x - self.x, 2)
                    ball_space_y = math.pow(ball[i].y - self.y, 2)
                    x_collide = False
                    y_collide = False

                    if ball_space_x <= math.pow(26, 2):
                        x_collide = True
                    if ball_space_y <= math.pow(26, 2):
                        y_collide = True

                    if x_collide and y_collide:
                        # 충돌 각 계산
                        collision_angle = self.calculate_collision_angle(ball[i])

                        # 방향 반전 및 충돌 퍼짐 설정
                        ball[i].face_dis_x = math.cos(collision_angle)
                        ball[i].face_dis_y = math.sin(collision_angle)

                        # 결과를 self.dis_x, self.dis_y에 넣기
                        self.x -= self.face_dis_x * self.power
                        self.y -= self.face_dis_y * self.power
                        self.face_dis_x = -math.cos(collision_angle)
                        self.face_dis_y = -math.sin(collision_angle)

                        ball[i].power = (self.power * 0.9)
                        self.power = self.power * 0.9
                        return
        else:
            for i in range(6):
                if self.goal == False and ball[i].goal == False:
                    x_collide = False
                    y_collide = False
                    if ball[i].whatball != self.whatball:
                        ball_space_x = math.pow(ball[i].x - self.x, 2)
                        ball_space_y = math.pow(ball[i].y - self.y, 2)
                        if ball_space_x <= math.pow(26, 2):
                            x_collide = True
                        if ball_space_y <= math.pow(26, 2):
                            y_collide = True

                    if x_collide and y_collide:
                        # 충돌 각 계산
                        collision_angle = self.calculate_collision_angle(ball[i])

                        # 방향 반전 및 충돌 퍼짐 설정
                        ball[i].face_dis_x = math.cos(collision_angle)
                        ball[i].face_dis_y = math.sin(collision_angle)

                        # 벡터 뒤집기
                        self.x -= self.face_dis_x * self.power
                        self.y -= self.face_dis_y * self.power
                        self.face_dis_x = -math.cos(collision_angle)
                        self.face_dis_y = -math.sin(collision_angle)

                        # 충돌 후 속도 감소
                        ball[i].power = self.power * 0.8
                        self.power = self.power * 0.8
                        return




def reset_game():
    global GameOn, background, world, mouse, player, mainball, ball, arrow

    GameOn = True
    world = []

    background = BackGround()
    world.append(background)

    mainball = Ball()
    mainball.x = 100
    mainball.y = 215
    mainball.dis_x = 0
    mainball.dis_y = 0
    world.append(mainball)

    ball = [Ball() for i in range(6)]

    Deployment = []
    for i in range(6):
        a = random.randint(0, 5)
        while a in Deployment:
            a = random.randint(0, 5)
        Deployment.append(a)

    ball[Deployment[0]].x = 375
    ball[Deployment[0]].y = 215

    ball[Deployment[1]].x = 410
    ball[Deployment[1]].y = 240

    ball[Deployment[2]].x = 410
    ball[Deployment[2]].y = 190

    ball[Deployment[3]].x = 445
    ball[Deployment[3]].y = 215

    ball[Deployment[4]].x = 445
    ball[Deployment[4]].y = 255

    ball[Deployment[5]].x = 445
    ball[Deployment[5]].y = 175

    for i in range(6):
        ball[i].whatball = i + 1
        world.append(ball[i])

    player = Player()
    world.append(player)

    arrow = Gameplaying()
    world.append(arrow)

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
mx, my = -100, -100

while GameOn:
    handle_events()
    update_game()
    render_game()
    delay(0.01)

close_canvas()
