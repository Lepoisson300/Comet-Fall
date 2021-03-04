import pygame

# définir une classe qui va gerer les animations
class AnimateSprite(pygame.sprite.Sprite):

    # définir les choses a faire a la créations de l'entité
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')


# definir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    # charger les 24 images de ce sprite correspondant
    images = []
    # recuperer le chemin du dossier pour ce sprite
    path = f"assets/{sprite_name}/{sprite_name}"

    # boucler sur chaque images dans ce dossier
    for num in range(1, 24):
        image_path = path + num + 'png'
        pygame.image.load(image_path)
        image.append(pygame.image.load(image_path))

    # renvoyer le contenu des images
    return images