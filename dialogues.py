import pygame

from functions import check_plot, click_wait, saving_plot, saving_guns


def dialog_with_AGT(self, screen, x):
    pygame.mouse.set_visible(True)
    if check_plot() == 0:
        self.dialog_sprites.draw(screen)
        screen.blit(self.dialog_namefont.render(x[12:], 1, (0, 0, 0)), (115, 370))
        screen.blit(self.dialog_font.render("Рад приветствовать вас, Робот-Наёмник РН-42. Как вам", 1, (0, 0, 0)), (110, 430))
        screen.blit(self.dialog_font.render("уже известно, во время раскопок в нашей шахте было", 1, (0, 0, 0)), (110, 455))
        screen.blit(self.dialog_font.render("обнаружено агрессивно-настроенное существо, которое каким-то образом", 1, (0, 0, 0)), (110, 480))
        screen.blit(self.dialog_font.render("смогло захватить некоторую нашу шахтёрскую технику.", 1, (0, 0, 0)), (110, 505))
        pygame.display.flip()
        click_wait()

        self.dialog_sprites.draw(screen)
        screen.blit(self.dialog_namefont.render(x[12:], 1, (0, 0, 0)), (115, 370))
        screen.blit(self.dialog_font.render("Чем дольше работа в шахте стоит, тем дольше страна", 1, (0, 0, 0)), (110, 430))
        screen.blit(self.dialog_font.render("остаётся без поставок медной руды. Сначала вам", 1, (0, 0, 0)), (110, 455))
        screen.blit(self.dialog_font.render("необходимо освободить моих коллег из плена этого существа.", 1, (0, 0, 0)), (110, 480))
        screen.blit(self.dialog_font.render("Первый - ИЛД1v108. Он прячется в Мат. офисе на третьем уровне.", 1, (0, 0, 0)), (110, 505))
        pygame.display.flip()
        click_wait()

        self.dialog_sprites.draw(screen)
        screen.blit(self.dialog_namefont.render(x[12:], 1, (0, 0, 0)), (115, 370))
        screen.blit(self.dialog_font.render("Думаю, вы с лёгкостью сломаете ящики, которыми", 1, (0, 0, 0)), (110, 430))
        screen.blit(self.dialog_font.render("я забарикадировал своих товарищей в ловушке с", 1, (0, 0, 0)), (110, 455))
        screen.blit(self.dialog_font.render("захваченной техникой. Само собой, я сделал это ради", 1, (0, 0, 0)), (110, 480))
        screen.blit(self.dialog_font.render("общей безопасности.", 1, (0, 0, 0)), (110, 505))
        pygame.display.flip()
        click_wait()
    elif check_plot() == 1:
        self.dialog_sprites.draw(screen)
        screen.blit(self.dialog_namefont.render(x[12:], 1, (0, 0, 0)), (115, 370))
        screen.blit(self.dialog_font.render("Похоже у ИЛД1v108 есть что-то для тебя", 1, (0, 0, 0)), (110, 430))
        pygame.display.flip()
        click_wait()
    elif check_plot() == 2:
        self.dialog_sprites.draw(screen)
        screen.blit(self.dialog_namefont.render(x[12:], 1, (0, 0, 0)), (115, 370))
        screen.blit(self.dialog_font.render("Похоже что СИНУС-ПУШКА компенсирует", 1, (0, 0, 0)), (110, 430))
        screen.blit(self.dialog_font.render("тебе отсутствие коленей. Теперь ты сможешь", 1, (0, 0, 0)), (110, 455))
        screen.blit(self.dialog_font.render("попасть в Мед. оффис, в котором прячется ПЛН0v105", 1, (0, 0, 0)), (110, 480))
        screen.blit(self.dialog_font.render("Спасёшь его и, может, получишь что-то новое.", 1, (0, 0, 0)), (110, 505))
        pygame.display.flip()
        click_wait()
    else:
        print("Этого диалога ещё нет")

    pygame.mouse.set_visible(False)


def dialog_with_ILD(self, screen, x):
    pygame.mouse.set_visible(True)
    if check_plot() == 0:
        self.dialog_sprites.draw(screen)
        screen.blit(self.dialog_namefont.render(x[12:], 1, (0, 0, 0)), (115, 370))
        screen.blit(self.dialog_font.render("Рад приветствовать вас, Робот-Наёмник РН-42.", 1, (0, 0, 0)),
                    (110, 430))
        screen.blit(self.dialog_font.render("Скорее возвращаемcя на главную площадь!", 1, (0, 0, 0)),
                    (110, 455))
        pygame.display.flip()
        saving_plot(1)
        click_wait()
        return "level_1"
    elif check_plot() == 1:
        self.dialog_sprites.draw(screen)
        screen.blit(self.dialog_namefont.render(x[12:], 1, (0, 0, 0)), (115, 370))
        screen.blit(self.dialog_font.render("Спасибо, что спас меня. Знаешь, пока я был", 1, (0, 0, 0)),
                    (110, 430))
        screen.blit(self.dialog_font.render("в MathHell я разработал новый вид оружия", 1, (0, 0, 0)),
                    (110, 455))
        screen.blit(self.dialog_font.render("Я назвал его СИНУС-ПУШКА (tm). В знак моей благодарности за", 1, (0, 0, 0)), (110, 480))
        screen.blit(self.dialog_font.render("спасение, ты можешь взять тестовый образец.", 1, (0, 0, 0)), (110, 505))
        saving_guns(1)
        saving_plot(2)
        pygame.display.flip()
        click_wait()
    elif check_plot() == 2:
        self.dialog_sprites.draw(screen)
        screen.blit(self.dialog_namefont.render(x[12:], 1, (0, 0, 0)), (115, 370))
        screen.blit(self.dialog_font.render("Спаси ПЛН0v105!", 1, (0, 0, 0)),
                    (110, 430))
        pygame.display.flip()
        click_wait()
    else:
        print("Этого диалога ещё нет")


def dialog_with_PLN(self, screen, x):
    pygame.mouse.set_visible(True)
    if check_plot() == 0:
        print("lol")