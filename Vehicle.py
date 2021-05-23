import random, pygame, ModelData as data

class Vehicle(pygame.sprite.Sprite):

    def __init__(self,initSpeed, initPosition, image, xPos, yPos, lane):
        pygame.sprite.Sprite.__init__(self)
        self.speed = initSpeed
        self.currentPos = initPosition
        self.newPos = 0
        self.checked = False
        self.image = image
        self.xPos = xPos
        self.yPos = yPos
        self.rect = image.get_rect()
        self.rect.x = xPos
        self.rect.y = yPos
        self.animation = True
        self.lane = lane
        self.move = 'X'

    def singleLaneUpdatePosition(self,gap):
        self.animation = True
        self.move = 'X'
        self._ruleOne()
        self.__singleLaneRuleTwo(gap)
        self._ruleThree()
        self._ruleFour()

    def multiLaneUpdatePosition(self, gap, gaps, movement):
        self.animation = True
        self.checked = True
        self._ruleOne()
        self._multiLaneRuleTwo(gap, gaps, movement)
        self._ruleThree()
        self._ruleFour()

    def _ruleOne(self):
        self.speed = min(self.speed + 1, data.maxSpeed)
    
    def __singleLaneRuleTwo(self, gap):
        self.speed = min(self.speed, gap)

    def _multiLaneRuleTwo(self, gap, gaps, movement):
        self.move = 'X'
        if(self.speed >= gap and movement != 'N/A' and (self.currentPos + self.speed) < 27):
            if(gaps[0] == data.maxSpeed and gaps[1] == self.speed):
                currentLane = self.lane
                self.changeLane(movement)
                if(currentLane == self.lane):
                    self.__singleLaneRuleTwo()
            else:
                self.__singleLaneRuleTwo(gap)
        else:
            self.__singleLaneRuleTwo(gap)

    def _ruleThree(self):
        if(self.speed > 0 and random.random() <= data.breakProbability):
            self.speed -= 1
    
    def _ruleFour(self):
        self.newPos = self.currentPos + self.speed
        if((self.newPos < 28) and (self.currentPos != self.newPos)):
            self.xPos += (43 * self.speed)

    def changeLane(self, movement):
        if(movement == 'UP'):
            if(random.random() <= data.laneChangeProbability):
                self.lane -= 1
                self.yPos -= 40
                self.move = 'Y-'
        elif(movement == 'DOWN'):
            if(random.random() <= data.laneChangeProbability):
                self.lane +=1
                self.yPos += 40
                self.move = 'Y+'

    def update(self):
        if(self.move == 'X'):
            if(self.rect.x < self.xPos):
                self.rect.x += 1
            else:
                self.animation = False
                self.move = ''
        elif(self.move == 'Y+'):
            if(self.rect.y < self.yPos):
                self.rect.y += 1
            else:
                self.animation = (self.rect.x < self.xPos)
                self.move = '' if(not(self.animation)) else 'X'
        elif(self.move == 'Y-'):
            if(self.rect.y > self.yPos):
                self.rect.y -= 1
            else:
                self.animation = (self.rect.x < self.xPos)
                self.move = '' if(not(self.animation)) else 'X'