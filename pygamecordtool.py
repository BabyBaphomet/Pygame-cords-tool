import pygame, random, time, sys
from pygame import mixer
from pygame.locals import *
from random import randrange
pygame.init()
mainClock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)
pygame.display.set_caption('pygame tool')
screenx, screeny = 500, 700
win = pygame.display.set_mode((screenx,screeny), 0, 32)
pygame.mouse.set_visible(False)
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1 , color)
    textrect = font.render(text, 1, color)
    textrect = (x, y)
    surface.blit(textobj, textrect)
click = False
# Loop ------------------------------------------------------- #
while True:


    # Background --------------------------------------------- #
    win.fill((212,98,96))
    mx, my = pygame.mouse.get_pos()
    mouse = pygame.mouse.get_pressed()
    if click == True:
        print(str(mx) + "," + str(my))
        click = False
    #Y IS UP AND DOWN
    #X is left and right
    bszx, bszy = 80,20
    bszx2, bszy2 = 180,30
    b = (244,119,90)
    g = (252,142,102)
    e = (255,168,120)
    # how to draw a rect
      # first we call a rect
                    #now what surface
                             #color  and now cordinates and size

 #   pygame.draw.rect(win, (255, 245, 215), pygame.Rect(16,653, bszx2, bszy2))
    draw_text('X ' + str(mx) + ' Y ' + str(my), font, e, win, 0, 0)
    draw_text("Block Size " + str(bszx)  + " " + str(bszy) , font, g, win, 0, 21)
    draw_text("Screen Size " + str(screenx)  + " " + str(screeny) , font, b, win, 0, 42)



    pygame.draw.rect(win, (255, 245, 215), pygame.Rect(mx, my, bszx, bszy))
    # Buttons ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Update ------------------------------------------------- #
    pygame.display.update()
    mainClock.tick(60)