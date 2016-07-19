#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame as pg
from pygame.locals import *

pg.init()                           # init pygame
w = 320                             # width
h = 240                             # height
size=(w,h)                          # size
screen = pg.display.set_mode(size)  # init screen  
FPS = 18                            # frames per second setting
framerate = pg.time.Clock()
pg.display.set_caption('STAR WARS CAPTION FX')

# filename_processed_pattern = "frame_%0#5d.pbm"
# processed_frames_folder = "./frames/"  

filename_processed_pattern = "frame_%0#5d.processed.ppm"
processed_frames_folder = "./processed-frames/"  

filename_frame = ""
repeat = True
while repeat: # iterate
    for frame_count in range(0, 560):
        filename_frame = filename_processed_pattern % frame_count
 
        img=pg.image.load(processed_frames_folder + filename_frame)
        screen.blit(img, (0,0)) # put image 
        pg.display.update()
        pg.display.flip() 
        framerate.tick(FPS)

        for event in pg.event.get():
            if event.type == QUIT:
                repeat = False

        if not repeat:
            break

pg.quit()    
print "done!"
