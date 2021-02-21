import numpy as np

class Lane:

    def __init__(self,vehicleQuantity, maxSpeed):
        self.maxSpeed = maxSpeed
        self.vehicleQuantity = vehicleQuantity
        self.occupiedCells = 0
        self.vehicleList = []
        self.vehicleNames = []
        self.setVehicleNames()
        self._createInitLane()

    def _createInitLane(self):
        for i in range(0,15):
            self.vehicleList.append(None) # Lista vacía

    def addVehicleToLane(self, vehicle):
        if(self.vehicleList.__getitem__(0) == None):
            self.vehicleList[0] = vehicle

    def updateLane(self):
        for vehicle in self.vehicleList:
            if(vehicle != None):
                vehicle.updatePosition(self.checkGap(vehicle),self.maxSpeed)
        for vehicle in self.vehicleList:
            if(vehicle != None):
                if(not(vehicle.checked)):
                    self.vehicleList[vehicle.currentPos] = None
                    if(vehicle.newPos <= len(self.vehicleList) - 1):
                        self.vehicleList[vehicle.newPos] = vehicle
                        vehicle.currentPos = vehicle.newPos
                        vehicle.checked = True
                    else:
                        self.occupiedCells -=1
                        nameIndex = self.vehicleNames.index(self.__getVehicleNameIndex(vehicle.name))
                        self.vehicleNames[nameIndex][1] = False
        self.restartVehicleValues()


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