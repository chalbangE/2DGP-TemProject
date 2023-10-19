from pico2d import *

back_W, back_H = 752, 669

def Click(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT

class BackGround:
    def __init__(self):
        self.image = load_image('PNG\\ready_background.png')
    def draw(self):
        self.image.draw(back_W / 2, back_H / 2)
    def update(self):
        pass

class Ready:
    def __init__(self, back):
        self.back = back
    def draw(self):
        self.image.draw(back_W / 2, back_H / 2)
    def update(self):
        pass