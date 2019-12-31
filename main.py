import pygame
import sys

from scenes import Menu


def terminate():
    pygame.quit()
    sys.exit()


pygame.init()
screen = pygame.display.set_mode((972, 600))
screen.fill((0, 0, 0))


scenename = "menu"
Scene = Menu()


while True:
    if scenename == "quit":
        terminate()
    elif scenename == "menu":
        Scene = Menu()
    # Сюда нужно подставлять остальные сцены по мере их готовности

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

        if scenename == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                scenename = Scene.click(event.pos)
        else:
            print(scenename)
            scenename = "menu"

    Scene.render(screen)
    pygame.display.flip()
