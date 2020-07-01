#importing required Libraries
import pygame
import sys
import time
from pygame.locals import *

#declaring global variables

XO='x' #stores  x or o
win=None
draw=None
width=500
height=500
white=(255,255,255)
line_color=(0,0,0) #black

#sets up a 3*3 board on Canvas
board=[[None]*3,[None]*3,[None]*3]
