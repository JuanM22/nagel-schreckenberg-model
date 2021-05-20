import pygame

class LaneSprite(pygame.sprite.Sprite):
    
    def __init__(self, image, xPos, yPos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = xPos
        self.rect.y = yPos