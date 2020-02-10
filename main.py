import pygame

from scenes import Menu, Listlevs, Level1, Level2, Level3
from functions import load_image, terminate, check_location, new_game_save


# поставь pygame.init() после pygame.mixer.init() чтобы небыло задержки звука выстрелов
# но тогда у музыки будут артефакты
# не забудь исправить этот косяк!

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
pygame.init()


pygame.display.set_caption("Hell Game")
screen = pygame.display.set_mode((972, 600))

pygame.mixer.music.load("data/Music/themesound.mp3")
pygame.mixer.music.set_volume(0.1)

scenename = "menu_"
oldscenname = scenename
scenenames = ["newgame", "menu_", "menu", "continue", "listlevs_", "listlevs",
              "level_1", "level1", "level_2", "level2", "level_3", "level3", "quit"]

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
ENEMYANIMATEEVENT = 27
pygame.time.set_timer(ENEMYANIMATEEVENT, 200)

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
        pygame.mixer.music.set_volume(0.1)
    elif scenename == "listlevs_":
        Scene = Listlevs()
        scenename= "listlevs"
    elif scenename == "newgame":
        new_game_save()
        Scene = Level1("Level_1.txt")
        scenename = "level1"
    elif scenename == "continue":
        pygame.mixer.music.set_volume(0.1)
        if check_location() == 1:
            Scene = Level1("Level_1.txt")
            scenename = "level1"
        elif check_location() == 2:
            Scene = Level2("Level_2.txt")
            scenename = "level2"
        elif check_location() == 3:
            Scene = Level3("Level_3.txt")
            scenename = "level3"
            pygame.mixer.music.set_volume(0.4)
    elif scenename == "level_1":
        Scene = Level1("Level_1.txt")
        scenename = "level1"
        pygame.mixer.music.set_volume(0.1)
    elif scenename == "level_2":
        Scene = Level2("Level_2.txt")
        scenename = "level2"
        pygame.mixer.music.set_volume(0.1)
    elif scenename == "level_3":
        Scene = Level3("Level_3.txt")
        scenename = "level3"
        pygame.mixer.music.set_volume(0.2)
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
            elif event.type == ENEMYANIMATEEVENT:
                Scene.enemyanimateupdate()
            elif event.type == MOVINGEVENT:
                Scene.movingupdate()
            elif event.type == SHOOTINGEVENT:
                Scene.hero_shoot()
            x = Scene.eventupdate(event, screen)
            if x:
                scenename = x

        if scenename == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                scenename = Scene.click(event.pos, screen)
        elif scenename == "listlevs":
            if event.type == pygame.MOUSEBUTTONDOWN:
                scenename = Scene.click(event.pos, screen)

        if scenename not in scenenames:
            print("Нет сцены " + scenename)
            terminate()

    Scene.render(screen)
    pygame.display.flip()
