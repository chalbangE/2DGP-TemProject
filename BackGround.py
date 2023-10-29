from pico2d import *

back_W, back_H = 752, 669
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
        self.image2 = load_image('PNG\\play_background.png')
        self.back = back
        self.now_state = Ready
        self.trans = {
            Ready: {click: Ready},
            GameStart: {click: GameStart}
        }
     def start(self):
        self.now_state.enter(self)
     def update(self):
        pass
     def draw(self):
        self.now_state.draw(self)
     def handle_event(self, e):
        for check_event, next_state in self.trans[self.now_state].items():
            if check_event(e):
                self.now_state.exit(self.back)
                self.now_state = next_state
                self.now_state.enter(self.back)
                return True

        return False