import random
import pygame


class AnimateSprite(pygame.sprite.Sprite):

    # définir les choses a faire a la créations de l'entité
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'cometfall/assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0  # commencer l'animation a l'image 0
        self.images = animation.get(sprite_name)
        self.animation = False

    # définir une methode pour démarer l'animation
    def start_animation(self):
        self.animation = True

    # définir une methode pour animer le sprite
    def animate(self, loop=False):
        # verifier si l'animation est active
        if self.animation:
            # passer a l'image suivante
            self.current_image += random.randint(0, 1)
            # verifier si on a atteint la fin de l'animation
            if self.current_image >= len(self.images):
                # remettre l'animation de départ
                self.current_image = 0
                # verifier si l'animation n'est pas en mode boucle
                if loop is False:
                    # désactivation de l'animation
                    self.animation = False
            # modifier l'image précédente par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)


# définir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    # charger les 24 images de ce sprite correspondant
    images = []
    # récupérer le chemin du dossier pour ce sprite
    path = f"cometfall/assets/{sprite_name}/{sprite_name}"

    # boucler sur chaque images dans ce dossier
    for num in range(1, 24):
        image_path = path + f'{num}.png'
        images.append(pygame.image.load(image_path))

    # renvoyer le contenu des images
    return images


def load_animation_images_player_right(sprite_name):
    # charger les 24 images de ce sprite correspondant
    images = []
    # récupérer le chemin du dossier pour ce sprite
    path = f"cometfall/assets/{sprite_name}/{sprite_name}"

    # boucler sur chaque images dans ce dossier
    for num in range(1, 7):
        image_path = path + f'{num}.png'
        images.append(pygame.image.load(image_path))

    # renvoyer le contenu des images
    return images


def load_animation_images_player_left(sprite_name):
    # charger les 24 images de ce sprite correspondant
    images = []
    # récupérer le chemin du dossier pour ce sprite
    path = f"cometfall/assets/{sprite_name}/{sprite_name}"

    # boucler sur chaque images dans ce dossier
    for num in range(1, 7):
        image_path = path + f'{num}.png'
        images.append(pygame.image.load(image_path))

    # renvoyer le contenu des images
    return images


# definir un dictionnaire qui va contenir les images chargées de chaque sprite
# mummy -- [...mummy1.png, ...mummy2.png, ...]
animation = {
    'mummy': load_animation_images('mummy'),
    'player': load_animation_images_player_right('player'),
    'player_left': load_animation_images_player_left('player_left'),
    'alien': load_animation_images('alien'),
    'squeletton': load_animation_images('squeletton')
}
