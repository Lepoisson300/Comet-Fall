import pygame
import random
from monster import Monster
from player import Player
from game import Game
from animation import AnimateSprite


class Levels:

    def __init__(self, background, game, name, size, offset=0):
        super().__init__(name, size)
        self.background = background
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 500 - offset
        self.loot_amount = 10
        self.velocity = random.randint(1, 3)
        self.start_animation()