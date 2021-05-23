import pygame
import ModelData as data
from LaneSprite import LaneSprite

carImages = ['./resources/car1.png', './resources/car2.png', './resources/car3.png', 
             './resources/car4.png', './resources/car5.png', './resources/car6.png',
             './resources/car7.png', './resources/car8.png', './resources/car9.png']
images = []

### SCREEN ###
backgroundImg = backgroundImg = pygame.image.load('./resources/nagelBackground.jpg')
#############################################################################

### LANES ###
laneSprites = pygame.sprite.Group()
laneBackGround = pygame.image.load('./resources/nagelModelLane.png')

def createLaneSprites(height):
    laneSprites.empty()
    laneSprites.update()
    ######################################################################
    laneXPos = 70
    laneYPos = (height * 30)/100
    for _ in range(0, data.laneQuantity):
        laneSprite = LaneSprite(laneBackGround, laneXPos, laneYPos)
        laneYPos += 40
        laneSprites.add(laneSprite)
#############################################################################

### VEHICLES ###
def chargeCarImages():
    for i in range(0, len(carImages)):
        car = pygame.image.load(carImages[i]).convert_alpha()
        car = pygame.transform.scale(car, (38, 28))
        images.append(car)