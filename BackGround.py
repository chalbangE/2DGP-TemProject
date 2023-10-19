from pico2d import *

back_W, back_H = 752, 669

class BackGround:
    def __init__(self):
        self.state = State()
        self.state.start()
    def draw(self):
        self.state.draw()
    def update(self):
        self.state.update()
    def handle_event(self, event):
        pass

class Ready:
    @staticmethod
    def enter(back):
        back.image = load_image('PNG\\ready_background.png')

    @staticmethod
    def draw(back):
        back.image.draw(back_W / 2, back_H / 2)

    @staticmethod
    def update(back):
        pass

class State:
     def __init__(self):
        self.now_state = Ready
     def start(self):
        self.now_state.enter(self)
     def update(self):
        pass
     def draw(self):
        self.now_state.draw(self)