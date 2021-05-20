from Lane import Lane

strChangeProbability = '20'
strBreakProbability = '0'

laneChangeProbability = 0
breakProbability = 0
laneQuantity = 1
vehicleQuantity = 28
maxSpeed = 5
mode = ''
hideLaneSelector = True
selectedButton = None

laneNames = []

def chargeLaneNames():
    for i in range(laneQuantity): laneNames.append('L'+str(i))
    return laneNames

def createLanes(road):
    laneNames = chargeLaneNames()
    for i in range(0, laneQuantity):
        lane = Lane(28, 5, laneNames[i])
        road.lanes.append(lane)