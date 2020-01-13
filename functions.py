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


def self_on_screen(self):
    if -100 <= self.rect.y <= 600 and -50 <= self.rect.x <= 972:
        return True
    return False


def check_block(x, y, all_sprites):
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("Enemys/check_block.png")
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = x
    sprite.rect.y = y
    if pygame.sprite.spritecollideany(sprite, all_sprites):
        return True
    return False


def check_npc(x, y, npces_sprites):
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("Enemys/check_block.png")
    sprite.rect = sprite.image.get_rect()
    sprite.rect.y = y + 35
    sprite.rect.x = x - 15
    x = pygame.sprite.spritecollideany(sprite, npces_sprites)
    if x:
        return x.rect.x + 15, x.rect.y - 20, x.name
    sprite.rect.x += 50
    x = pygame.sprite.spritecollideany(sprite, npces_sprites)
    if x:
        return x.rect.x + 15, x.rect.y - 20, x.name
    sprite.rect.x += 40
    x = pygame.sprite.spritecollideany(sprite, npces_sprites)
    if x:
        return x.rect.x + 15, x.rect.y - 20, x.name


def check_hero(x, y, move_right, hero_sprites):
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("Enemys/check_hero.png")
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = x
    sprite.rect.y = y
    sp = -10
    if move_right:
        sp = 10
    while -100 <= sprite.rect.x <= 1000:
        sprite.rect.x += sp
        if pygame.sprite.spritecollideany(sprite, hero_sprites):
            sprite.kill()
            return True
    sprite.kill()
    return False


def check_hero_down(x, y, hero_sprites):
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("Enemys/check_hero.png")
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = x
    sprite.rect.y = y
    sp = 10
    while sprite.rect.y <= 600:
        sprite.rect.y += sp
        if pygame.sprite.spritecollideany(sprite, hero_sprites):
            sprite.kill()
            return True
    sprite.kill()
    return False
