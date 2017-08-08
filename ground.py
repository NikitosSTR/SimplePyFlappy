from pygame import *

GROUND_WIDTH = 640
GROUND_HEIGHT = 40
GROUND_COLOR = "#effa69"


class Ground(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = Surface((GROUND_WIDTH, GROUND_HEIGHT))
        self.image.fill(Color(GROUND_COLOR))
        self.rect = Rect(0, 440, GROUND_WIDTH, GROUND_HEIGHT)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
