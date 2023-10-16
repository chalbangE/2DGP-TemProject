from pico2d import load_image


class Play:
    def __init__(self):
        self.image = load_image('play_background.png')
    def draw(self):
        self.image.draw(0,0)
