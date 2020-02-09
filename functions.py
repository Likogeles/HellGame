import pygame
import os
import sqlite3
import sys


def terminate():
    pygame.mixer.quit()
    pygame.quit()
    sys.exit()


def click_wait():
    click = True
    while click:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = False


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
    sprite.rect.x = x - 5
    x = pygame.sprite.spritecollideany(sprite, npces_sprites)
    if x:
        return x
    sprite.rect.x += 55
    x = pygame.sprite.spritecollideany(sprite, npces_sprites)
    if x:
        return x


def check_hero(x, y, move_right, hero_sprites):
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("Enemys/check_hero.png")
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = x
    sprite.rect.y = y
    sp = -45
    if move_right:
        sp = 45
    while -100 <= sprite.rect.x <= 1000:
        if pygame.sprite.spritecollideany(sprite, hero_sprites):
            sprite.kill()
            return True
        sprite.rect.x += sp
    sprite.kill()
    return False


def check_hero_down(x, y, hero_sprites):
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("Enemys/check_hero.png")
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = x
    sprite.rect.y = y
    sp = 70
    while sprite.rect.y <= 600:
        if pygame.sprite.spritecollideany(sprite, hero_sprites):
            sprite.kill()
            return True
        sprite.rect.y += sp
    sprite.kill()
    return False


def saving_location(location):
    con = sqlite3.connect("save.db")
    cur = con.cursor()
    cur.execute("""
                UPDATE Save
                SET location = {}""".format(location)).fetchall()
    con.commit()
    con.close()


def check_location():
    con = sqlite3.connect("save.db")
    cur = con.cursor()
    num = cur.execute("""
        SELECT location FROM Save """).fetchall()
    con.commit()
    con.close()
    return num[0][0]


def saving_plot(plot):
    con = sqlite3.connect("save.db")
    cur = con.cursor()
    cur.execute("""
                UPDATE Save
                SET plot = {}""".format(plot)).fetchall()
    con.commit()
    con.close()


def check_plot():
    con = sqlite3.connect("save.db")
    cur = con.cursor()
    num = cur.execute("""
        SELECT plot FROM Save """).fetchall()
    con.commit()
    con.close()
    return num[0][0]


def saving_guns(guns):
    con = sqlite3.connect("save.db")
    cur = con.cursor()
    cur.execute("""
                UPDATE Save
                SET guns = {}""".format(guns)).fetchall()
    con.commit()
    con.close()


def check_saves_guns():
    con = sqlite3.connect("save.db")
    cur = con.cursor()
    num = cur.execute("""
        SELECT guns FROM Save """).fetchall()
    con.commit()
    con.close()
    return num[0][0]


def new_game_save():
    con = sqlite3.connect("save.db")
    cur = con.cursor()
    cur.execute("""
                UPDATE Save
                SET continue = 1""").fetchall()
    con.commit()
    con.close()
    saving_plot(0)
    saving_guns(0)
    saving_location(1)


def check_continue():
    con = sqlite3.connect("save.db")
    cur = con.cursor()
    num = cur.execute("""
        SELECT continue FROM Save """).fetchall()
    con.commit()
    con.close()
    return num[0][0]
