import pygame
import math

from functions import load_image, check_block, check_hero


class HealthPoint(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = load_image("Hero/healthpoint.png", -1)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Button(pygame.sprite.Sprite):
    def __init__(self, name, imagename, x, y, *group):
        super().__init__(*group)
        self.image = load_image("Buttons/" + imagename)
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
        self.image = load_image("Floor/" + imgname, -1)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Box(Floor):
    def __init__(self, x, y, imgname, *group):
        super().__init__(x, y, imgname, *group)
        self.gravity_acceleration = 0
        self.gravity_log = True
        self.hp = 100
        self.t = 0

    def get_hit(self, damage):
        if self.t == 0:
            self.rect.x += 2
        elif self.t == 1:
            self.rect.x -= 2
        elif self.t == 2:
            self.rect.x -= 2
        elif self.t == 3:
            self.rect.x += 2
        self.t += 1
        if self.t > 3:
            self.t = 0

        self.hp -= damage
        if self.hp <= 0:
            self.kill()


class Endlevel(pygame.sprite.Sprite):
    def __init__(self, x, y, name_of_next_level, imgname, *group):
        super().__init__(*group)
        self.image = load_image("Endsoflevels/" + imgname, -1)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.nextlevel = name_of_next_level


class BulletSliderSprite(pygame.sprite.Sprite):
    def __init__(self, imgname, *group):
        super().__init__(*group)
        self.image = load_image("Bullets/" + imgname, -1)
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 40


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, move_on_right, speed, imgname="bull_0.png", *group):
        super().__init__(*group)
        self.image = load_image("Bullets/" + imgname, -1)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move = -speed
        if move_on_right:
            self.move = speed

    def fly(self, all_sprites, hero_sprites):
        self.rect.x += self.move
        if not (-100 <= self.rect.x <= 1000):
            self.kill()
        x = pygame.sprite.spritecollideany(self, all_sprites)
        if x:
            if type(x) == Enemy or type(x) == Box:
                x.get_hit(20)
                self.kill()
            elif type(x) == Floor:
                self.kill()

        x = pygame.sprite.spritecollideany(self, hero_sprites)
        if x:
            if type(x) == Hero:
                x.get_hit(20)
                self.kill()
                return x.hp


class SinusBullet(Bullet):
    def __init__(self, x, y, move_on_right, speed, *group):
        super().__init__(x, y, move_on_right, speed, "bull_1.png", *group)
        self.move = - math.pi * 2
        if move_on_right:
            self.move = -self.move
        self.oldx = x
        self.oldy = y

    def fly(self, all_sprites, hero_sprites):
        self.rect.y = self.oldy + int(math.sin((self.rect.x - self.oldx) // 18) * 22)
        self.rect.x += self.move
        if not (-100 <= self.rect.x <= 1000):
            self.kill()
        x = pygame.sprite.spritecollideany(self, all_sprites)
        if x:
            if type(x) == Enemy or type(x) == Box:
                x.get_hit(5)
                self.kill()
            elif type(x) == Floor:
                self.kill()


class Person(pygame.sprite.Sprite):
    def __init__(self, x, y, imgname, *group):
        super().__init__(*group)
        self.image = load_image(imgname, -1)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.gravity_acceleration = 0
        self.gravity_log = True
        self.oldrunningwasright = True
        self.hp = 100

    def gravity(self, floor_sprites):
        self.rect.y += 1 + int(self.gravity_acceleration)
        if pygame.sprite.spritecollideany(self, floor_sprites):
            self.rect.y -= 1 + int(self.gravity_acceleration)
            self.gravity_acceleration = 0
            self.gravity_log = False
        elif self.gravity_log:
            self.gravity_acceleration += 0.1
            if self.gravity_acceleration > 50:
                self.gravity_acceleration = 50
        else:
            self.gravity_acceleration += 0.1
        if self.rect.y > 600:
            self.rect.y = -100

    def get_hit(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.kill()


class Hero(Person):
    def __init__(self, x, y, *group):
        super().__init__(x, y, "Hero/hero_0.png", *group)

        self.weapons_slide = 0
        self.shooting_log = False

        self.t = 0
        self.standing_right = []
        for i in range(8):
            self.standing_right.append(pygame.transform.scale(load_image("Hero/standing_" + str(i) + ".png", -1), (45, 90)))
        self.standing_left = []
        for i in range(8):
            x = pygame.transform.scale(load_image("Hero/standing_" + str(i) + ".png", -1), (45, 90))
            self.standing_left.append(pygame.transform.flip(x, True, False))
        self.running_right = []
        for i in range(8):
            self.running_right.append(pygame.transform.scale(load_image("Hero/running_" + str(i) + ".png", -1), (45, 90)))
        self.running_left = []
        for i in range(8):
            x = pygame.transform.scale(load_image("Hero/running_" + str(i) + ".png", -1), (45, 90))
            self.running_left.append(pygame.transform.flip(x, True, False))

        self.right_move = False
        self.left_move = False

    def animate(self):
        if self.right_move:
            self.image = self.running_right[self.t]
            self.t += 1
            if self.t > 7:
                self.t = 0
            self.oldrunningwasright = True
        elif self.left_move:
            self.image = self.running_left[self.t]
            self.t += 1
            if self.t > 7:
                self.t = 0
            self.oldrunningwasright = False
        else:
            if self.oldrunningwasright:
                self.image = self.standing_right[self.t]
                self.t += 1
                if self.t > 7:
                    self.t = 0
            else:
                self.image = self.standing_left[self.t]
                self.t += 1
                if self.t > 7:
                    self.t = 0

    def move(self, floor_sprites, all_sprites):
        sp = 0
        if self.right_move:
            self.rect.x += 2
            if not(pygame.sprite.spritecollideany(self, floor_sprites)):
                sp = -2
            self.rect.x -= 2

            self.gravity_log = True
        elif self.left_move:
            self.rect.x -= 2
            if not(pygame.sprite.spritecollideany(self, floor_sprites)):
                sp = 2
            self.rect.x += 2
            self.gravity_log = True
        if sp != 0:
            if self.rect.x != 486:
                if 0 <= self.rect.x - sp <= 922:
                    self.rect.x -= sp
            else:
                minx = 0
                maxx = 0
                for i in all_sprites:
                    if i.rect.x <= minx:
                        minx = i.rect.x
                    if i.rect.x > maxx:
                        maxx = i.rect.x
                if minx + sp > 0 or maxx + sp < 922:
                    if 0 <= self.rect.x - sp <= 922:
                        self.rect.x -= sp
                else:
                    for i in all_sprites:
                        i.rect.x += sp

    def shoot(self):
        if self.shooting_log:
            x = self.rect.x
            if self.oldrunningwasright:
                x += 50
            else:
                x -= 25
            if self.weapons_slide == 1:
                return SinusBullet(x, self.rect.y + 35, self.oldrunningwasright, 10)

    def eventin(self, event, floor_sprites, all_sprites):
        if self.hp > 0:
            new_bullet = None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d or event.key == pygame.K_a or event.key == pygame.K_SPACE:
                    self.beginmove(event, floor_sprites)
                elif event.key == pygame.K_j:
                    self.beginmove(event, floor_sprites)
                    x = self.rect.x
                    if self.oldrunningwasright:
                        x += 50
                    else:
                        x -= 25
                    if self.weapons_slide == 0:
                        new_bullet = Bullet(x, self.rect.y + 10, self.oldrunningwasright, 10)
                elif event.key == pygame.K_i:
                    self.weapons_slide = 0
                elif event.key == pygame.K_o:
                    self.weapons_slide = 1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_a or event.key == pygame.K_j:
                    self.stopmove(event)

            self.move(floor_sprites, all_sprites)
            if new_bullet:
                return new_bullet

            x = pygame.sprite.spritecollideany(self, all_sprites)
            if type(x) == Endlevel:
                return x.nextlevel
            return None

    def beginmove(self, event, floor_sprites):
        if event.key == pygame.K_d:
            self.right_move = True
            self.left_move = False
            self.gravity_log = True
        elif event.key == pygame.K_a:
            self.left_move = True
            self.right_move = False
            self.gravity_log = True
        elif event.key == pygame.K_j:
            self.shooting_log = True
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
        elif event.key == pygame.K_j:
            self.shooting_log = False


class Enemy(Person):
    def __init__(self, x, y, *group):
        super().__init__(x, y, "Enemys/Enemy_0.png", *group)
        self.bullet_spawn = 1000

    def moving(self, floor_sprites, hero_sprites):
        if self.oldrunningwasright:
            if check_hero(self.rect.x - 25, self.rect.y + 10, True, hero_sprites):
                if self.bullet_spawn > 50:
                    self.bullet_spawn = 0
                    return Bullet(self.rect.x + 50, self.rect.y + 10, True, 5, "bull_0.png")
                else:
                    self.bullet_spawn += 1
            else:
                self.bullet_spawn = 1000
                if check_block(self.rect.x + 45, self.rect.y + 70, floor_sprites) and\
                        not(check_block(self.rect.x + 45, self.rect.y + 20, floor_sprites)):
                    self.rect.x += 1
                else:
                    self.oldrunningwasright = False
        else:
            if check_hero(self.rect.x - 25, self.rect.y + 10, False, hero_sprites):
                if self.bullet_spawn > 50:
                    self.bullet_spawn = 0
                    return Bullet(self.rect.x - 25, self.rect.y + 10, False, 5, "bull_0.png")
                else:
                    self.bullet_spawn += 1
            else:
                self.bullet_spawn = 1000
                if check_block(self.rect.x - 10, self.rect.y + 70, floor_sprites) and\
                        not (check_block(self.rect.x - 10, self.rect.y + 20, floor_sprites)):
                    self.rect.x -= 1
                else:
                    self.oldrunningwasright = True
        return None
