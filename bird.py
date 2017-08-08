#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *

bird_height = 35
bird_width = 35
bird_indent = 150
gravity = 0.3
bird_jump = 5
bird_colour = "#de5fe1"


class Bird(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = Surface((bird_width, bird_height))
        self.image.fill(Color(bird_colour))
        self.rect = Rect(
            bird_indent,
            bird_indent,
            bird_width,
            bird_height
        )
        self.y_val = 0
        self.onGround = False

    def update(self, jump, platforms, ground):
        if jump:
            if not self.onGround:
                self.y_val = -bird_jump

        self.y_val += gravity

        self.rect.y += self.y_val
        return self.collide(platforms, ground)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def collide(self, platforms, ground):
        game_over = False
        for p in platforms:
            if (p.rect.x + 23) <= self.rect.x >= (p.rect.x + 20):
                game_over = True
            # если есть пересечение платформы с игроком
            if sprite.collide_rect(self, p) or sprite.collide_rect(self, p.down_platform):
                game_over = False
                self.y_val += gravity
                self.rect.x = p.rect.x - bird_width

        if sprite.collide_rect(self, ground):
            self.rect.y = ground.rect.y - bird_height

        if self.rect.y <= 0:
            self.rect.y = 0

        return game_over
