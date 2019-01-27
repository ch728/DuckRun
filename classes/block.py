import pygame

class Block(pygame.sprite.Sprite):
 
    def __init__(self,img,coord):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(img)
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=coord
    def update(self,x,y):
        self.rect.left+=x
        self.rect.top+=y
    def get_pos(self):
        return (self.rect)

    
    