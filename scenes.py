import pygame

from classes import Button


class Menu:
    def __init__(self):
        self.but_sprites = pygame.sprite.Group()
        self.levelbut = Button("newgame", "newgamebut.png", 336, 300, self.but_sprites)
        self.levelbut = Button("levels", "levelsbut.png", 336, 360, self.but_sprites)
        self.levelbut = Button("continue", "continuebut.png", 336, 420, self.but_sprites)
        self.levelbut = Button("quit", "quitbut.png", 336, 480, self.but_sprites)

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.but_sprites.draw(screen)

    def click(self, pos):
        for i in self.but_sprites:
            if i.click(pos):
                return i.name
        return "menu"
