from Lane import Lane

start = False
pause = False
appState = 0

strChangeProbability = '70'
strBreakProbability = '30'
strMaxSpeed = '5'
strLaneQuantity = '1'
strVehicleQuantity = '10'

laneChangeProbability = 0.7
breakProbability = 0.3
laneQuantity = 1
vehicleQuantity = 10
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
        lane = Lane(28, laneNames[i])
        road.lanes.append(lane)