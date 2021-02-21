from Vehicle import Vehicle
from Lane import Lane
import sched
import random
import sys
import pygame

######################################
size = width, height = 1366, 720
black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
blue = [153, 255, 255]

pygame.display.init()
pygame.display.set_caption('Nagel-Schreckenberg Model')
screen = pygame.display.set_mode(size)

x = 55
y = 20

screen.fill(white)
######################################

lane = Lane(15, 5)
brakeProbability = 0.3

carImages = ['./screen/car.jpg','./screen/car2.jpg','./screen/car3.jpg','./screen/car4.jpg']
width = 45
height = 20

def createVehicle():
    if(lane.vehicleList[0] == None):
        imgPos = random.randint(0,3)
        car = pygame.image.load(carImages[imgPos])
        car.convert()
        vehicle = Vehicle(0, 0, brakeProbability, car, x, y)
        lane.addVehicleToLane(vehicle)
        lane.occupiedCells += 1

# def printLand():
#     data = ''
#     for vehicle in lane.vehicleList:
#         if(vehicle != None):
#             data += str(vehicle.name)+' '
#         else:
#             data += '0 '
#     print(data, end='\r')

clock = pygame.time.Clock()

while 1:

    if(lane.occupiedCells < lane.vehicleQuantity):
        createVehicle() # Crea un nuevo vehiculo
    ############################################################
    pygame.event.pump()
    pygame.draw.rect(screen, black, [50, 20, 1315 - width, 40], 2)

    xline = 105
    for i in range(0, 23):
        pygame.draw.line(screen, black, [xline, 20], [xline, 60])
        xline += 55

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    beforePos = []
    for i in range(0, len(lane.vehicleList)):
        vehicle = lane.vehicleList[i]
        if(vehicle != None):
            beforePos.append([55 * (vehicle.currentPos + 1), False])

    lane.updateLane()

    afterPos = []
    for i in range(0, len(lane.vehicleList)):
        vehicle = lane.vehicleList[i]
        if(vehicle != None):
            afterPos.append([vehicle.xPos, i])

    counter = 0

    if(len(beforePos) > len(afterPos)):
        pos = len(beforePos) - 1
        beforePos.remove(beforePos[pos])

    while(counter < len(beforePos)):
        pygame.draw.rect(screen, black, [50, 20, 1315 - width, 40], 2)

        xline = 105
        for i in range(0, 23):
            pygame.draw.line(screen, black, [xline, 20], [xline, 60])
            xline += 55


        for i in range(0, len(afterPos)):
            if(beforePos[i][0] <= (afterPos[i][0]+0.5)):
                beforePos[i][0] += 0.5
            else:
                if(not(beforePos[i][1])):
                  counter += 1
                  beforePos[i][1] = True

        images = []
        for i in range(0, len(afterPos)):
            position = afterPos[i][1]
            vehicle = lane.vehicleList[position]
            images.append([vehicle.image, [beforePos[i][0], vehicle.yPos]])

        screen.blits(images)
        clock.tick(500)
        pygame.display.flip()
        screen.fill(white)
        images.clear()

    screen.fill(white)
