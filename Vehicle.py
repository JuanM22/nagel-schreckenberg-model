import random, pygame

class Vehicle(pygame.sprite.Sprite):

    def __init__(self,initSpeed, initPosition, brakeProbability, image, xPos, yPos, name):
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
        if((self.newPos < 28) and (self.currentPos != self.newPos)):
            self.xPos += (43 * self.speed)

    def update(self):
        if(self.rect.x < self.xPos):
            self.rect.x += 1