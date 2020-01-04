import pygame
import time


from classes import HealthPoint, Button, Floor, Endlevel, Bullet, Hero, Enemy


class Menu:
    def __init__(self):
        self.but_sprites = pygame.sprite.Group()
        Button("continue", "continuebut.png", 336, 300, self.but_sprites)
        Button("newgame", "newgamebut.png", 336, 360, self.but_sprites)
        Button("listlevels", "levelsbut.png", 336, 420, self.but_sprites)
        Button("quit", "quitbut.png", 336, 480, self.but_sprites)
        # Временно обозначено управление
        Button("", "upravlenie.png", 50, 50, self.but_sprites)

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.but_sprites.draw(screen)

    def click(self, pos, scr):
        for i in self.but_sprites:
            if i.click(pos):
                while i.rect.x < 970:
                    for j in self.but_sprites:
                        j.rect.x += 50
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
        self.bullet_sprites = pygame.sprite.Group()
        self.hp_sprites = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.but_sprites = pygame.sprite.Group()
        self.pause = False

        filename = "data/LevelsLists/" + level_text
        with open(filename, 'r') as mapFile:
            level_map = [line.strip() for line in mapFile]
        max_width = max(map(len, level_map))
        level = list(map(lambda x: x.ljust(max_width, '.'), level_map))

        for i in range(len(level)):
            for j in range(len(level[0])):
                if level[i][j] == "=":
                    self.all_sprites.add(Floor(50 * j, 50 * i, "floor.png", self.floor_sprites))
                elif level[i][j] == "@":
                    self.hero = Hero(50 * j, 50 * i - 40, self.hero_sprites)
                elif level[i][j] == "#":
                    self.all_sprites.add(Enemy(50 * j, 50 * i - 20, self.enemy_sprites))
                elif level[i][j] == "+":
                    Endlevel(50 * j, 50 * i - 50, "menu", "level1.png", self.all_sprites)

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.all_sprites.draw(screen)
        self.hero_sprites.draw(screen)
        self.hp_sprites.draw(screen)
        self.bullet_sprites.draw(screen)
        if self.pause:
            self.but_sprites.draw(screen)

    def gravity(self):
        if not self.pause:
            self.hero.gravity(self.floor_sprites)
            for i in self.enemy_sprites:
                i.gravity(self.floor_sprites)
            for i in self.bullet_sprites:
                i.fly(self.all_sprites, self.hero_sprites)

            for i in range(self.hero.hp):
                if i % 20 == 0:
                    HealthPoint(i * 30 + 10, 10, self.hp_sprites)

            for i in self.hp_sprites:
                i.kill()
            for i in range(self.hero.hp):
                if i % 20 == 0:
                    HealthPoint((i // 20) * 40 + 10, 10, self.hp_sprites)

    def movingupdate(self):
        if not self.pause:
            for i in self.enemy_sprites:
                new_bullet = i.moving(self.floor_sprites, self.hero_sprites)
                if new_bullet:
                    self.bullet_sprites.add(new_bullet)

    def animateupdate(self):
        if not self.pause:
            self.hero.animate()


class Level1(Level):
    def __init__(self, level_text):
        super().__init__(level_text)
        Button("continue", "continuebut.png", 336, 300, self.but_sprites)
        Button("menu", "exittomenu.png", 336, 360, self.but_sprites)
        Button("quit", "quitbut.png", 336, 420, self.but_sprites)

    def click(self, pos, scr):
        for i in self.but_sprites:
            if i.click(pos):
                return i.name
        return "level1"

    def eventupdate(self, event, screen):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.pause = not self.pause

        if self.pause:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = self.click(event.pos, screen)
                if x == "continue":
                    self.pause = not self.pause
                else:
                    return x
        else:
            x = self.hero.eventin(event, self.floor_sprites, self.all_sprites)
            if x:
                if type(x) == Bullet:
                    self.bullet_sprites.add(x)
                elif x == "menu":
                    return x
