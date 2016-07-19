#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame as pg
from pygame.locals import *

pg.init()                           # init pygame
w = 320                             # width
h = 240                             # height
size=(w,h)                          # size
screen = pg.display.set_mode(size)  # init screen
pg.display.set_caption('Star Wars TFA')  # caption
filename = "./swtfa.jpg"            # filename
img=pg.image.load(filename)         # image 606x700
x = 0
y = 0
FPS = 10                            # frames per second setting
framerate = pg.time.Clock()
repeat = True
   
while repeat:                       # iterate
    # put image
    screen.blit(img, (0,0), (x, y, 320, 240)) 
    pg.display.flip() 
          
    # scroll down image
    y = y + 1
    if (y + 240 > 800):
      y = 0

    #10fps
    framerate.tick(FPS)

    # capture events
    for event in pg.event.get():
      if event.type == QUIT:
          repeat = False

# exit          
pg.quit()    
print "done!"
