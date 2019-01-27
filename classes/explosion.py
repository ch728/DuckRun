# -*- coding: utf-8 -*-
import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center,exp_pics):
        pygame.sprite.Sprite.__init__(self)
        self.exp_pics=exp_pics
        self.image = pygame.image.load(exp_pics[0])
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.image=pygame.transform.scale(self.image,(int(self.rect[2]*0.75),int(self.rect[3]*0.75)))
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 40

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.exp_pics):
                self.kill()
            else:
                center = self.rect.center
                self.image = pygame.image.load(self.exp_pics[self.frame])
                self.rect = self.image.get_rect()
                self.rect.center = center
                self.image=pygame.transform.scale(self.image,(int(self.rect[2]*0.75),int(self.rect[3]*0.75)))

