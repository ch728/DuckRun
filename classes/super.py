import pygame
from itertools import cycle

class Super(pygame.sprite.Sprite):
    
    def __init__(self,center,images):
        pygame.sprite.Sprite.__init__(self)
        self.frame_rate=20
        self.duration=15*1000
        self.images=cycle(images)
        self.image=pygame.image.load(next(self.images))
        self.rect=self.image.get_rect()
        self.rect.center=center 
        self.start_time=pygame.time.get_ticks()
        self.last_update=pygame.time.get_ticks()
        
    def update(self,move):
        now=pygame.time.get_ticks()
        self.rect.center=(self.rect.center[0],self.rect.center[1]+move)
            
        if now-self.start_time> self.duration:
            self.kill()

        elif now-self.last_update > self.frame_rate:
            self.last_update=now
            center = self.rect.center
            self.image =pygame.image.load(next(self.images))
            self.rect = self.image.get_rect()
            self.rect.center = center
           
