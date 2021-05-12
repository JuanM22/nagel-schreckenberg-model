class Road ():
    
    def __init__(self):
        self.lanes = []

    def update(self, mode):
        if(mode == 'single'):
            self.singleLaneUpdate()
        else:
            self.multiLaneUpdate()

    def singleLaneUpdate(self):
        lane = self.lanes[0]
        for vehicle in lane.vehicleList:
            if(vehicle != None):
                if(not(vehicle.checked)):
                    vehicle.singleLaneUpdatePosition(lane.checkGap(vehicle),lane.maxSpeed)
                    lane.vehicleList[vehicle.currentPos] = None
                    if(vehicle.newPos < len(lane.vehicleList)):
                        lane.vehicleList[vehicle.newPos] = vehicle
                        vehicle.currentPos = vehicle.newPos
                        vehicle.checked = True
                    else:
                        lane.occupiedCells -=1
                        # nameIndex = lane.vehicleNames.index(lane.__getVehicleNameIndex(vehicle.name))
                        # lane.vehicleNames[nameIndex][1] = False
                        vehicle.kill()
        lane.restartVehicleValues()

    def multiLaneUpdate(self):
        for lane in self.lanes:
            for vehicle in lane.vehicleList:
                if(vehicle != None):
                    if(not(vehicle.checked)):
                        ############ Data for second rule ###########
                        movement = self.validateSideMovement(vehicle) ## MOVE UP OR DOWN ##
                        gaps = []
                        if(movement == 'UP'):
                            gaps = [self.forwardGap(self.lanes[vehicle.lane - 1], vehicle.currentPos), self.backwardGap(lane, vehicle.currentPos)]
                        elif(movement == 'DOWN'):
                            gaps = [self.forwardGap(self.lanes[vehicle.lane + 1], vehicle.currentPos), self.backwardGap(lane, vehicle.currentPos)]
                        #####################################################################
                        currentLane = vehicle.lane ## Carril actual ###
                        vehicle.multiLaneUpdatePosition(lane.checkGap(vehicle), gaps,lane.maxSpeed, movement)
                        if(vehicle.lane == currentLane):
                            movement = 'N/A'
                        lane.vehicleList[vehicle.currentPos] = None
                        vehicle.checked = True
                        if(movement != 'N/A'):
                            lane.occupiedCells -=1
                            self._changeLanesVehicle(vehicle)
                        else:
                            if(vehicle.newPos < len(lane.vehicleList)):
                                lane.vehicleList[vehicle.newPos] = vehicle
                                vehicle.currentPos = vehicle.newPos
                            else:
                                lane.occupiedCells -=1
                                # nameIndex = lane.vehicleNames.index(lane.__getVehicleNameIndex(vehicle.name))
                                # lane.vehicleNames[nameIndex][1] = False
                                vehicle.kill()
            lane.restartVehicleValues()

    def _changeLanesVehicle(self, vehicle):
        lane = self.lanes[vehicle.lane]
        lane.vehicleList[vehicle.currentPos] = vehicle
        vehicle.kill()
        lane.add(vehicle)
        lane.occupiedCells += 1

    def validateSideMovement(self, vehicle):
        moveUp = (vehicle.lane - 1) >= 0
        moveDown = (vehicle.lane + 1) < len(self.lanes)
        #######################################################
        if(moveUp):
            laneOne = self.lanes[vehicle.lane - 1] ## UP
            if(laneOne.vehicleList[vehicle.currentPos] == None):
                return 'UP'
        if(moveDown):
            laneTwo = self.lanes[vehicle.lane + 1] ## DOWN
            if(laneTwo.vehicleList[vehicle.currentPos] == None):
                return 'DOWN'        
        return 'N/A'

    def forwardGap(self, lane, pos):
        gap = 0
        for i in range((pos + 1), len(lane.vehicleList)): ## 
            vehicle = lane.vehicleList[i]
            if(vehicle == None):
                gap+=1
            else:
                return gap
        return gap
        
    def backwardGap(self, lane, pos):
        gap = 0
        for i in range((pos - 1), 0, -1): ## 
            vehicle = lane.vehicleList[i]
            if(vehicle == None):
                gap += 1
            else:
                return gap
        return gap
