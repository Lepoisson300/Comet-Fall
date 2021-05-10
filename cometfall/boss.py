import pygame

import random


class Boss:
    def __init__(self, BossEvent):
        super().__init__()
        # définir l'image associé a ce boss
        self.image = pygame.image.load('assets/Boss_ship.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(3, 5)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.BossEvent = BossEvent
        self.game = self.BossEvent.game


class BossEvent:
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 0.12
        self.game = game
        self.boss_mode = False