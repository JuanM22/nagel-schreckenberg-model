import sys, pygame, time

size = width, height = 1366 , 720
black = [0, 0, 0]
white = [255, 255, 255]
red = [255,0,0]
blue = [153, 255, 255]

screen = pygame.display.set_mode(size)
screen.fill(white)

pygame.display.init()

while 1:
    pygame.event.pump()
    time.sleep(0.1)
    pygame.draw.rect(screen,black,[250, 150, 70,45],0) # x, y, width, height
    pygame.draw.rect(screen,red,[250, 140, 25,10],0) # x, y, width, height
    pygame.draw.rect(screen,red,[250, 195, 25,10],0) # x, y, width, height
    pygame.draw.rect(screen,red,[295, 140, 25,10],0) # x, y, width, height
    pygame.draw.rect(screen,red,[295, 195, 25,10],0) # x, y, width, height
    pygame.draw.rect(screen,blue,[305, 152, 10,40],0) # x, y, width, height
    pygame.display.flip()