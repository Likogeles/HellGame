import pygame
import sys

from scenes import Menu, Level1


def terminate():
    pygame.quit()
    sys.exit()


pygame.init()
screen = pygame.display.set_mode((972, 600))


scenename = "menu"
Scene = Menu()


while True:
    if scenename == "quit":
        terminate()
    elif scenename == "menu":
        Scene = Menu()
    elif scenename == "newgame":
        # Сброс базы данных
        Scene = Level1()
        scenename = "level_1"
    # Сюда нужно подставлять остальные сцены по мере их готовности

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

        if scenename == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                scenename = Scene.click(event.pos)
        elif scenename == "level_1":
            print("level_1")
            # Scene.update(event)
        else:
            print("Нет сцены " + scenename)
            terminate()

    Scene.render(screen)
    pygame.display.flip()
