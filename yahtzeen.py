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
GREEN =    (27, 105, 3)
BLUE =     (0, 0, 255)
BKGR_RED = (148, 10, 10)
WHITE =    (255, 255, 255)
BLACK =    (0, 0, 0)
PURPLE =   (96, 20, 226)
BROWN =    (119, 77, 43)

#temp positions of six dice (to be used for upper section)
LEFT = pygame.Rect((width/10)+50, height/2.25, 120, 120)
LESS_LEFT = pygame.Rect((width/10)+150, height/2.25, 120, 120)
LESSER_LEFT = pygame.Rect((width/10)+250, height/2.25, 120, 120)
EVEN_LESS_LEFT = pygame.Rect((width/10)+350, height/2.25, 120, 120)
LEFFFFFFFT = pygame.Rect((width/10)+450, height/2.25, 120, 120)
MOST_LEFT = pygame.Rect((width/10)+550, height/2.25, 120, 120)

TOP_LEFT = pygame.Rect(30, 120, 120, 120)
TOP_LESS_LEFT = pygame.Rect(120, 120, 120, 120)
TOP_LESSER_LEFT = pygame.Rect(210, 120, 120, 120)
TOP_EVEN_LESS_LEFT = pygame.Rect(300, 120, 120, 120)
TOP_LEFFFFFFFT = pygame.Rect(390, 120, 120, 120)

def displayPicture(picture,location,scale):
    image = pygame.image.load(picture).convert_alpha()
    image = pygame.transform.rotozoom(image, 0, scale)
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

        pygame.draw.line(surface, BLACK, (0, 700/3),(width, 700/3),2) #top third
        pygame.draw.line(surface, BLACK, (0, 2*(700/3)),(width, 2*(700/3)),2) #bottom third
        pygame.draw.line(surface, BLACK, (500,0), (500, 700/3),  2) #top third vertical line
        pygame.draw.line(surface, BLACK, (500, 58), (width, 58), 2) #top logo/scoring line
        pygame.draw.line(surface, BLACK, (500, 116), (width, 116), 2) #second scoring line
        pygame.draw.line(surface, BLACK, (500, 174), (width, 174), 2) #third scoring line

        #draw player indicator box
        pygame.draw.line(surface, BLACK, (300,0), (300, 75), 2)
        pygame.draw.line(surface, BLACK, (0, 75), (300, 75), 2)

        #miscellaneous UI elements
        pygame.draw.line(surface, BLACK, (820, 0), (820, 58), 2) #vertical menu line
        pygame.draw.line(surface, BLACK, (840, 20), (880, 20), 4) #menu line one
        pygame.draw.line(surface, BLACK, (840, 30), (880, 30), 4) #menu line two
        pygame.draw.line(surface, BLACK, (840, 40), (880, 40), 4) #menu line three
        pygame.draw.rect(surface, GREEN, pygame.Rect(310, 10, 182, 60), 0, 3) #rect is at (310, 10), width 182, height 60px

        #display dice for current roll, need to be 80 pixels each with 10 px between each
        displayPicture("ace.png", TOP_LEFT, 0.076555)
        displayPicture("two.png", TOP_LESS_LEFT, 0.076555)
        displayPicture("three.png", TOP_LESSER_LEFT, 0.076555)
        displayPicture("four.png", TOP_EVEN_LESS_LEFT, 0.076555)
        displayPicture("five.png", TOP_LEFFFFFFFT, 0.076555)

        #display middle dice
        displayPicture("ace.png", LEFT, 0.087081)
        displayPicture("two.png", LESS_LEFT, 0.087081)
        displayPicture("three.png", LESSER_LEFT, 0.087081)
        displayPicture("four.png", EVEN_LESS_LEFT, 0.087081)
        displayPicture("five.png", LEFFFFFFFT, 0.087081)
        displayPicture("six.png", MOST_LEFT, 0.087081)

        pygame.display.update()
main()