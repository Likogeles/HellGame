import pygame

from classes import Button, Floor, Hero


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
        self.hero_sprites = pygame.sprite.Group()
        self.floor_sprites = pygame.sprite.Group()
        self.hero = Hero(100, 100, self.hero_sprites)
        Floor(100, 200, "floor.png", self.floor_sprites)
        Floor(50, 200, "floor.png", self.floor_sprites)
        Floor(150, 200, "floor.png", self.floor_sprites)
        Floor(150, 150, "floor.png", self.floor_sprites)
        Floor(50, 150, "floor.png", self.floor_sprites)

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.floor_sprites.draw(screen)
        self.hero_sprites.draw(screen)

    def update(self, event):
        if event.type == pygame.KEYDOWN:
            self.hero.beginmove(event, self.floor_sprites)
        elif event.type == pygame.KEYUP:
            self.hero.stopmove(event)
        self.hero.move(self.floor_sprites)

    def gravity(self):
        self.hero.gravity(self.floor_sprites)
