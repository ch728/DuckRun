# -*- coding: utf-8 -*-
import pygame

class Item(pygame.sprite.Sprite):

    def __init__(self,img,coord,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(img)
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=coord
        self.speed=speed
    def update(self,super_stat):
        if self.rect.left <=0:
           self.kill()
        else:
            self.rect.left += (self.speed+(super_stat*self.speed))


