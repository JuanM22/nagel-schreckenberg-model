import random

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
        for vehicle in list(filter(None, lane.vehicleList)):
            if(not(vehicle.checked)):
                vehicle.singleLaneUpdatePosition(lane.checkGap(vehicle),lane.maxSpeed)
                lane.vehicleList[vehicle.currentPos] = None
                if(vehicle.newPos < len(lane.vehicleList)):
                    lane.vehicleList[vehicle.newPos] = vehicle
                    vehicle.currentPos = vehicle.newPos
                    vehicle.checked = True
                else:
                    lane.occupiedCells -=1
                    vehicle.kill()
        lane.restartVehicleValues()

    def multiLaneUpdate(self):
        for lane in self.lanes:
            for vehicle in list(filter(None, lane.vehicleList)):
                if(not(vehicle.checked)):
                    ############ Data for second rule ###########
                    movement = self.validateSideMovement(vehicle) ## MOVE UP OR DOWN ##
                    gaps = []
                    if(movement == 'UP'):
                        gaps = [self.backwardGap(lane, vehicle.currentPos), self.forwardGap(self.lanes[vehicle.lane - 1], vehicle.currentPos)]
                    elif(movement == 'DOWN'):
                        gaps = [self.backwardGap(lane, vehicle.currentPos), self.forwardGap(self.lanes[vehicle.lane + 1], vehicle.currentPos)]
                    #####################################################################
                    currentLane = vehicle.lane ## Carril actual ###
                    gap = lane.checkGap(vehicle)
                    vehicle.multiLaneUpdatePosition(gap, gaps,lane.maxSpeed, movement)
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
                            vehicle.kill()
            lane.restartVehicleValues()

    def _changeLanesVehicle(self, vehicle):
        vehicle.kill()
        lane = self.lanes[vehicle.lane]
        vehicle.currentPos = vehicle.newPos ## Actualiza la posicion al nuevo carril ##
        lane.vehicleList[vehicle.currentPos] = vehicle
        lane.add(vehicle)
        lane.occupiedCells += 1

    def validateSideMovement(self, vehicle):
        moveUp = (vehicle.lane - 1) >= 0
        moveDown = (vehicle.lane + 1) < len(self.lanes)
        #######################################################
        moves = []
        if(moveUp):
            laneOne = self.lanes[vehicle.lane - 1] ## UP
            if(laneOne.vehicleList[vehicle.currentPos] == None):
                moves.append('UP')
        if(moveDown):
            laneTwo = self.lanes[vehicle.lane + 1] ## DOWN
            if(laneTwo.vehicleList[vehicle.currentPos] == None):
                moves.append('DOWN')
        if(len(moves) == 2):
            return moves[random.randint(0,1)]
        elif(len(moves) == 1): 
            return moves[0]
        else:
            return 'N/A'

    def forwardGap(self, lane, pos):
        gap = 0
        if(pos > 0):
            for i in range((pos + 1), len(lane.vehicleList)):
                vehicle = lane.vehicleList[i]
                if(vehicle == None):
                    gap += 1
                else:
                    return gap  
        return gap
        
    def backwardGap(self, lane, pos):
        gap = 0
        if(pos > 0):
            for i in range((pos - 1), 0, -1): ## 
                vehicle = lane.vehicleList[i]
                if(vehicle == None):
                    gap += 1
                else:
                    return gap
        return gap