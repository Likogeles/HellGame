import pygame
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data/SpritesList', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey((255, 255, 255))
    else:
        image = image.convert_alpha()
    return image


def check_block(x, y, all_sprites):
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("Enemys/check_block.png")
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = x
    sprite.rect.y = y
    if pygame.sprite.spritecollideany(sprite, all_sprites):
        return True
    return False


def check_hero(x, y, hero_sprites):
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("Enemys/check_hero.png")
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = x
    sprite.rect.y = y
    if pygame.sprite.spritecollideany(sprite, hero_sprites):
        return True
    return False
