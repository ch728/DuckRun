import pygame

class Duck(pygame.sprite.Sprite):

    def __init__(self,img,coord):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(img)
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=coord
        self.image=pygame.transform.scale(self.image,(int(self.rect[2]*0.8),int(self.rect[3]*0.8)))
        self.health=3
        self.speed=5
    def update(self,direction,super_stat):
        self.super=super_stat
        self.rect.top+= direction*(self.speed+(super_stat*self.speed))
    def get_health(self):
        return self.health
    def update_health(self,damage):
        self.health += damage
    
        

