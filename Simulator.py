from Vehicle import Vehicle
from Lane import Lane
import sched
import time
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
screen = pygame.display.set_mode(size)

car = pygame.image.load("./screen/car.jpg")
carImageSize = car.get_size()
width = carImageSize[0]
height = carImageSize[1]

x = 50
y = 30

screen.fill(white)
######################################

lane = Lane(6, 2)
v = [1, 2, 3, 4, 5, 6]
brakeProbability = 0.3

v1 = Vehicle(2, 0, brakeProbability, car, x, y)
x += width+10
v2 = Vehicle(1, 2, brakeProbability, car, x, y)
x += width+10
v3 = Vehicle(1, 5, brakeProbability, car, x, y)
x += width+10
v4 = Vehicle(0, 6, brakeProbability, car, x, y)

lane.vehicleList[0] = v1
lane.vehicleList[2] = v2
lane.vehicleList[5] = v3
lane.vehicleList[6] = v4


def createVehicle():
    if(lane.vehicleList[0] == None):
        vehicle = Vehicle(0, 0, 'V'+str(v.pop()), brakeProbability)
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

# printLand()

s = sched.scheduler(time.time, time.sleep)


def startSimulation(sc):
    # if(lane.occupiedCells < lane.vehicleQuantity):
    #     createVehicle() # Crea un nuevo vehiculo
    # lane.updateLane()
    ############################################################
    ### 123 px por carril ###
    pygame.event.pump()
    # x, y, width, height
    pygame.draw.rect(screen, black, [40, 20, 1316 - width, 40], 1)
    # pygame.draw.rect(screen,black,[40, 70, 1316 - width,40],1) # x, y, width, height

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # if(x >= (1316-width)):
    #     x = 50
    #     y = 30
    # else:
    #     x += 1

    # if(x >= 500 and x <= 550):
    #     y+=1

    for vehicle in lane.vehicleList:
        if(vehicle != None):
            rect = vehicle.image.get_rect()
            screen.blit(vehicle.image, [vehicle.xPos, vehicle.yPos])
            vehicle.xPos += vehicle.image.get_size()[0] + 10
    
    # rect = lane.vehicleList[0].image.get_rect()
    # screen.blit(lane.vehicleList[0].image, [lane.vehicleList[0].xPos, lane.vehicleList[0].yPos])
    # rect.x += lane.vehicleList[0].image.get_size()[0] + 10

    pygame.display.flip()
    screen.fill(white)
    # time.sleep(0.005)
    ############################################################
    # printLand()
    s.enter(2, 1, startSimulation, (sc,))


s.enter(1, 1, startSimulation, (s,))
s.run()
