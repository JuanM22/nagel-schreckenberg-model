import sys
import pygame
import time

size = width, height = 1366, 720
black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
blue = [153, 255, 255]

pygame.display.init()
screen = pygame.display.set_mode(size)


pygame.font.init()
myfont = pygame.font.SysFont('Arial', 12)
textsurface = myfont.render('V1', False, (0, 0, 0), blue)

car = pygame.image.load("car1.png", "imagen1")
car_rect = car.get_rect()

carImageSize = car.get_size()
width = carImageSize[0]
height = carImageSize[1]

# car.blit(textsurface, ((width*35)/100, 0))

# car_rect.x = 50
# car_rect.y = 25

screen.fill(white)

clock = pygame.time.Clock()
imagesSprite = pygame.sprite.Group()

###########################################################
class Enemy(pygame.sprite.Sprite):  # classe do inimigo
    def __init__(self, image, xPos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.speed = 1
        self.rect = image.get_rect()  # posição aleatória, dentro dos limites
        self.rect.x = xPos
        self.alive = True

    def update(self):
        if(self.speed > 0):
            self.rect.x += 1
            self.speed = self.speed + 1
            if(self.speed == 100):
                self.speed = 0
###########################################################

xPos = 80

for _ in range(0, 5):
    vehicle = Enemy(car, xPos)
    imagesSprite.add(vehicle)
    xPos += 80

while 1:

    pygame.event.pump()

    imagesSprite.draw(screen)
    imagesSprite.update()

    # # x, y, width, height
    # pygame.draw.rect(screen, black, [40, 20, 1316 - width, 50], 1)
    # xline = 95
    # for i in range(0, 23):
    #     pygame.draw.line(screen, black, [xline, 20], [xline, 70])
    #     xline += 55
    # # pygame.draw.rect(screen,black,[40, 70, 1316 - width,40],1) # x, y, width, height

    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         sys.exit()

    # if(car_rect.x >= (1316-width)):
    #     car_rect.x = 40
    #     car_rect.y = 25
    # else:
    #     car_rect.x += 1

    # print(car_rect)

    # screen.blit(car, [car_rect.x, car_rect.y])
    pygame.display.flip()
    screen.fill(white)
    clock.tick(150)
