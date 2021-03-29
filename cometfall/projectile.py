import pygame 


class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self. velocity = 7
        self.player = player
        self.image = pygame.image.load('cometfall/assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 130
        self.rect.y = player.rect.y + 60
        self.origin_image = self.image
        self.angle = 0

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        #self.rotate()
        # test si le projectile entre en collision avec un monstre
        for monster in self.player.game.check_colision(self, self.player.game.all_monster):
            self.remove()  # supprimer la boule de feu
            monster.damage(self.player.attack)  # infliger des dégats

        # verifier si notre n'est plus recent sur l'ecran
        if self.rect.x > 1080:
            # supprimer le projectile (en dehors de l'ecran)
            self.remove()

"""
    def rotate(self):
        # tourner le projectile
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
"""