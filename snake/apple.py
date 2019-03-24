from pygame.locals import *
import pygame
import time
class Apple:
    x=0
    y=0
    step = 25

    def __init__(self, x, y):
        self.x = x * self.step
        self.y = y * self.step
    
    def draw (self, surface, image):
        #resizing the apple image
        image = pygame.transform.scale(image, (25,25))
        #drawing the apple image
        surface.blit(image, (self.x, self.y))