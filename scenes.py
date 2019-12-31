import pygame

from classes import Button, Hero


class Menu:
    def __init__(self):
        self.but_sprites = pygame.sprite.Group()
        Button("continue", "continuebut.png", 336, 300, self.but_sprites)
        Button("newgame", "newgamebut.png", 336, 360, self.but_sprites)
        Button("levels", "levelsbut.png", 336, 420, self.but_sprites)
        Button("quit", "quitbut.png", 336, 480, self.but_sprites)

    def render(self, screen, *args):
        screen.fill((0, 0, 0))
        self.but_sprites.draw(screen)

    def click(self, pos):
        for i in self.but_sprites:
            if i.click(pos):
                return i.name
        return "menu"


class Level1:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.hero_sprites = pygame.sprite.Group()
        self.hero = Hero(100, 100, self.hero_sprites)

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.all_sprites.draw(screen)
        self.hero_sprites.draw(screen)

    def update(self, event):
        pass