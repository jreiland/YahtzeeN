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

#temp positions of six dice (to be used for upper section)
LEFT= pygame.Rect((width/10), height/2, 120, 120)
LESS_LEFT = pygame.Rect((width/10)+75, height/2, 120, 120)
LESSER_LEFT= pygame.Rect((width/10)+150, height/2, 120, 120)
EVEN_LESS_LEFT = pygame.Rect((width/10)+225, height/2, 120, 120)
LEFFFFFFFT= pygame.Rect((width/10)+300, height/2, 120, 120)
MOST_LEFT = pygame.Rect((width/10)+375, height/2, 120, 120)

def displayPicture(picture,location):
    image = pygame.image.load(picture).convert_alpha()
    image = pygame.transform.rotozoom(image, 0, 0.087081)
    surface.blit(image, location)

def main():
    while (True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
        #game logic goes here
        



        #draw UI!
        surface.fill(BKGR_RED)

        pygame.draw.line(surface, BLACK, (0, 200),(width, 200),2) #top third
        pygame.draw.line(surface, BLACK, (0, 550),(width, 550),2) #bottom third
        pygame.draw.line(surface, BLACK, (500,0), (500, 200),  2) #top third vertical line
        displayPicture("six.png", LEFT)
        displayPicture("ace.png", LESS_LEFT)
        displayPicture("two.png", LESSER_LEFT)
        displayPicture("three.png", EVEN_LESS_LEFT)
        displayPicture("four.png", LEFFFFFFFT)
        displayPicture("five.png", MOST_LEFT)

        pygame.display.update()
main()