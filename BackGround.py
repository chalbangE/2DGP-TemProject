from pico2d import *

back_W, back_H = 752, 669
back_WS = 762
def click(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONDOWN
class BackGround:
    def __init__(self):
        self.state = State(self)
        self.state.start()
    def draw(self):
        self.state.draw()
    def update(self):
        self.state.update()
        #print(self.state)
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

class State:
     def __init__(self, back):
        self.image1 = load_image('PNG\\ready_background.png')
        self.image2 = load_image('PNG\\play_background2.png')
        self.image3 = load_image('PNG\\select_background.png')

        self.p1select_img = load_image('PNG\\1P_select.png')
        self.p2select_img = load_image('PNG\\2P_select.png')
        self.p1whatSelect = 3
        self.p2whatSelect = 3

        self.back = back
        self.now_state = GameStart
     def start(self):
        self.now_state.enter(self)
     def update(self):
        pass
     def draw(self):
        self.now_state.draw(self)
     def handle_event(self, e):
         pass
