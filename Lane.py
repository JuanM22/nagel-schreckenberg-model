import numpy as np
import pygame

class Lane(pygame.sprite.Group):

    def __init__(self,vehicleQuantity, maxSpeed, name):
        pygame.sprite.Group.__init__(self)
        self.maxSpeed = maxSpeed
        self.vehicleQuantity = vehicleQuantity
        self.occupiedCells = 0
        self.vehicleList = []
        self.vehicleNames = []
        self.setVehicleNames()
        self._createInitLane()
        self.name = name

    def _createInitLane(self):
        self.vehicleList += [None] * self.vehicleQuantity # Lista vacía

    def checkGap(self, vehicle):
        start = self.vehicleList.index(vehicle) + 1
        end = 0
        if(start == len(self.vehicleList)):
            end = len(self.vehicleList)
        else:
            for i in range(start, len(self.vehicleList)):
                if(self.vehicleList.__getitem__(i) == None):
                    end +=1
                else:
                    break
        return end

    def carCounter(self):
        counter = 0
        for vehicle in self.vehicleList:
            if(vehicle!=None):
                counter+=1
        return counter

    def restartVehicleValues(self):
        for vehicle in self.vehicleList:
            if(vehicle != None):
              vehicle.checked = False

    def setVehicleNames(self):
        for i in range(0, self.vehicleQuantity):
            self.vehicleNames.append(['V'+str(i+1), False])
    
    def __getVehicleNameIndex(self, name):
        data = []
        for i in range(0, len(self.vehicleNames)):
            arr = self.vehicleNames[i]
            if(arr[0] == name):
                data = arr
                break
        return data