import pygame
class Game:
    BLACK = [0, 0, 0]
    BLUE = [0,0,255]
    def isCollision(self, x1, y1, x2, y2, bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False
    
    def boundaryCollision(self, x1, y1, x2, y2, bsize):
        if x2<=0 or x2+x1>=800 :
            if y1+y2>=y2 :
                return True
        if y2>=575 or y2<=y1:
            return True
        return False
    
    def drawScore(self, surf, text, size, x, y):
        #print(text)
        #font_name = pygame.font.match_font('arial')
        #rect = pygame.Rect(200, 200, 350, 350)
        #pygame.draw.rect(surf, (255, 255, 255), rect)
        font = pygame.font.SysFont('Comic Sans MS', size)
        text_surface = font.render(text, True, self.BLUE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)
    
    def gameOver(self, surf, player):
        gameover_image = pygame.image.load('gameover.png').convert()
        image = pygame.transform.scale(gameover_image, (500,500))
        #drawing the apple image
        surf.fill([255,255,255])
        surf.blit(image, (150,50))
        self.drawScore(surf,  str('your Score is : ')+str(player.score),  30, 50, 10)
        pygame.display.flip()