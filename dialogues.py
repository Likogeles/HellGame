import pygame

from functions import check_plot, click_wait


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
        screen.blit(self.dialog_font.render("Первый - ИЛД1v118. Он прячется в Офиссе на третьем уровне.", 1, (0, 0, 0)), (110, 505))
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

    pygame.mouse.set_visible(False)