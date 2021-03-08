import pygame
import random
import animation

# creer une classe qui va gerer la notion de monstre sur notre jeu
class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset

        self.start_animation()

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, 3)

    def damage(self, amount):
        #infliger les degats
        self.health -= amount

        # verrifier si son nouveau nombre de point de vie  = 0
        if self.health <= 0:
            # réaparaitre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, self.default_speed)
            self.health = self.max_health

            # si la barre d'evenement est chargé a son maximum
            if self.game.comet_event.is_full_loaded():
                self.game.all_monster.remove(self)

                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        # dessiner notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward(self):
        # si il n'y a pas de collision avec un joueur
        if not self.game.check_colision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si il est en collisipon avec notre joueur
        else:
            #infliger des dégats
            self.game.player.damage(self.attack)

# definir une classe pour la momie
class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)


# définir une classe pour l'alien
class Alien(Monster):

    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 130)
        self.health = 250
        self.max_health = 250
        self.attack = 0.8
        self.set_speed(2)