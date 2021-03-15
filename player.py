import pygame
from threading import Timer

from projectile import Projectile
import animation


class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 100
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 450
        self.launch_issafe = True

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # si le joueur n'a plus de point de vie
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def _launch_cooldown(self, t=0.4):
        """ Create cooldown between each projectile """
        def make_launch_safe():
            self.launch_issafe = True
        self.launch_issafe = False
        Timer(t, make_launch_safe).start()

    def launch_projectile(self):
        if self.launch_issafe:
            # créer une nouvelle instance de la classe projectile
            self._launch_cooldown()
            self.all_projectiles.add(Projectile(self))
            self.start_animation()
            self.game.sound_manager.play('tir')

    def update_health_bar(self, surface):
        # dessiner notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])

    def move_right(self):
        # si le joueur n'est pas en colision avec une entité monstre
        if not self.game.check_colision(self, self.game.all_monster):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
