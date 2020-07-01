#importing required Libraries
import pygame as pg
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

#game display
pg.init()
fps=30 #frames per second
clock=pg.time.Clock()

screen=pg.display.set_mode((width,height+100),0,32)
#height+100 is to provide extra 100pc space to display game status

#name tag
pg.display.set_caption("Tic Tac Toe")

#load images
init_window=pg.image.load("images/cover_img.jpg")
x_img=pg.image.load("images/x_img.jpg")
o_img=pg.image.load("images/o_img.png")

#resizing images to required width and height
init_window=pg.transform.scale(init_window,(width,height+100))
x_img=pg.transform.scale(x_img,(80,80))
y_img=pg.transform.scale(o_img,(80,80))

def game_init_window():
    screen.blit(init_window,(0,0))
    pg.display.update()
    time.sleep(3)
    screen.fill(white)

    #drawing 2 vertical lines that splits the canvas in three equal halves
    pg.draw.line(screen,line_color,(width/3,0),(width/3,height),7)
    pg.draw.line(screen,line_color,(width/3*2,0),(width/3*2,height),7)

    #drawing 2 horizontal lines that splits the canvas in three equal halves
    pg.draw.line(screen,line_color,(0,height/3),(width,height/3),7)
    pg.draw.line(screen,line_color,(0,height/3*2),(width,height/3*2),7)
    draw_status()

def draw_status():

    global drawing
    if win is None:
        msg=XO.upper()+"'s turn"
    else:
        msg=XO.upper()+" Won!"
    if draw:
        msg="Game Draw!"

    font=pg.font.Font(None,30)
    text=font.render(msg,1,white)

    #creating a small block at the bottom of the display
    screen.fill(line_color,(0,500,600,100))
    text_rect=text.get_rect(center=(width/2,550))
    screen.blit(text,text_rect)
    pg.display.update()
