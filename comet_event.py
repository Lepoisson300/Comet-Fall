import pygame
from comet import Comet
#creer une classe qui va gerer cet evenement
class CometFalllEvent:

    #lors du chargement -- creer un compteur
    def __init__(self):
        self.percent = 0
        self.percent_speed = 5

        # definir un groupe de comete
        self.all_comet = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 5

    def is_full_loaded(self):
        return self.percent >= 100

    def meteor_fall(self):
        # apparaitre boule de feu
        self.all_comet.add(Comet())

    def attempt_fall(self):
        #la jauge d'eevenement est totallement chargé
        if self.is_full_loaded():
            self.percent = 0

    def update_bar(self, surface):

        #ajouter du pourcentage a la barre
        self.add_percent()

        # appel de la methode pour declencher la pluie
        if self.is_full_loaded():
            self.meteor_fall()

        # barre noir (en arriere plan)
        pygame.draw.rect(surface, (0, 0, 0), [
            0,  # axe des x
            surface.get_height() - 20,  # axe des y
            surface.get_width(),  # longueur de la fenetre
            10  # epaisseur de la barre
        ])
        # barre rouge (jauge d'evenement)
        pygame.draw.rect(surface, (187, 11, 11), [
            0, # axe des x
            surface.get_height()-20 , #axe des y
            (surface. get_width() / 100)* self.percent, # longueur de la fenetre
            10 #epaisseur de la barre
        ])
