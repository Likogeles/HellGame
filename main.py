import pygame
import sys

from scenes import Menu, Level1


def terminate():
    pygame.quit()
    sys.exit()


pygame.init()
pygame.display.set_caption("Hell Game")
screen = pygame.display.set_mode((972, 600))


scenename = "menu"
Scene = Menu()

MYEVENTTYPE = 30
pygame.time.set_timer(MYEVENTTYPE, 10)
while True:
    if scenename == "quit":
        terminate()
    elif scenename == "menu":
        Scene = Menu()
    elif scenename == "newgame" or scenename == "level_1":
        # Сброс базы данных
        Scene = Level1()
        scenename = "level1"
    # Сюда нужно подставлять остальные сцены по мере их готовности

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if "level" in scenename[:5] and event.type == MYEVENTTYPE:
            Scene.gravity()

        if scenename == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                scenename = Scene.click(event.pos)
        elif scenename == "level1":
            Scene.update(event)
        else:
            print("Нет сцены " + scenename)
            terminate()

    Scene.render(screen)
    pygame.display.flip()
