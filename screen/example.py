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
height = carImageSize[1]

x = 50
y = 30

screen.fill(white)

while 1:

    ### 123 px por carril ###
    pygame.event.pump()
    pygame.draw.rect(screen,black,[40, 20, 1316 - width,40],1) # x, y, width, height
    # pygame.draw.rect(screen,black,[40, 70, 1316 - width,40],1) # x, y, width, height

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if(x >= (1316-width)):
        x = 50
        y = 30
    else:
        x+=1

    # if(x >= 500 and x <= 550):
    #     y+=1

    screen.blit(car, [x,y])
    pygame.display.flip()
    screen.fill(white)
    time.sleep(0.005)