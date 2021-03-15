import pygame
import random


class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        # definir l'image associé a cette comete
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random .randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comet.remove(self)
        self.comet_event.game.sound_manager.play('meteorite')

        # verifier si le nb de comete est 0
        if len(self.comet_event.all_comet) == 0:
            # remettre la barre a 0
            self.comet_event.reset_percent()
            # apparaitre les 2 premiers monstre
            self.comet_event.game.start()
            self.comet_event.game.start()

    def fall(self):
        self.rect.y += self.velocity

        # ne tombe pas sur le sol
        if self.rect.y >= 500:
            self.remove()

            # si il n'y a plus de boules de feu
            if len(self.comet_event.all_comet) == 0:
                # remettre la jauge de départ
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        # verifier si la boule de feu touche le joueur
        if self.comet_event.game.check_colision(
                self, self.comet_event.game.all_players):
            # retirer la boule feu
            self.remove()
            # subir 20 de degat
            self.comet_event.game.player.damage(20)



