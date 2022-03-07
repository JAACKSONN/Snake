from glob import glob
import random
import math
import tkinter as tk
from tkinter import messagebox
import pygame
 
class cube(object):
    rows = 20
    w = 500
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        pass
 
       
    def move(self, dirnx, dirny):
        pass
 
    def draw(self, surface, eyes=False):
        pass
       
       
 
 
 
class snake(object):

    def __init__(self, color, pos):
        pass
 
    def move(self):
        pass
 
    def reset(self, pos):
 
 
    def addCube(self):
        pass
       
 
    def draw(self, surface):
        pass
 
 
def drawGrid(w, rows, surface):
    pass
       
#this will update the display 
def redrawWindow(surface):
    global rows, width
    surface.fill((0,0,0))
    drawGrid(surface)
    pygame.display.update()
 
 
def randomSnack(rows, item):
    pass
 
 
def message_box(subject, content):
    pass
 
 
def main():
    global width, rows  
    width = 500
    rows = 20 #can make this less so that the snake has less squares to move around in
    win = pygame.display.set_mode(width, width)  
    s = snake((255, 0, 0), (10,10))

    flag = True
    clock = pygame.time.Clock()
    while flag:
        pygame.time.delay(50) #lower this is, the faster its going to be
        clock.tick(10) #makes sure that our game does not run at more than 10 frames per second, our snake can move 10 blocks in 1 second, so we have a delay

        redrawWindow(win)
    pass
 
 
 
main()
');

