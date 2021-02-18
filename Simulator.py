from Vehicle import Vehicle
from Lane import Lane
import sched, time
import random

lane = Lane(6,5)
v = [1,2,3,4,5,6]

def createVehicle():
    if(lane.vehicleList[0] == None):
        vehicle = Vehicle(0,0, 'V'+str(v.pop()))
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

s = sched.scheduler(time.time, time.sleep)
def startSimulation(sc):
    if(lane.occupiedCells < lane.vehicleQuantity):
        createVehicle() # Crea un nuevo vehiculo
    #########################################################################
    lane.updateLane()
    printLand()
    s.enter(5, 1, startSimulation, (sc,))

s.enter(1, 1, startSimulation, (s,))
s.run()






