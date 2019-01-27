import pygame

class Rock(pygame.sprite.Sprite):

    def __init__(self,img,coord,speed,size):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(img)
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=coord
        self.speed=speed 
        self.image=pygame.transform.scale(self.image,(int(self.rect[2]*size),int(self.rect[3]*size)))
    def update(self,super_stat):
        if self.rect.left <=0:
           self.kill()
        else:
            self.rect.left += (self.speed+(super_stat*self.speed))

