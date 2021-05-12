import numpy as np
import pygame

class Lane(pygame.sprite.Group):

    def __init__(self,vehicleQuantity, maxSpeed, name):
        pygame.sprite.Group.__init__(self)
        self.maxSpeed = maxSpeed
        self.vehicleQuantity = vehicleQuantity
        self.occupiedCells = 0
        self.vehicleList = []
        self._createInitLane()
        self.name = name

    def _createInitLane(self):
        self.vehicleList += [None] * self.vehicleQuantity # Lista vacía

    def restartVehicleValues(self):
        for vehicle in list(filter(None, self.vehicleList)):
            vehicle.checked = False

    def checkGap(self, vehicle):
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