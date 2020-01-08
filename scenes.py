import pygame
import time


from classes import HealthPoint, BulletSliderSprite, Button
from classes import Floor, Endlevel, Box
from classes import Bullet, SinusBullet
from classes import Hero, BaseEnemy, UpEnemy


class Menu:
    def __init__(self):
        pygame.mouse.set_visible(True)
        self.menu_but_sprites = pygame.sprite.Group()
        Button("continue", "continuebut.png", 336, 300, self.menu_but_sprites)
        Button("newgame", "newgamebut.png", 336, 360, self.menu_but_sprites)
        Button("listlevs_", "levelsbut.png", 336, 420, self.menu_but_sprites)
        Button("quit", "quitbut.png", 336, 480, self.menu_but_sprites)

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.menu_but_sprites.draw(screen)

    def click(self, pos, scr):
        for i in self.menu_but_sprites:
            if i.click(pos):
                while i.rect.x < 970:
                    for j in self.menu_but_sprites:
                        j.rect.x += 10
                    scr.fill((0, 0, 0))
                    self.menu_but_sprites.draw(scr)
                    pygame.display.flip()
                    time.sleep(0.001)
                return i.name
        return "menu"


class Listlevs:
    def __init__(self):
        self.menu_but_sprites = pygame.sprite.Group()
        Button("level_1", "level_1.png", 336, 300, self.menu_but_sprites)
        Button("level_2", "level_2.png", 336, 360, self.menu_but_sprites)
        Button("menu_", "back.png", 336, 480, self.menu_but_sprites)
        # Временно обозначено управление

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.menu_but_sprites.draw(screen)

    def click(self, pos, scr):
        for i in self.menu_but_sprites:
            if i.click(pos):
                while i.rect.x < 970:
                    for j in self.menu_but_sprites:
                        j.rect.x += 10
                    scr.fill((0, 0, 0))
                    self.menu_but_sprites.draw(scr)
                    pygame.display.flip()
                    time.sleep(0.001)
                return i.name
        return "listlevs"


class Level:
    def __init__(self, level_text):
        self.hero_sprites = pygame.sprite.Group()
        self.floor_sprites = pygame.sprite.Group()
        self.boxes_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()
        self.hp_sprites = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.but_sprites = pygame.sprite.Group()
        self.pause = False
        self.level_text = level_text[:-4].lower()

        Button("continue", "continuebut.png", 336, 300, self.but_sprites)
        Button(self.level_text, "again.png", 336, 360, self.but_sprites)
        Button("menu_", "exittomenu.png", 336, 420, self.but_sprites)
        Button("quit", "quitbut.png", 336, 480, self.but_sprites)

        self.bullet_0_slider = pygame.sprite.Group(BulletSliderSprite("bull_0_slider.png"))
        self.bullet_1_slider = pygame.sprite.Group(BulletSliderSprite("bull_1_slider.png"))

        filename = "data/LevelsLists/" + level_text
        with open(filename, 'r') as mapFile:
            level_map = [line.strip() for line in mapFile]
        max_width = max(map(len, level_map))
        level = list(map(lambda x: x.ljust(max_width, '.'), level_map))

        for i in range(len(level)):
            for j in range(len(level[0])):
                if level[i][j] == "=":
                    self.all_sprites.add(Floor(50 * j, 50 * i, "floor.png", self.floor_sprites))
                elif level[i][j] == "0":
                    x = Box(50 * j, 50 * i, "box.png", self.boxes_sprites)
                    self.all_sprites.add(x)
                    self.floor_sprites.add(x)
                elif level[i][j] == "@":
                    self.hero = Hero(50 * j, 50 * i - 40, self.hero_sprites)
                elif level[i][j] == "#":
                    self.all_sprites.add(BaseEnemy(50 * j, 50 * i - 20, self.enemy_sprites))
                elif level[i][j] == "&":
                    self.all_sprites.add(UpEnemy(50 * j, 50 * i - 20, self.enemy_sprites))
                elif level[i][j] == "+":
                    if level_text == "Level_1.txt":
                        Endlevel(50 * j, 50 * i - 50, "level_2", "level1.png", self.all_sprites)
                    elif level_text == "Level_2.txt":
                        Endlevel(50 * j, 50 * i - 50, "menu_", "level1.png", self.all_sprites)

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.all_sprites.draw(screen)
        self.hero_sprites.draw(screen)
        self.hp_sprites.draw(screen)
        self.bullet_sprites.draw(screen)
        if self.pause:
            pygame.mouse.set_visible(True)
            self.but_sprites.draw(screen)
        else:
            pygame.mouse.set_visible(False)
        if self.hero.weapons_slide == 0:
            self.bullet_0_slider.draw(screen)
        elif self.hero.weapons_slide == 1:
            self.bullet_1_slider.draw(screen)

    def gravity(self):
        if not self.pause:
            self.hero.gravity(self.floor_sprites, self.all_sprites)

            for i in self.bullet_sprites:
                x = i.fly(self.all_sprites, self.hero_sprites)
                if type(x) == int:
                    if x <= 0:
                        return self.level_text
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
                    self.all_sprites.add(new_bullet)

    def animateupdate(self):
        if not self.pause:
            self.hero.animate()


class Level1(Level):
    def __init__(self, level_text):
        super().__init__(level_text)

    def hero_shoot(self):
        x = self.hero.shoot()
        if x:
            self.bullet_sprites.add(x)

    def click(self, pos):
        for i in self.but_sprites:
            if i.click(pos):
                return i.name
        return "level1"

    def eventupdate(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.pause = not self.pause

        if self.pause:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = self.click(event.pos)
                if x == "continue":
                    self.pause = not self.pause
                else:
                    return x
        else:
            x = self.hero.eventin(event, self.floor_sprites, self.all_sprites)
            if x:
                if type(x) == Bullet:
                    self.bullet_sprites.add(x)
                elif type(x) == SinusBullet:
                    self.bullet_sprites.add(x)
                elif x == "level_2" or x == "menu_":
                    return x


class Level2(Level):
    def __init__(self, level_text):
        super().__init__(level_text)

    def hero_shoot(self):
        x = self.hero.shoot()
        if x:
            self.bullet_sprites.add(x)

    def click(self, pos):
        for i in self.but_sprites:
            if i.click(pos):
                return i.name
        return "level1"

    def eventupdate(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.pause = not self.pause

        if self.pause:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = self.click(event.pos)
                if x == "continue":
                    self.pause = not self.pause
                else:
                    return x
        else:
            x = self.hero.eventin(event, self.floor_sprites, self.all_sprites)
            if x:
                if type(x) == Bullet:
                    self.bullet_sprites.add(x)
                elif type(x) == SinusBullet:
                    self.bullet_sprites.add(x)
                elif x == "menu_":
                    return x
