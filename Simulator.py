from Vehicle import Vehicle
from Lane import Lane
from Road import Road
import sched
import random
import sys
import pygame
import time

pygame.display.init()
resolution = pygame.display.Info()
pygame.display.set_mode(
    (resolution.current_w, int((resolution.current_h * 90)/100)))

vehicleQuantity = 3
mode = 'multi'
# mode = 'single'

size = width, height = resolution.current_w, resolution.current_h
black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
blue = [204, 255, 255]
green = [0, 255, 0]

backgroundImg = pygame.image.load('./screen/background.jpg')
backgroundImg = pygame.transform.scale(
    backgroundImg, [resolution.current_w, resolution.current_h])

appState = ['Nagel-Schreckenberg Model',
            'Nagel-Schreckenberg Model (Running)', 'Nagel-Schreckenberg Model (Paused)']

pygame.display.set_caption(appState[1])
screen = pygame.display.set_mode(size)
pygame.font.init()
myfont = pygame.font.SysFont('Arial', 12)
tableFont = pygame.font.SysFont('Arial', 15)

road = Road()
laneNames = []

for i in range(vehicleQuantity):
    laneNames.append("L" + str(i))

for i in range(0, vehicleQuantity):
    lane = Lane(28, 5, laneNames[i])
    road.lanes.append(lane)
########################################################
brakeProbability = 0.3
########################################################


class LaneSprite(pygame.sprite.Sprite):

    def __init__(self, image, xPos, yPos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = xPos
        self.rect.y = yPos
########################################################


laneBackGround = pygame.image.load('./screen/nagelModelLane.png')
laneX = 70
laneY = (resolution.current_h * 15)/100

laneSprite = pygame.sprite.Group()

for _ in range(0, vehicleQuantity):
    laneSprite1 = LaneSprite(laneBackGround, laneX, laneY)
    laneY += 40
    laneSprite.add(laneSprite1)

########################################################
carImages = ['./screen/car1.png', './screen/car2.png',
             './screen/car3.png', './screen/car4.png', './screen/car5.png']
width = 70
height = 50
########################################################
images = []


def chargeImages():
    for i in range(0, len(carImages)):
        car = pygame.image.load(carImages[i]).convert_alpha()
        car = pygame.transform.scale(car, (38, 28))
        images.append(car)


chargeImages()


def createVehicle(lane, x, y):
    if(lane.vehicleList[0] == None):
        imagePos = random.randint(0, 4)
        car = images[imagePos].copy()
        #########################################################
        vehicle = Vehicle(0, 0, brakeProbability, car, x, y,
                          laneNames.index(lane.name))  # Ya tengo nombre ###
        lane.vehicleList[0] = vehicle
        lane.add(vehicle)
        lane.occupiedCells += 1

def setVehicleName(lane):
    flag = False
    name = ''
    namePos = 0
    while(not(flag)):
        namePos = random.randint(0, lane.vehicleQuantity - 1)
        if(not(lane.vehicleNames[namePos][1])):
            name = lane.vehicleNames[namePos][0]
            lane.vehicleNames[namePos][1] = True
            flag = True
    return [myfont.render(name, False, (0, 0, 0), blue), name]


clock = pygame.time.Clock()

buttons = pygame.Surface([resolution.current_w, (resolution.current_h*10)/100])

def renderButtonTable():
    title = tableFont.render('********** Controls **********', False, green)
    buttonsText = tableFont.render(
        'S  >>> Start  ||  R  >>> Restart  ||  Space  >>> Pause  ||  X  >>> Exit', False, green)
    #######################################################
    boardX = (buttons.get_size()[0] * 30) / 100
    boardY = buttons.get_size()[1]
    buttons.blit(title, [(resolution.current_w * 5)/100, (boardY*5)/100])
    buttons.blit(
        buttonsText, [(resolution.current_w * 5)/100, (boardX*10)/100])
    backgroundImg.blit(buttons, [0, (resolution.current_h*2)/100])

pause = False
state = 0

def validateLane(lane, x, y):
    if(lane.occupiedCells < lane.vehicleQuantity):
        createVehicle(lane, x, y)  # Crea un nuevo vehiculo

def _chargeBeforeAndAfter(lane):
    for vehicle in list(filter(None, lane.vehicleList)):
        if(vehicle.animation):
            return True
    return False

def pushVehicles(y):
    for lane in road.lanes:
        validateLane(lane, x, round(y, 0))
        y += 40

start = False
renderButtonTable()
screen.blit(backgroundImg, [0, 0])
pygame.display.flip()
#######################################################

pygame.display.set_caption(appState[state])

while 1:

    pygame.event.pump()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_x):
                sys.exit()
            elif(event.key == pygame.K_SPACE):
                pause = not(pause)
                state = 2 if(state == 1) else 1
            elif(event.key == pygame.K_s):
                start = True
                state = 1
            pygame.display.set_caption(appState[state])

    if(start):

        if(not(pause)):

            x = 80
            y = (resolution.current_h * 15.8)/100

            pushVehicles(y)
            road.update(mode)

            afterPosList = []

            for lane in road.lanes:
                afterPosList.append(_chargeBeforeAndAfter(lane))

            while(True in afterPosList):

                screen.blit(backgroundImg, [0, 0])
                laneSprite.draw(screen)
                laneSprite.update()
                for i in range(0, len(road.lanes)):
                    lane = road.lanes[i]
                    lane.update()
                    afterPosList[i] = _chargeBeforeAndAfter(lane)
                
                for lane in road.lanes:
                    lane.draw(screen)

                pygame.display.update()
                screen.fill(white)
                # clock.tick(300)
