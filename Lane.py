from Vehicle import Vehicle
import pygame, random, ModelData as data

class Lane(pygame.sprite.Group):

    def __init__(self,vehicleQuantity, maxSpeed, name):
        pygame.sprite.Group.__init__(self)
        self.maxSpeed = maxSpeed
        self.vehicleQuantity = vehicleQuantity
        self.occupiedCells = 0
        self.vehicleList = []
        self.__createInitLane()
        self.name = name

    def __createInitLane(self):
        self.vehicleList += [None] * self.vehicleQuantity # Lista vacía

    def createVehicle(self, x, y, car):
        if(self.occupiedCells < self.vehicleQuantity):
            if(self.vehicleList[0] == None):
                vehicle = Vehicle(0, 0, car, x, y, data.laneNames.index(self.name))
                self.vehicleList[0] = vehicle
                self.add(vehicle)
                self.occupiedCells += 1

    def restartVehicleValues(self):
        for vehicle in list(filter(None, self.vehicleList)):
            vehicle.checked = False

    def checkVehicleGap(self, vehicle):
        v = self.vehicleList[vehicle.currentPos]
        if(v != vehicle):
            self.occupiedCells -=1
            v.kill()
        start = vehicle.currentPos + 1
        end = 0
        if(start == len(self.vehicleList)):
            end = len(self.vehicleList)
        else:
            for i in range(start, len(self.vehicleList)):
                if(self.vehicleList[i] == None):
                    end +=1
                else:
                    return end
        return end

    def stillAnimate(self):
        for vehicle in list(filter(None, self.vehicleList)):
            if(vehicle.animation):
                return True
        return False