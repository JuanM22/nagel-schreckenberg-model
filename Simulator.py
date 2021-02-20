from Vehicle import Vehicle
from Lane import Lane
import sched, time
import random

lane = Lane(6,2)
v = [1,2,3,4,5,6]
brakeProbability = 0.3

v1 = Vehicle(2,0,'V1', brakeProbability)
v2 = Vehicle(1,2,'V2', brakeProbability)
v3 = Vehicle(1,5,'V3', brakeProbability)
v4 = Vehicle(0,6,'V4', brakeProbability)

lane.vehicleList[0] = v1
lane.vehicleList[2] = v2
lane.vehicleList[5] = v3
lane.vehicleList[6] = v4


def createVehicle():
    if(lane.vehicleList[0] == None):
        vehicle = Vehicle(0,0, 'V'+str(v.pop()), brakeProbability)
        lane.addVehicleToLane(vehicle)
        lane.occupiedCells +=1
    
def printLand():
    data = ''
    for vehicle in lane.vehicleList:
        if(vehicle!=None):
            data += str(vehicle.name)+' '
        else:
            data += '0 '
    print(data, end='\r')

printLand()

# s = sched.scheduler(time.time, time.sleep)
# def startSimulation(sc):
#     if(lane.occupiedCells < lane.vehicleQuantity):
#         createVehicle() # Crea un nuevo vehiculo
#     lane.updateLane()
#     printLand()
#     s.enter(5, 1, startSimulation, (sc,))

# s.enter(1, 1, startSimulation, (s,))
# s.run()

s = sched.scheduler(time.time, time.sleep)
def startSimulation(sc):
    # if(lane.occupiedCells < lane.vehicleQuantity):
    #     createVehicle() # Crea un nuevo vehiculo
    lane.updateLane()
    printLand()
    s.enter(2, 1, startSimulation, (sc,))

s.enter(5, 1, startSimulation, (s,))
s.run()





