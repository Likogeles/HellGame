import pygame
import sys
import time

from scenes import Menu, Level1
from functions import load_image

def terminate():
    pygame.quit()
    sys.exit()


pygame.init()
pygame.display.set_caption("Hell Game")
screen = pygame.display.set_mode((972, 600))


scenename = "menu"
oldscenname = scenename

download_image = pygame.sprite.Sprite()
download_image.image = load_image("download.png")
download_image.rect = download_image.image.get_rect()
download_image.rect.x = 0
download_image.rect.y = 0

downloadSprites = pygame.sprite.Group()
downloadSprites.add(download_image)

Scene = Menu()

GRAVITYEVENT = 30
pygame.time.set_timer(GRAVITYEVENT, 10)
ANIMATEEVENT = 31
pygame.time.set_timer(ANIMATEEVENT, 80)
MOVINGEVENT = 29
pygame.time.set_timer(MOVINGEVENT, 20)

while True:
    if scenename != oldscenname:
        downloadSprites.draw(screen)
        oldscenname = scenename
        pygame.display.flip()
    if scenename == "quit":
        terminate()
    elif scenename == "menu":
        Scene = Menu()
    elif scenename == "newgame" or scenename == "level_1":
        # Сброс базы данных
        Scene = Level1("Level_1.txt")
        scenename = "level1"
    # Сюда нужно подставлять остальные сцены по мере их готовности

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if "level" in scenename[:5]:
            if event.type == GRAVITYEVENT:
                Scene.gravity()
            elif event.type == ANIMATEEVENT:
                Scene.animateupdate()
            elif event.type == MOVINGEVENT:
                Scene.movingupdate()

        if scenename == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                scenename = Scene.click(event.pos, screen)
        elif scenename == "level1":
            x = Scene.eventupdate(event, screen)
            if x:
                scenename = x
        else:
            print("Нет сцены " + scenename)
            terminate()

    Scene.render(screen)
    pygame.display.flip()
