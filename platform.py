import random
import pygame
from main import *
from ground import *
from pygame import *

PLATFORM_WIDTH = 40
PLATFORM_SPEED = 4
PLATFORM_DELTA = 100
PLATFORM_HEIGHT = WIN_HEIGHT - PLATFORM_DELTA - GROUND_HEIGHT
PLATFORM_COLOR = "#ffb16b"


class Down_Platform(sprite.Sprite):
    def __init__(self, height, margin):
        sprite.Sprite.__init__(self)

        self.down_image = Surface((PLATFORM_WIDTH, WIN_HEIGHT - height - GROUND_HEIGHT))
        self.down_image.fill(Color(PLATFORM_COLOR))
        self.rect = Rect(
            WIN_WIDTH + PLATFORM_WIDTH + margin,
            height + PLATFORM_DELTA,
            PLATFORM_WIDTH,
            WIN_HEIGHT - height - GROUND_HEIGHT
        )

    def draw(self, screen):
            screen.blit(self.down_image, (self.rect.x, self.rect.y))

    def update(self, height):

        if self.rect.x >= -PLATFORM_WIDTH:
            self.rect.x -= PLATFORM_SPEED
        else:

            h = WIN_HEIGHT

            self.down_image = Surface((PLATFORM_WIDTH, h))
            self.down_image.fill(Color(PLATFORM_COLOR))
            self.rect = Rect(
                WIN_WIDTH + PLATFORM_WIDTH,
                height  + PLATFORM_DELTA,
                PLATFORM_WIDTH,
                h
            )





class Platform(sprite.Sprite):
    def __init__(self, margin):
        sprite.Sprite.__init__(self)

        self.rnd_platform_heigh = random.random() * PLATFORM_HEIGHT

        #print(self.rnd_platform_heigh, '\n')

        self.up_image = Surface((PLATFORM_WIDTH, self.rnd_platform_heigh))
        self.up_image.fill(Color(PLATFORM_COLOR))
        self.rect = Rect(
            WIN_WIDTH + PLATFORM_WIDTH + margin,
            0,
            PLATFORM_WIDTH,
            self.rnd_platform_heigh
        )

        self.down_platform = Down_Platform(self.rnd_platform_heigh, margin)



    def update(self):
        if self.rect.x >= -PLATFORM_WIDTH:
            self.rect.x -= PLATFORM_SPEED
        else:

            self.rnd_platform_heigh = random.random() * PLATFORM_HEIGHT

            self.up_image = Surface((PLATFORM_WIDTH, self.rnd_platform_heigh))
            self.up_image.fill(Color(PLATFORM_COLOR))
            self.rect = Rect(
                WIN_WIDTH + PLATFORM_WIDTH,
                0,
                PLATFORM_WIDTH,
                self.rnd_platform_heigh
            )

        self.down_platform.update(self.rnd_platform_heigh)

    def draw(self, screen):
        screen.blit(self.up_image, (self.rect.x, self.rect.y))
        self.down_platform.draw(screen)