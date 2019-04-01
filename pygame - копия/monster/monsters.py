import pygame
from pygame.locals import *
import pyganim
import os

pygame.init()

x = 50
y = 430
monster_width = 60
monster_height = 71
speed = 2
monster_health = 100

display.set_mode()

walkmRight = [pygame.image.load('monster/animation/Walkright1.png'), pygame.image.load('monster/animation/Walkright2.png'), pygame.image.load('monster/animation/Walkright3.png'), pygame.image.load('monster/animation/Walkright4.png'), pygame.image.load('monster/animation/Walkright5.png'), pygame.image.load('monster/animation/Walkright6.png')]

walkmLeft = [pygame.image.load('monster/animation/Walkleft1.png'), pygame.image.load('monster/animation/Walkleft2.png'), pygame.image.load('monster/animation/Walkleft3.png'), pygame.image.load('monster/animation/Walkleft4.png'), pygame.image.load('monster/animation/Walkleft5.png'), pygame.image.load('monster/animation/Walkleft6.png')]

hurtRight = [pygame.image.load('monster/animation/Hurtright1.png'), pygame.image.load('monster/animation/Hurtright2.png'), pygame.image.load('monster/animation/Hurtright3.png'), pygame.image.load('monster/animation/Hurtright4.png'), pygame.image.load('monster/animation/Hurtright5.png')]

hurtLeft = [pygame.image.load('monster/animation/Hurtleft1.png'), pygame.image.load('monster/animation/Hurtleft2.png'), pygame.image.load('monster/animation/Hurtleft3.png'), pygame.image.load('monster/animation/Hurtleft4.png'), pygame.image.load('monster/animation/Hurtleft5.png')]

deadRight = [pygame.image.load('monster/animation/Deadright1.png'), pygame.image.load('monster/animation/Deadright2.png'), pygame.image.load('monster/animation/Deadright3.png'), pygame.image.load('monster/animation/Deadright4.png'), pygame.image.load('monster/animation/Deadright5.png'), pygame.image.load('monster/animation/Deadright6.png'), pygame.image.load('monster/animation/Deadright7.png'), pygame.image.load('monster/animation/Deadright8.png')]

deadLeft = [pygame.image.load('monster/animation/Deadleft1.png'), pygame.image.load('monster/animation/Deadleft2.png'), pygame.image.load('monster/animation/Deadleft3.png'), pygame.image.load('monster/animation/Deadleft4.png'), pygame.image.load('monster/animation/Deadleft5.png'), pygame.image.load('monster/animation/Deadleft6.png'), pygame.image.load('monster/animation/Deadleft7.png'), pygame.image.load('monster/animation/Deadleft8.png')]

attackRight = [pygame.image.load('monster/animation/Attackright1.png'), pygame.image.load('monster/animation/Attackright1.png'), pygame.image.load('monster/animation/Attackright3.png'), pygame.image.load('monster/animation/Attackright4.png'), pygame.image.load('monster/animation/Attackright5.png'), pygame.image.load('monster/animation/Attackright6.png')]

attackLeft = [pygame.image.load('monster/animation/Attackleft1.png'), pygame.image.load('monster/animation/Attackleft2.png'), pygame.image.load('monster/animation/Attackleft3.png'), pygame.image.load('monster/animation/Attackleft4.png'), pygame.image.load('monster/animation/Attackleft5.png'), pygame.image.load('monster/animation/Attackleft6.png')]


#class Monster(sprite.Sprite):

class Monster():
    def __init__(self, x, y, left, right, maxLengthLeft, maxLengthRight, monster_health):
        sprite.Sprite.__init__(self)
        self.image = Surface((monster_width, monster_height))
        self.rect = Rect(x, y, monster_width)
        self.startX = x # начальные координаты
        self.startY = y
        self.maxLengthLeft = maxLengthLeft # максимальное расстояние, которое может пройти в одну сторону, лево.
        self.maxLengthRight= maxLengthUp # максимальное расстояние, которое может пройти в одну сторону, право.
        self.monster_health = monster_health
        self.xvel = left # cкорость передвижения по горизонтали, 0 - стоит на месте
        self.yvel = right # скорость движения право, 0 - не двигается

        self.rect.y += self.yvel
        self.rect.x += self.xvel

        self.collide(platforms)

        if (abs(self.startX - self.rect.x) > self.maxLengthLeft):
            self.xvel =-self.xvel  # если прошли максимальное растояние, то идеи в обратную сторону

    def collide(self, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p) and self != p: # если с чем-то или кем-то столкнулись
               self.xvel = - self.xvel # то поворачиваем в обратную сторону
               self.yvel = - self.yvel

def drawWindow():
    global animCount

#Програвання спрайтів
    if animCount + 1 >= 30:
        animCount = 0

    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1

    if left:
        win.blit(hurtLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        win.blit(hurtRight[animCount // 5], (x, y))
        animCount += 1

    if left:
        win.blit(deadLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        win.blit(deadRight[animCount // 5], (x, y))
        animCount += 1

    if left:
        win.blit(attackLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        win.blit(attackRight[animCount // 5], (x, y))
        animCount += 1

    pygame.display.update()
