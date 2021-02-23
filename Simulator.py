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

x = 80
y = (resolution.current_h * 16.5)/100

lane = Lane(5, 5)
brakeProbability = 0.3

laneBackGround = pygame.image.load('./screen/nagelModelLane.png')
carImages = ['./screen/car1.png','./screen/car2.png','./screen/car3.png','./screen/car4.png','./screen/car5.png']
width = 70
height = 50

def createVehicle():
    if(lane.vehicleList[0] == None):
        imgPos = random.randint(0,4)
        car = pygame.image.load(carImages[imgPos])
        vehicleData = setVehicleName()
        car.blit(vehicleData[0],(0,0))
        vehicle = Vehicle(0, 0, brakeProbability, car, x, y, vehicleData[1], imgPos+1) ### Ya tengo nombre ###
        lane.addVehicleToLane(vehicle)

def setVehicleName():
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

table = pygame.Surface([200, 25 * (lane.vehicleQuantity + 1)])
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

def renderTable():
    table.fill(black)
    x = 0
    y = 0
    cellWidth = 100
    ########### HEADER ###########
    pygame.draw.rect(table, red, [x, y, cellWidth, cellWidth/4], 1)
    pygame.draw.rect(table, red, [x+100, y, cellWidth, cellWidth/4], 1)
    leftCol = tableFont.render('Car', False, green)
    rightCol = tableFont.render('Speed', False, green)
    table.blit(leftCol, [(x + 40), (y + 5)])
    table.blit(rightCol, [(x + 130), (y + 5)])
    y = 25
    ##############################
    for i in range(0, lane.vehicleQuantity):
        pygame.draw.rect(table, red, [x, y, cellWidth, cellWidth/4], 1)
        pygame.draw.rect(table, red, [x + 100, y, cellWidth, cellWidth/4], 1)
        strName = lane.vehicleNames[i][0]
        speedIndex = -1

        for j in range(0, lane.vehicleQuantity):
            vehicle = lane.vehicleList[j]
            if(vehicle != None):
                if(lane.vehicleList[j].name == strName):
                    speedIndex = j    
                    break

        name = tableFont.render(strName, False, green)
        strSpeed = str(lane.vehicleList[speedIndex].speed) if(speedIndex != -1) else 'N/A'
        speed = tableFont.render(strSpeed, False, green)
        table.blit(name,[(x + 40),(y + 5)])
        table.blit(speed,[(x + 140),(y + 5)])
        y+=(cellWidth/4)
    ###############################
    backgroundImg.blit(table, [50, (resolution.current_h*30)/100])

pause = False
state = 1

def printSpeed():
    for vehicle in lane.vehicleList:
        if(vehicle!=None):
            print(vehicle.speed,' ', end='')
    print('\n*********************************')

def _chargeBeforeAndAfter(type):
    arr = []
    for i in range(0, len(lane.vehicleList)):
        vehicle = lane.vehicleList[i]
        if(vehicle != None):
            if(type == 'before'):
                arr.append([vehicle.xPos, False])
            else:
                arr.append([vehicle.xPos, i])
    return arr

# pygame.time.delay(3000)

start = False
renderButtonTable()
screen.blit(backgroundImg, [0,0])
pygame.display.flip()

while 1:
    
    if(lane.occupiedCells < lane.vehicleQuantity):
        createVehicle() # Crea un nuevo vehiculo
    ############################################################
    pygame.event.pump()

    # screen.blit(backgroundImg, [0,0])
    # screen.blit(laneBackGround, [70,20])

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_x):
                sys.exit()
            elif(event.key == pygame.K_SPACE):
                pause = not(pause)
                state = 2 if (state == 1) else 1
                pygame.display.set_caption(appState[state])
            elif(event.key == pygame.K_s):
                start = True

    if(start):

        if(not(pause)):
    
            renderTable()

            beforePos = _chargeBeforeAndAfter('before')
            lane.updateLane()
            afterPos = _chargeBeforeAndAfter('after')

            counter = 0

            if(len(beforePos) > len(afterPos)):
                beforePos.remove(beforePos[len(beforePos) - 1])

            while(counter < len(beforePos)):
        
                for i in range(0, len(afterPos)):
                    if(beforePos[i][0] <= (afterPos[i][0])):
                        beforePos[i][0] += 2
                    else:
                        if(not(beforePos[i][1])):
                            counter += 1
                            beforePos[i][1] = True

                images = []
                images.append([laneBackGround,[70,(resolution.current_h * 15)/100]])
                for i in range(0, len(afterPos)):
                    position = afterPos[i][1]
                    vehicle = lane.vehicleList[position]
                    images.append([vehicle.image, [beforePos[i][0], vehicle.yPos]])

                backgroundImg.blits(images)
                screen.blit(backgroundImg, [0,0])
                pygame.display.flip()
                images.clear()
        
        # pygame.time.delay(500)
    