import pygame

from comet import Comet


class CometFallEvent:

    # lors du chargement -- creer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 0.25
        self.game = game
        self.fall_mode = False

        # definir un groupe de comete
        self.all_comet = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 5

    def reset_percent(self):
        self.percent = 0

    def is_full_loaded(self):
        return self.percent >= 100

    def meteor_fall(self):
        # boucle pour le nb de comet
        for i in range(1, 20):
            # apparaitre boule de feu
            self.all_comet.add(Comet(self))

    def reinit_comet(self):
        self.all_comet = pygame.sprite.Group()

    def attempt_fall(self):
        # la jauge d'eevenement est totallement chargé
        if self.is_full_loaded() and len(self.game.all_monster) == 0:
            self.meteor_fall()
            self.reset_percent()
            self.fall_mode = True

    def update_bar(self, surface):
        # ajouter du pourcentage a la barre
        self.add_percent()

        # barre noir (en arriere plan)
        pygame.draw.rect(surface, (0, 0, 0), [
            0,  # axe des x
            surface.get_height() - 20,  # axe des y
            surface.get_width(),  # longueur de la fenetre
            10  # epaisseur de la barre
        ])
        # barre rouge (jauge d'evenement)
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # axe des x
            surface.get_height()-20,  # axe des y
            (surface. get_width() / 100) * self.percent,  # longueur de la fenetre
            10  # epaisseur de la barre
        ])
