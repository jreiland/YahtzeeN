import pygame
import sys

pygame.init()

#open a window, set size
width = 900
height = 700
size = (width, height)
surface = pygame.display.set_mode(size)

#set title bar of window
pygame.display.set_caption("YahtzeeN")

#color constants
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BKGR_RED = (148, 10, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FUN = (231, 78, 111)
PURPLE = (96, 20,226)
YELLOW = (234, 216, 65)
BROWN = (119, 77, 43)
PINK = (248, 179, 197)
#temp to test image
LEFT= pygame.Rect(width/10, height/4, 120, 120)

def displayPicture(picture,location):
    image = pygame.image.load(picture).convert_alpha()
    image = pygame.transform.rotozoom(image, 0, 0.2)
    surface.blit(image, location)

def main():
    while (True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
        #game logic goes here
        



        #set background color
        surface.fill(BKGR_RED)

        displayPicture("ace.png", LEFT)

        pygame.display.update()
main()