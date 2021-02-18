class Vehicle:

    def __init__(self,initSpeed, initPosition):
        self.speed = initSpeed
        self.currentPos = initPosition
        self.newPos = 0
        self.checked = False

    def updatePosition(self,gap, maxSpeed):
        self._ruleOne(maxSpeed)
        self._ruleTwo(gap)
        #self._ruleOne(gap,maxSpeed)
        self._ruleFour()

    def _ruleOne(self, maxSpeed):
        self.speed = min(self.speed + 1, maxSpeed)
    
    def _ruleTwo(self, gap):
        self.speed = min(self.speed, gap)
    
    def _ruleThree(self):
        add = 1 + 2
    
    def _ruleFour(self):
        self.newPos += self.speed

