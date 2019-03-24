from pygame.locals import *
import pygame
from player import Player
from apple import Apple
from game import Game
from random import randint
import time
class App:
    windowWidth = 800
    windowHeight = 600
    player = 0
    event = None
    rect = None
    gameOver = False
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._apple_surf = None
        self.player = Player(3)
        self.apple = Apple(5,5)
        self.game = Game()

    def on_init(self):
        print('inside on_init')
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight),  pygame.HWSURFACE)
        pygame.display.set_caption('Snake Game')
        self._running = True
        self.rect = pygame.Rect(25, 47, 750, 600-47-25)
        self._snakebody = pygame.image.load('snakebody.png').convert()
        self._apple_surf = pygame.image.load('apple.png').convert()
    
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
    
    def on_loop(self):
        if not self.gameOver:
            self.player.update()
        #does snake eat apple
        for i in range(0, self.player.length):
            if self.game.isCollision(self.apple.x, self.apple.y, self.player.x[i], self.player.y[i], 20):
                self.player.length = self.player.length + 1
                self.apple.x = randint(2,9) * 25
                self.apple.y = randint(2,9) * 25
                self.player.score = self.player.score + 1
        
        #does snake collide with itself
        for i in range(2, self.player.length):
            self.gameOver = self.game.isCollision(self.player.x[0], self.player.y[0], self.player.x[i], self.player.y[i], 20)
            if self.game.isCollision(self.player.x[0], self.player.y[0], self.player.x[i], self.player.y[i], 20):
                print("You lose! Collision")
                print('YOUR SCORE IS : ', self.player.score)
                return
        
        #does snake collide with boundary
        self.gameOver = self.game.boundaryCollision(self.rect.x, self.rect.y, self.player.x[0], self.player.y[0], 20)
        pass

    def on_render(self):
        #filling color in background
        self._display_surf.fill((255,255,255))
        
        pygame.draw.rect(self._display_surf, (0, 0, 0), self.rect)

        #line dividing score board block and game block
        pygame.draw.line(self._display_surf, (255, 255, 255), (0, 47), (800, 47))

        #checking what side of head should be drawn on the snake
        if self.event[K_RIGHT]:
            if self.player.block != 0:
                self._image_surf = pygame.image.load('snakehead_right.png').convert()

        if self.event[K_LEFT]:
            if self.player.block != 1:
                self._image_surf = pygame.image.load('snakehead_left.png').convert()

        if self.event[K_UP]:
            if self.player.block != 2:
                self._image_surf = pygame.image.load('snakehead_up.png').convert()

        if self.event[K_DOWN]:
            if self.player.block != 3:
                self._image_surf = pygame.image.load('snakehead_down.png').convert()
        
        #draw player(snake)
        self.player.draw(self._display_surf, self._image_surf, self._snakebody)
        #draw apple 
        self.apple.draw(self._display_surf, self._apple_surf)
        #draw score board
        self.game.drawScore(self._display_surf, str('your Score is : ')+str(self.player.score), 30, 50, 10 )
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()
    
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        self._image_surf = pygame.image.load('snakehead_right.png').convert()
        
        while(self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            #self.on_loop()
            self.event = keys
            if keys[K_RIGHT]:
                self.player.moveRight()

            if keys[K_LEFT]:
                self.player.moveLeft()

            if keys[K_UP]:
                self.player.moveUp()
            
            if keys[K_DOWN]:
                self.player.moveDown()

            if keys[K_ESCAPE]:
                self._running = False
            
            #if game is over the screen stops
            if self.gameOver:
                self.game.gameOver(self._display_surf, self.player)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self._image_surf = pygame.image.load('snakehead_right.png').convert()
                            self._display_surf.fill([255,255,255])
                            self.player = Player(3)
                            self.appple = Apple(5,5)
                            self.on_init()
                            self.gameOver = False
                            break

            else:
                self.on_loop()
                self.on_render()
            time.sleep(100.0/1000.0)
            #self.on_event()
        self.on_cleanup()      

if __name__ == '__main__':
    theApp = App()
    theApp.on_execute()