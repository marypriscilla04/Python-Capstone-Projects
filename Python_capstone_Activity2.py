# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pygame

pygame.init()

screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Bouncing Ball")

x=200
y=30
ballVelocity = 1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    pygame.time.delay(3)
    y = y + ballVelocity
    
    if y >= 370:
        ballVelocity = -1
        
    if y <= 30:
        ballVelocity = +1
         
    screen.fill("black")
    """ square = pygame.Rect(x,y,60,60) """
    pygame.draw.circle(screen,"green",(x,y),20)
    pygame.display.update()
    