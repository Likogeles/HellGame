import pygame
import sys

from scenes import Menu, Listlevs, Level1, Level2
from functions import load_image


def terminate():
    pygame.quit()
    sys.exit()


pygame.init()
pygame.display.set_caption("Hell Game")
screen = pygame.display.set_mode((972, 600))


scenename = "menu_"
oldscenname = scenename
scenenames = ["newgame", "menu_", "menu", "listlevs_", "listlevs", "level_1", "level1", "level_2", "level2", "quit"]

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
SHOOTINGEVENT = 28
pygame.time.set_timer(SHOOTINGEVENT, 50)

while True:
    if scenename != oldscenname:
        downloadSprites.draw(screen)
        oldscenname = scenename
        pygame.display.flip()
    if scenename == "quit":
        terminate()
    elif scenename == "menu_":
        Scene = Menu()
        scenename= "menu"
    elif scenename == "listlevs_":
        Scene = Listlevs()
        scenename= "listlevs"
    elif scenename == "newgame":
        # Сброс базы данных
        Scene = Level1("Level_1.txt")
        scenename = "level1"
    elif scenename == "level_1":
        Scene = Level1("Level_1.txt")
        scenename = "level1"
    elif scenename == "level_2":
        Scene = Level2("Level_2.txt")
        scenename = "level2"
    # Сюда нужно подставлять остальные сцены по мере их готовности

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if "level" in scenename[:5]:
            if event.type == GRAVITYEVENT:
                x = Scene.gravity()
                if x:
                    scenename = x
            elif event.type == ANIMATEEVENT:
                Scene.animateupdate()
            elif event.type == MOVINGEVENT:
                Scene.movingupdate()
            elif event.type == SHOOTINGEVENT:
                Scene.hero_shoot()

        if scenename == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                scenename = Scene.click(event.pos, screen)
        elif scenename == "listlevs":
            if event.type == pygame.MOUSEBUTTONDOWN:
                scenename = Scene.click(event.pos, screen)
        elif scenename == "level1":
            x = Scene.eventupdate(event)
            if x:
                scenename = x
        elif scenename == "level2":
            x = Scene.eventupdate(event)
            if x:
                scenename = x
        if scenename not in scenenames:
            print("Нет сцены " + scenename)
            terminate()

    Scene.render(screen)
    pygame.display.flip()
