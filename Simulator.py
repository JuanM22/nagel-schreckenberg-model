from Vehicle import Vehicle
from Lane import Lane
import sched, random, sys, pygame, time

pygame.display.init()
resolution = pygame.display.Info()
pygame.display.set_mode((resolution.current_w, int((resolution.current_h * 90)/100)))

size = width, height = resolution.current_w, resolution.current_h
black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
blue = [204, 255, 255]
green = [0,255,0]

backgroundImg = pygame.image.load('./screen/background.jpg')
backgroundImg = pygame.transform.scale(backgroundImg, [resolution.current_w, resolution.current_h])

appState = ['Nagel-Schreckenberg Model','Nagel-Schreckenberg Model (Running)','Nagel-Schreckenberg Model (Paused)']

pygame.display.set_caption(appState[1])
screen = pygame.display.set_mode(size)
pygame.font.init()
myfont = pygame.font.SysFont('Arial', 12)
tableFont = pygame.font.SysFont('Arial', 15)

laneList = []

for _ in range(0,3):
    lane = Lane(28, 5)
    laneList.append(lane)
########################################################
brakeProbability = 0.3
########################################################

class LaneSprite(pygame.sprite.Sprite):
    
    def __init__(self,image, xPos, yPos):
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

for _ in range(0, 3):
    laneSprite1 = LaneSprite(laneBackGround,laneX, laneY)
    laneY += 40
    laneSprite.add(laneSprite1)

########################################################
carImages = ['./screen/car1.png','./screen/car2.png','./screen/car3.png','./screen/car4.png','./screen/car5.png']
width = 70
height = 50
########################################################


def createVehicle(lane, x, y):
    if(lane.vehicleList[0] == None):
        imgPos = random.randint(0,4)
        car = pygame.image.load(carImages[imgPos])
        car = pygame.transform.scale(car, (38, 28))
        #########################################################
        vehicleData = setVehicleName(lane)
        car.blit(vehicleData[0],(0,0))
        vehicle = Vehicle(0, 0, brakeProbability, car, x, y, vehicleData[1]) ### Ya tengo nombre ###
        lane.addVehicleToLane(vehicle)
        lane.add(vehicle)

def setVehicleName(lane):
    flag = False
    name = ''
    namePos = 0
    while(not(flag)):
        namePos = random.randint(0,lane.vehicleQuantity -1)
        if(not(lane.vehicleNames[namePos][1])):
            name = lane.vehicleNames[namePos][0]
            lane.vehicleNames[namePos][1] = True
            flag = True
    return [myfont.render(name, False, (0, 0, 0), blue), name]

clock = pygame.time.Clock()

# table = pygame.Surface([200, 25 * (lane.vehicleQuantity + 1)])
buttons = pygame.Surface([resolution.current_w, (resolution.current_h*10)/100])

def renderButtonTable():
    title = tableFont.render('********** Controls **********', False, green)
    buttonsText = tableFont.render('S  >>> Start  ||  R  >>> Restart  ||  Space  >>> Pause  ||  X  >>> Exit', False, green)
    #######################################################
    boardX = (buttons.get_size()[0]* 30) / 100
    boardY = buttons.get_size()[1]
    buttons.blit(title, [(resolution.current_w * 5)/100, (boardY*5)/100])
    buttons.blit(buttonsText, [(resolution.current_w * 5)/100, (boardX*10)/100])
    backgroundImg.blit(buttons, [0, (resolution.current_h*2)/100])

# def renderTable():
#     table.fill(black)
#     x = 0
#     y = 0
#     cellWidth = 100
#     ########### HEADER ###########
#     pygame.draw.rect(table, red, [x, y, cellWidth, cellWidth/4], 1)
#     pygame.draw.rect(table, red, [x+100, y, cellWidth, cellWidth/4], 1)
#     leftCol = tableFont.render('Car', False, green)
#     rightCol = tableFont.render('Speed', False, green)
#     table.blit(leftCol, [(x + 40), (y + 5)])
#     table.blit(rightCol, [(x + 130), (y + 5)])
#     y = 25
#     ##############################
#     for i in range(0, lane.vehicleQuantity):
#         pygame.draw.rect(table, red, [x, y, cellWidth, cellWidth/4], 1)
#         pygame.draw.rect(table, red, [x + 100, y, cellWidth, cellWidth/4], 1)
#         strName = lane.vehicleNames[i][0]
#         speedIndex = -1

#         for j in range(0, lane.vehicleQuantity):
#             vehicle = lane.vehicleList[j]
#             if(vehicle != None):
#                 if(lane.vehicleList[j].name == strName):
#                     speedIndex = j    
#                     break

#         name = tableFont.render(strName, False, green)
#         strSpeed = str(lane.vehicleList[speedIndex].speed) if(speedIndex != -1) else 'N/A'
#         speed = tableFont.render(strSpeed, False, green)
#         table.blit(name,[(x + 40),(y + 5)])
#         table.blit(speed,[(x + 140),(y + 5)])
#         y+=(cellWidth/4)
#     ###############################
#     backgroundImg.blit(table, [50, (resolution.current_h*30)/100])

pause = False
state = 0

def validateLane(lane, x, y):
    if(lane.occupiedCells < lane.vehicleQuantity):
                createVehicle(lane,x,y) # Crea un nuevo vehiculo

def _chargeBeforeAndAfter(lane):
    arr = []
    for i in range(0, len(lane.vehicleList)):
        vehicle = lane.vehicleList[i]
        if(vehicle != None):
            arr.append(vehicle.animation)
    return arr


start = False
renderButtonTable()
screen.blit(backgroundImg, [0,0])
pygame.display.flip()

#######################################################
def isStillAnimate(afterPosList):
    for lane in afterPosList:
        if(True in lane):
            return True
    return False
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

            afterPosList = []
            
            x = 80
            y = (resolution.current_h * 15.8)/100

            for lane in laneList:
                validateLane(lane, x, y)
                lane.updateLane()
                afterPosList.append(_chargeBeforeAndAfter(lane))
                y += 40

            # renderTable()

            while(isStillAnimate(afterPosList)):
                afterPosList = []

                screen.blit(backgroundImg, [0,0])
                laneSprite.draw(screen)
                laneSprite.update()
                for lane in laneList:
                    afterPosList.append(_chargeBeforeAndAfter(lane))
                    lane.draw(screen)
                    lane.update()
                pygame.display.update()
                screen.fill(white)
                clock.tick(250)
                