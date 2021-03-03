import pygame

#creer une classe pour gerer cette comete
class Comet(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        #definir l'image associé a cette comete
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()