
back_W, back_H = 752, 669
back_WS = 762

from pico2d import *

class BackGround:
    def __init__(self):
        self.state = State(self)
        self.state.start()
        self.win = 0
    def draw(self):
        self.state.draw()

    def update(self):
        self.state.update()

    def handle_event(self, event):
        self.state.handle_event(('INPUT', event))


class Ready:
    @staticmethod
    def enter(back):
        hide_cursor()

    @staticmethod
    def draw(back):
        back.image1.draw(back_W / 2, back_H / 2)

    @staticmethod
    def update(back):
        pass

    @staticmethod
    def exit(back):
        show_cursor()
        pass


class Select:
    @staticmethod
    def enter(back):
        pass

    @staticmethod
    def draw(back):
        back.image3.draw(back_W / 2, back_H / 2)
        back.p1select_img.clip_draw(back.p1whatSelect * back_WS, 0, back_WS, back_H, back_W / 2, back_H / 2)
        back.p2select_img.clip_draw(back.p2whatSelect * back_WS, 0, back_WS, back_H, back_W / 2, back_H / 2)

    @staticmethod
    def update(back):
        pass
    @staticmethod
    def exit(back):
        pass

class GameStart:
    @staticmethod
    def enter(back):
        pass
    @staticmethod
    def draw(back):
        back.image2.draw(back_W / 2, back_H / 2)
    @staticmethod
    def update(back):
        pass
    @staticmethod
    def exit(back):
        pass

class End:
    @staticmethod
    def enter(back):
        pass
    @staticmethod
    def draw(back):
        if back.win == 1:
            if back.p1whatSelect == 0:
                back.end_image1.draw(back_W / 2, back_H / 2)
            elif back.p1whatSelect == 1:
                back.end_image2.draw(back_W / 2, back_H / 2)
            elif back.p1whatSelect == 2:
                back.end_image3.draw(back_W / 2, back_H / 2)
            back.font.draw(110, back_H - 500, 'P1', (103, 153, 255))
        elif back.win == 2:
            if back.p2whatSelect == 0:
                back.end_image1.draw(back_W / 2, back_H / 2)
            elif back.p2whatSelect == 1:
                back.end_image2.draw(back_W / 2, back_H / 2)
            elif back.p2whatSelect == 2:
                back.end_image3.draw(back_W / 2, back_H / 2)
            back.font.draw(110, back_H - 500, 'P2', (255, 151, 220))
    @staticmethod
    def update(back):
        pass

    @staticmethod
    def exit(back):
        pass

class State:
     def __init__(self, back):
        self.image1 = load_image('PNG\\ready_background.png')
        self.image2 = load_image('PNG\\play_background2.png')
        self.image3 = load_image('PNG\\select_background.png')
        self.end_image1 = load_image('PNG\\end_background1.png')
        self.end_image2 = load_image('PNG\\end_background2.png')
        self.end_image3 = load_image('PNG\\end_background3.png')

        self.p1select_img = load_image('PNG\\1P_select.png')
        self.p2select_img = load_image('PNG\\2P_select.png')
        self.p1whatSelect = 3
        self.p2whatSelect = 3

        self.font = load_font('ttf\\Ramche.ttf', 90)

        self.back = back
        self.win = 0
        self.now_state = Ready

        self.bgm = load_wav('WAV\\bgm.wav')
        self.bgm.set_volume(20)

     def start(self):
         self.bgm.set_volume(20)
         self.bgm.repeat_play()
         pass
     def update(self):
         if self.now_state == End:
             self.bgm.set_volume(0)
         pass
     def draw(self):
        self.now_state.draw(self)
     def handle_event(self, e):
         pass
