import pygame
from comet_event import CometFallEvent
from player import Player
from monster import Monster


#creer une seconde classe qui va representer notre jeu
class Game:

    def __init__(self):
        #definir si notre jeu a commencé
        self.is_playing = False
        #generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #generer l'evenement
        self.comet_event = CometFallEvent(self)
        #definir un groupe de monstre
        self.all_monster = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monster.add(monster)

    def check_colision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def game_over(self):
        # remettre le jeu a neuf
        self.all_monster = pygame.sprite.Group()
        self.comet_event.all_comet = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False

    def update(self, screen):
        # apliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiszer la bnarre de vie du joueur
        self.player.update_health_bar(screen)

        # actualiser la barre d'evenement du jeu
        self.comet_event.update_bar(screen)

        # recuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperant les monstre de notre jeu
        for monster in self.all_monster:
            monster.forward()
            monster.update_health_bar(screen)

        # recuperer les comete de notre jeu
        for comet in self.comet_event.all_comet:
            comet.fall()

        # appliquer l'ensemble des iùmage de mon groupe de projectile
        self.player.all_projectiles.draw(screen)
        
        #appliquer l'ensemble des images de comet
        self.comet_event.all_comet.draw(screen)

        # appliquer l'ensemble des imùages de mon groupe de monstre
        self.all_monster.draw(screen)

        # verifier si le joueur souhaite aller a gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
