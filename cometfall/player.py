from threading import Timer

import pygame

from projectile import Projectile
import animation


class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 80
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.default_image = self.image
        image = pygame.image.load('cometfall/assets/player_T.png')
        self.shoot_image = pygame.transform.scale(image, (200, 200))
        self.rect.x = 400
        self.rect.y = 470
        self.launch_issafe = True

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # si le joueur n'a plus de point de vie
            self.game.game_over()

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
            # self.start_animation()
            self.game.sound_manager.play('tir', volume=0.5)

    def update_health_bar(self, surface):
        # dessiner notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])

    def move_right(self):
        # si le joueur n'est pas en collision avec une entité monstre
        self.set_images('player')
        if not self.game.check_colision(self, self.game.all_monster):
            self.rect.x += self.velocity
            self.start_animation()

    def move_left(self):
        self.set_images('player_left')
        self.rect.x -= self.velocity
        self.start_animation()

    def jump(self):
        # si le joueur appuie sur la fleche du haut, il saute
        for i in range(15):
            self.rect.y += 1
        for i in range(15):
            self.rect.y -= 1

