from pygame import *

size = 20
color = "#222222aa"
width = 1200
height = 50

class Score_lable(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)

    def draw(self, text, screen):
        self.font = font.SysFont("Arial", size)
        self.textSurf = self.font.render(text, 1, Color(color))
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        screen.blit(self.textSurf, (width/2 - W/2, height/2 - H/2))