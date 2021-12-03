import pygame
import sys

pygame.init()

#open a window, set size
width = 300
height = 300
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

def main():
    while (True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
        #game logic goes here
        '''
        
        
        
        '''

        #set background color
        surface.fill(BKGR_RED)


        pygame.display.update()
main()