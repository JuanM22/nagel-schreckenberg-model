import sys, pygame, time

size = width, height = 1366 , 720
black = [0, 0, 0]
white = [255, 255, 255]
red = [255,0,0]
blue = [153, 255, 255]

pygame.display.init()
screen = pygame.display.set_mode(size)

car = pygame.image.load("car.jpg")
carImageSize = car.get_size()
width = carImageSize[0]
print(width)
height = carImageSize[1]

x = 50
y = 30

screen.fill(white)

clock = pygame.time.Clock()

while 1:

    ### 123 px por carril ###
    pygame.event.pump()
    pygame.draw.rect(screen,black,[40, 20, 1316 - width,40],1) # x, y, width, height
    xline = 95
    for i in range(0,23):
        pygame.draw.line(screen, black, [xline,20], [xline, 60])
        xline += 55
    # pygame.draw.rect(screen,black,[40, 70, 1316 - width,40],1) # x, y, width, height

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if(x >= (1316-width)):
        x = 40
        y = 30
    else:
        x+=0.5

    # if(x >= 500 and x <= 550):
    #     y+=1

    screen.blit(car, [x,y])
    pygame.display.flip()
    screen.fill(white)
    clock.tick(350)