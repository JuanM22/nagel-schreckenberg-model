import random, pygame

class Vehicle:

    def __init__(self,initSpeed, initPosition, brakeProbability, image, xPos, yPos, namePos):
        self.speed = initSpeed
        self.currentPos = initPosition
        self.newPos = 0
        self.checked = False
        self.brakeProbability = brakeProbability
        self.image = image
        self.xPos = xPos
        self.yPos = yPos
        self.namePos = namePos

    def updatePosition(self,gap, maxSpeed):
        self._ruleOne(maxSpeed)
        self._ruleTwo(gap)
        self._ruleThree()
        self._ruleFour()

    def _ruleOne(self, maxSpeed):
        self.speed = min(self.speed + 1, maxSpeed)
    
    def _ruleTwo(self, gap):
        self.speed = min(self.speed, gap)
    
    def _ruleThree(self):
        if(self.speed > 0 and random.random() <= self.brakeProbability):
            self.speed -= 1
    
    def _ruleFour(self):
        self.newPos = self.currentPos
        self.newPos += self.speed
        if(self.newPos < 23):
            self.xPos = 55 * (self.newPos + 1)
