import pygame
import time

pygame.init()
screen=pygame.display.set_mode((600,600))

r=pygame.image.load('rocket.png')
s=pygame.image.load('space.png')
g=pygame.image.load('g_over.jpg')

playing=True

x=300
y=300

while playing:
    screen.blit(s,(0,0))
    screen.blit(r,(x,y))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT and x>0:
                x=x-8
            if event.key==pygame.K_RIGHT and x<600:
                x=x+8
            if event.key==pygame.K_UP and y>0:
                y=y-8
    y=y+2        
    time.sleep(0.05)
    if y>600:
        screen.blit(g,(0,0))

    pygame.display.update()

