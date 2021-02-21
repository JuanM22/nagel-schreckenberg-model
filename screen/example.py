import sys, pygame, time

size = width, height = 1366 , 720
black = [0, 0, 0]
white = [255, 255, 255]
red = [255,0,0]
blue = [153, 255, 255]

pygame.display.init()
screen = pygame.display.set_mode(size)


pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.

myfont = pygame.font.SysFont('Arial', 12)
textsurface = myfont.render('V1', False, (0, 0, 0), blue)

car = pygame.image.load("car.jpg", "imagen1")

carImageSize = car.get_size()
width = carImageSize[0]
height = carImageSize[1]

car.blit(textsurface,((width*35)/100,0))

x = 50
y = 25

screen.fill(white)

clock = pygame.time.Clock()

while 1:

    # pygame.display.flip()

    ### 123 px por carril ###
    pygame.event.pump()
    pygame.draw.rect(screen,black,[40, 20, 1316 - width,50],1) # x, y, width, height
    xline = 95
    for i in range(0,23):
        pygame.draw.line(screen, black, [xline,20], [xline, 70])
        xline += 55
    # pygame.draw.rect(screen,black,[40, 70, 1316 - width,40],1) # x, y, width, height

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if(x >= (1316-width)):
        x = 40
        y = 25
    else:
        x+=0.5

    screen.blit(car, [x,y])
    pygame.display.flip()
    screen.fill(white)
    clock.tick(350)