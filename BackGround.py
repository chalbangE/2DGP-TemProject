from pico2d import *


class Background:
    def __init__(self):
        self.image = load_image('PNG\play_background.png')
    def draw(self):
        self.image.draw(752 / 2, 669 / 2)
    def update(self):
        pass



