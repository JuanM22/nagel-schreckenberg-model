import pygame
import Colors

mode_selector = 0

pygame.display.init()
resolution = pygame.display.Info()
size = width, height = resolution.current_w, resolution.current_h
pygame.display.set_mode((width, int((height * 90)/100)))
screen = pygame.display.set_mode(size)
pygame.font.init()
myfont = pygame.font.SysFont('Arial', 12)
tableFont = pygame.font.SysFont('Arial', 15)

on = pygame.image.load('./resources/car1.png', 'onBtn')
on_rect = on.get_rect()

on_rect.x = 250
on_rect.y = 250

off = pygame.image.load('./resources/car2.png')
off_rect = off.get_rect()
off_rect.x = 330
off_rect.y = 250

btn_image = on

txt = '0'

modeText = tableFont.render('Mode  >>> ', False, Colors.black)
screen.blit(modeText, [150, 250])
pygame.display.update()

perc_value = tableFont.render(txt, False, Colors.black)

# print(perc_value.text)

while 1:

    pygame.event.pump()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mpos = pygame.mouse.get_pos()  # Get mouse position
            if on_rect.collidepoint(mpos):
                intval = int(txt)
                if(intval > 0):
                    intval -= 5
                    txt = str(intval)
            elif off_rect.collidepoint(mpos):
                intval = int(txt)
                if(intval < 75):
                    intval += 5
                    txt = str(intval)
            #     perc_pos = min(len(percs)-1, perc_pos+1)
                # if(mode_selector == 1):
                #     mode_selector = 0
                #     btn_image = off
                # else:
                #     mode_selector = 1
                #     btn_image = on
            perc_value = tableFont.render(txt, False, Colors.black)

    screen.fill(Colors.white)
    screen.blit(perc_value, [270,200])
    screen.blit(on, [on_rect.x, on_rect.y])
    screen.blit(off, [off_rect.x, off_rect.y])
    pygame.display.update()
