import pygame
import random
import animation


class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0,
                 max_health=100, attack=0.3):
        super().__init__(name, size)
        self.game = game
        self.max_health = int(max_health)
        self.health = int(max_health)
        self.attack = attack
        self.default_speed = 1
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 500 - offset
        self.loot_amount = 10
        self.velocity = random.randint(1, self.default_speed)
        self.start_animation()

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        # infliger les degats
        self.health -= amount

        # vérifier si le monstre est mort
        if self.health <= 0:
            self.game.add_score(self.loot_amount)

            # si la barre d'evenement est chargé à son maximum
            if self.game.comet_event.is_full_loaded():
                self.game.all_monster.remove(self)
                if not bool(self.game.all_monster):
                    self.game.comet_event.meteor_fall()
            else:
                # respawn
                self.rect.x = 1000 + random.randint(0, 300)
                self.velocity = random.randint(1, self.default_speed)
                self.health = self.max_health

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        """ dessiner notre barre de vie """
        pygame.draw.rect(surface, (60, 63, 60),
                         [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46),
                         [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward(self):
        # s'il n'y a pas de collision avec un joueur
        if not self.game.check_colision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # s'il est en collision avec notre joueur
        else:
            # infliger des dégats
            self.game.player.damage(self.attack)


class Mummy(Monster):

    def __init__(self, game, health_factor=1, attack_factor=1):
        super().__init__(game, "mummy", (130, 130),
                         max_health=120*health_factor, attack=0.5*attack_factor)
        self.default_speed = 4
        self.set_loot_amount(20)


class Alien(Monster):

    def __init__(self, game, health_factor=1, attack_factor=1):
        super().__init__(game, "alien", (300, 300), offset=145,
                         max_health=250*health_factor, attack=0.8*attack_factor)
        self.default_speed = 2
        self.set_loot_amount(80)


class Squeletton(Monster):

    def __init__(self, game, health_factor=1, attack_factor=1):
        super().__init__(game, "squeletton", (50, 100), offset=-20,
                         max_health=120*health_factor, attack=0.5*attack_factor)
        self.default_speed = 6
        self.set_loot_amount(10)


class Dragon(Monster):

    def __init__(self, game, health_factor=1, attack_factor=1):
        super().__init__(game, "dragon", (155, 175), offset=50,
                         max_health=300*health_factor, attack=5*attack_factor)
        self.default_speed = 2
        self.set_loot_amount(160)