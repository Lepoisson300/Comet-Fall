import pygame
import numpy as np
import random


class Boss(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        # définir l'image associé a ce boss
        self.image = pygame.image.load('cometfall/assets/Boss_ship.png')
        self.max_health = 1000
        self.health = 1000
        self.attack = 20
        self.default_speed = 1
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 320
        self.loot_amount = 10000
        self.game = game
        self.spawn_mode = False

    def damage(self, amount):
        # infliger les degats
        self.health -= amount

        # vérifier si le monstre est mort
        if self.health <= 0:
            self.game.add_score(self.loot_amount)
            self.spawn_mode = False
            # si la barre d'evenement est chargé à son maximum
            self.game.game_over()

    def update_health_bar(self, surface):
        """ dessiner notre barre de vie """
        pygame.draw.rect(surface, (60, 63, 60),
                         [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46),
                         [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def move(self):
        # générer des valeurs entre -2 et 2 avec une certaine probabilité
        move_x, move_y = np.random.choice(np.arange(-5, 6), 2, p=[0.05, 0.05, 0.05, 0.05, 0.05, 0.5, 0.05, 0.05, 0.05, 0.05, 0.05])
        if 0 <= self.rect.y + move_y <= 500:  # test pour savoir si il est en collision avec la limite
            self.rect.y += move_y
        if 0 <= self.rect.x + move_x <= 650:
            self.rect.x += move_x

        # verifier si la boule de feu touche le joueur
        if self.game.check_colision(
                self, self.game.all_players):
            # subir 20 de dégats
            self.game.player.damage(10)


class BossEvent:

    # lors du chargement -- créer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 0.5
        self.game = game
        self.spawn_mode = False
        # définir un groupe de comète
        self.all_objects = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed

    def reset_percent(self):
        self.percent = 0

    def is_full_loaded(self):
        return self.percent >= 100

    def spawn(self):
        """ Generate n meteors"""
        self.spawn_mode = True
        self.game.event_number += 1
        self.percent = 0
        self.all_objects.add(Boss(self.game))

    def reinit(self):
        self.game.load_level()
        """
        endroit pour theo 
        """

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def update_bar(self, surface):
        # ajouter du pourcentage a la barre
        self.add_percent()

        # barre noir (en arriere plan)
        pygame.draw.rect(surface, (0, 0, 0), [
            0,  # axe des x
            surface.get_height() - 20,  # axe des y
            surface.get_width(),  # longueur de la fenêtre
            10  # épaisseur de la barre
        ])
        # barre rouge (jauge d'événement)
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # axe des x
            surface.get_height()-20,  # axe des y
            (surface. get_width() / 100) * self.percent,  # longueur de la fenêtre
            10  # épaisseur de la barre
        ])
