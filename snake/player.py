import pygame
class Player:
    x = []
    y = []
    WHITE = [255, 255, 255]
    step = 25
    length = 3
    direction = 0
    score = 0
    updateCountMax = 2
    updateCount = 0
    #block variable stops the snake from colliding itself if opposite direction event occurs it basically blocks the direction
    block = 1


    def __init__(self, length):
        self.x = []
        self.y = []
        self.block = 1
        self.direction = 0
        self.step = 25
        self.length = length
        for i in range(0,2000):
            self.x.append(-50)
            self.y.append(-50)
            #print(self.x)
        # initial positions, no collision.
        self.x[0] = 75
        self.y[0] = 75

    def update(self):
        self.updateCount = self.updateCount+1
        if self.updateCount > self.updateCountMax:
            #update previous position
            for i in range(self.length-1, 0, -1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]

            if  self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if  self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if  self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if  self.direction == 3:
                self.y[0] = self.y[0] + self.step
            self.updateCount = 0

    #movement methods
    def moveRight(self):
        if self.block != 0:
            self.direction = 0
            self.block = 1
        return
    def moveLeft(self):
        if self.block != 1:
            self.direction = 1
            self.block = 0
        return
    def moveUp(self):
        if self.block != 2:
            self.direction = 2
            self.block = 3
        return
    def moveDown(self):
        if self.block != 3:
            self.direction = 3
            self.block = 2
        return

    def draw(self, surface, snakehead, snakebody):
        surface.blit(snakehead,(self.x[0], self.y[0]))
        for i in range(1, self.length):
            surface.blit(snakebody,(self.x[i], self.y[i]))

    
    