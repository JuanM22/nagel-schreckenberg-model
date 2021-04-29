import random, pygame

class Vehicle(pygame.sprite.Sprite):

    def __init__(self,initSpeed, initPosition, brakeProbability, image, xPos, yPos, name, lane):
        pygame.sprite.Sprite.__init__(self)
        self.speed = initSpeed
        self.currentPos = initPosition
        self.newPos = 0
        self.checked = False
        self.brakeProbability = brakeProbability
        self.image = image
        self.xPos = xPos
        self.yPos = yPos
        self.name = name
        self.rect = image.get_rect()
        self.rect.x = xPos
        self.rect.y = yPos
        self.animation = True
        self.lane = lane
        self.move = 'X'

    def singleLaneUpdatePosition(self,gap, maxSpeed):
        self.animation = True
        self.move = 'X'
        self._ruleOne(maxSpeed)
        self._singleLaneRuleTwo(gap)
        self._ruleThree()
        self._ruleFour()

    def multiLaneUpdatePosition(self, gap, gaps, maxSpeed, movement):
        self.animation = True
        self._ruleOne(maxSpeed)
        self._multiLaneRuleTwo(gap, gaps, maxSpeed, movement)
        self._ruleThree()
        self._ruleFour()

    def _ruleOne(self, maxSpeed):
        self.speed = min(self.speed + 1, maxSpeed)
    
    def _singleLaneRuleTwo(self, gap):
        self.speed = min(self.speed, gap)

    def _multiLaneRuleTwo(self, gap, gaps, maxSpeed, movement):
        self.move = 'X'
        if(len(gaps) > 0):
            # if(self.speed >= gap and movement != 'N/A'):
            if(gaps[0] == self.speed and gaps[1] == maxSpeed):
                self.changeLane(movement)
            else:
                self._singleLaneRuleTwo(gap)
        else:
            self._singleLaneRuleTwo(gap)

    def _ruleThree(self):
        if(self.speed > 0 and random.random() <= self.brakeProbability):
            self.speed -= 1
    
    def _ruleFour(self):
        self.newPos = self.currentPos + self.speed
        if((self.newPos < 28) and (self.currentPos != self.newPos)):
            self.xPos += (43 * self.speed)

    def changeLane(self, movement):
        if(movement == 'UP'):
            if(random.random() <= 0.7):
                self.lane -= 1
                self.yPos -= 40
                self.move = 'Y-'
        elif(movement == 'DOWN'):
            if(random.random() <= 0.7):
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
                self.rect.y +=1
            else:
                self.animation = False
                self.move = ''
        elif(self.move == 'Y-'):
            if(self.rect.y > self.yPos):
                self.rect.y -=1
            else:
                self.animation = False
                self.move = ''