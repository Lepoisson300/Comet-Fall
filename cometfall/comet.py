import random

import pygame


class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        # définir l'image associé a cette comète
        self.image = pygame.image.load('cometfall/assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random .randint(3, 5)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event
        self.game = self.comet_event.game

    def remove(self):
        self.comet_event.all_objects.remove(self)
        self.game.sound_manager.play('meteorite')

        # if all comets are fallen
        if not bool(self.comet_event.all_objects):
            self.comet_event.reinit()
            # remettre la jauge de départ
            self.comet_event.reset_percent()
            self.comet_event.spawn_mode = False

    def move(self):
        self.rect.y += self.velocity

        # ne tombe pas sur le sol
        if self.rect.y >= 500:
            self.remove()

        # verifier si la boule de feu touche le joueur
        if self.game.check_colision(
                self, self.game.all_players):
            # retirer la boule feu
            self.remove()
            # subir 20 de dégats
            self.game.player.damage(20)


class CometFallEvent:

    # lors du chargement -- créer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 0.1
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

    def spawn(self, n=20):
        """ Generate n meteors"""
        self.spawn_mode = True
        self.game.event_number += 1
        self.percent = 0
        for _ in range(n):
            # apparaitre boule de feu
            self.all_objects.add(Comet(self))

    def reinit(self):
        self.game.load_level()
        self.game.spawn_monsters()

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
