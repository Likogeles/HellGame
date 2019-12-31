import pygame

from functions import load_image


class Button(pygame.sprite.Sprite):
    def __init__(self, name, imagename, x, y, *group):
        super().__init__(*group)
        self.image = load_image(imagename)
        self.rect = self.image.get_rect()
        self.w, self.h = self.image.get_rect()[2], self.image.get_rect()[3]
        self.rect.x = x
        self.rect.y = y
        self.name = name

    def click(self, pos):
        if self.rect.x <= pos[0] <= self.rect.x + self.w and \
                self.rect.y <= pos[1] <= self.rect.y + self.h:
            return True
        return False


class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y, imgname, *group):
        super().__init__(*group)
        self.image = load_image(imgname, -1)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Person(pygame.sprite.Sprite):
    def __init__(self, x, y, imgname, *group):
        super().__init__(*group)
        self.image = load_image(imgname, -1)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.gravity_acceleration = 0
        self.gravity_log = True

    def gravity(self, floor_sprites):
        x = pygame.sprite.spritecollideany(self, floor_sprites)
        if x:
            self.gravity_acceleration = 0
            self.rect.y -= 1
            self.gravity_log = False
        elif self.gravity_log:
            self.rect.y += 1 + int(self.gravity_acceleration)
            self.gravity_acceleration += 0.1
            if self.gravity_acceleration > 50:
                self.gravity_acceleration = 50
        if self.rect.y > 600:
            self.rect.y = -100


class Hero(Person):
    def __init__(self, x, y, *group):
        super().__init__(x, y, "hero.png", *group)
        self.right_move = False
        self.left_move = False

    def move(self, floor_sprites):
        if self.right_move:
            self.rect.x += 3
            if not pygame.sprite.spritecollideany(self, floor_sprites):
                self.gravity_log = True
        elif self.left_move:
            self.rect.x -= 3
            if not pygame.sprite.spritecollideany(self, floor_sprites):
                self.gravity_log = True

    def beginmove(self, event, floor_sprites):
        if event.key == pygame.K_d:
            self.right_move = True
            self.left_move = False
            self.gravity_log = True
        elif event.key == pygame.K_a:
            self.left_move = True
            self.right_move = False
            self.gravity_log = True
        elif event.key == pygame.K_SPACE:
            self.rect.y += 1
            if pygame.sprite.spritecollideany(self, floor_sprites):
                self.gravity_log = True
                self.rect.y -= 5
                self.gravity_acceleration = -7

    def stopmove(self, event):
        if event.key == pygame.K_d:
            self.right_move = False
        elif event.key == pygame.K_a:
            self.left_move = False
