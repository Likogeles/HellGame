import pygame
import time


from classes import Button, Floor, Hero


class Menu:
    def __init__(self):
        self.but_sprites = pygame.sprite.Group()
        Button("continue", "continuebut.png", 336, 300, self.but_sprites)
        Button("newgame", "newgamebut.png", 336, 360, self.but_sprites)
        Button("listlevels", "levelsbut.png", 336, 420, self.but_sprites)
        Button("quit", "quitbut.png", 336, 480, self.but_sprites)

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.but_sprites.draw(screen)

    def click(self, pos, scr):
        for i in self.but_sprites:
            if i.click(pos):
                while i.rect.x < 970:
                    for j in self.but_sprites:
                        j.rect[0] += 50
                        scr.fill((0, 0, 0))
                        self.but_sprites.draw(scr)
                        pygame.display.flip()
                        time.sleep(0.001)
                return i.name
        return "menu"


class Level:
    def __init__(self, level_text):
        self.hero_sprites = pygame.sprite.Group()
        self.floor_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
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

    def gravity(self):
        self.hero.gravity(self.floor_sprites)


class Level1(Level):
    def __init__(self, level_text):
        super().__init__(level_text)

    def update(self, event):
        if event.type == pygame.KEYDOWN:
            self.hero.beginmove(event, self.floor_sprites)
        elif event.type == pygame.KEYUP:
            self.hero.stopmove(event)
        self.hero.move(self.floor_sprites)
