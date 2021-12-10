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

#temp positions of six dice (to be used for upper section)
LEFT = pygame.Rect((width/10), height/2.15, 120, 120)
LESS_LEFT = pygame.Rect((width/10)+125, height/2.15, 120, 120)
LESSER_LEFT = pygame.Rect((width/10)+250, height/2.15, 120, 120)
EVEN_LESS_LEFT = pygame.Rect((width/10)+375, height/2.15, 120, 120)
LEFFFFFFFT = pygame.Rect((width/10)+500, height/2.15, 120, 120)
MOST_LEFT = pygame.Rect((width/10)+625, height/2.15, 120, 120)
#positions of current roll
TOP_LEFT = pygame.Rect(30, 120, 120, 120)
TOP_LESS_LEFT = pygame.Rect(120, 120, 120, 120)
TOP_LESSER_LEFT = pygame.Rect(210, 120, 120, 120)
TOP_EVEN_LESS_LEFT = pygame.Rect(300, 120, 120, 120)
TOP_LEFFFFFFFT = pygame.Rect(390, 120, 120, 120)

def displayPicture(picture,location,scale):
    image = pygame.image.load(picture).convert_alpha()
    image = pygame.transform.rotozoom(image, 0, scale)
    surface.blit(image, location)

def displayMessage(words, font,fontSize, x, y, color, isUnderlined):
    font = pygame.font.Font(font, fontSize)
    if(isUnderlined):
        font.underline = True
    text = font.render(words, True, color)
    textBounds = text.get_rect()
    textBounds.center = (x, y)
    surface.blit(text, textBounds)

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
        pygame.draw.line(surface, BLACK, (0, 525), (width, 525), 2) #lower section score split line
        pygame.draw.line(surface, BLACK, (width/7, 525), (width/7, height), 2) #first lower score section
        pygame.draw.line(surface, BLACK, ((2*width)/7, 525), ((2*width)/7, height), 2) #second lower score section
        pygame.draw.line(surface, BLACK, ((3*width)/7, 525), ((3*width)/7, height), 2) #third lower score section
        pygame.draw.line(surface, BLACK, ((4*width)/7, 525), ((4*width)/7, height), 2) #fourth lower score section
        pygame.draw.line(surface, BLACK, ((5*width)/7, 525), ((5*width)/7, height), 2) #fifth lower score section
        pygame.draw.line(surface, BLACK, ((6*width)/7, 525), ((6*width)/7, height), 2) #sixth lower score section
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

        #logo text
        displayMessage("YahtzeeN!", "Smooch-Regular.ttf", 72, 700, 30, WHITE, False)
        #display upper section labels
        displayMessage("Aces", "Smooch-Regular.ttf", 48, (width/10)+50, height/2.28, WHITE, False)
        displayMessage("Twos", "Smooch-Regular.ttf", 48, (width/10)+175, height/2.28, WHITE, False)
        displayMessage("Threes", "Smooch-Regular.ttf", 48, (width/10)+300, height/2.28, WHITE, False)
        displayMessage("Fours", "Smooch-Regular.ttf", 48, (width/10)+425, height/2.28, WHITE, False)
        displayMessage("Fives", "Smooch-Regular.ttf", 48, (width/10)+550, height/2.28, WHITE, False)
        displayMessage("Sixes", "Smooch-Regular.ttf", 48, (width/10)+675, height/2.28, WHITE, False)
        #display player/role state label
        displayMessage("Player X: Roll x of 3", "Raleway-Light.ttf", 32, 150, 40, WHITE, False)
        #display "roll now!" button text
        displayMessage("Roll Now!", "Raleway-SemiBold.ttf", 34, 402, 40, BLACK, True)
        #display "upper section" and "lower section" titles
        displayMessage("Upper Section", "Raleway-Light.ttf", 40, width/2, height/2.7, WHITE, True)
        displayMessage("Lower Section", "Raleway-Light.ttf", 40, width/2, 2.12*(700/3), WHITE, True)
        #display "upper section score" and "lower section score"
        displayMessage("Upper Section Score: XX", "Raleway-SemiBold.ttf", 34, 700, 85, WHITE, False)
        displayMessage("Lower Section Score: XX", "Raleway-SemiBold.ttf", 34, 700, 143, WHITE, False)
        displayMessage("Total Score: XX", "Raleway-SemiBold.ttf", 34, 627, 201, WHITE, False)
        #display each lower section category name
        displayMessage("3 of a Kind", "Smooch-Regular.ttf", 27, width/14, 542, WHITE, False)
        displayMessage("4 of a Kind", "Smooch-Regular.ttf", 27, (3*width)/14, 542, WHITE, False)
        displayMessage("Full House", "Smooch-Regular.ttf", 27, (5*width)/14, 542, WHITE, False)
        displayMessage("Sm. Straight", "Smooch-Regular.ttf", 27, (7*width)/14, 542, WHITE, False)
        displayMessage("Lg. Straight", "Smooch-Regular.ttf", 27, (9*width)/14, 542, WHITE, False)
        displayMessage("Yahtzee!", "Smooch-Regular.ttf", 27, (11*width)/14, 542, WHITE, False)
        displayMessage("Chance", "Smooch-Regular.ttf", 27, (13*width)/14, 542, WHITE, False)

        ###NOTE You will need to add a space if the score is a single digit instead of two digits###

        #display upper section scores
        displayMessage("NaN", "Raleway-Light.ttf", 30, (width/10)+45, height/1.6, WHITE, False)
        displayMessage("NaN", "Raleway-Light.ttf", 30, (width/10)+170, height/1.6, WHITE, False)
        displayMessage("NaN", "Raleway-Light.ttf", 30, (width/10)+295, height/1.6, WHITE, False)
        displayMessage("NaN", "Raleway-Light.ttf", 30, (width/10)+420, height/1.6, WHITE, False)
        displayMessage("NaN", "Raleway-Light.ttf", 30, (width/10)+545, height/1.6, WHITE, False)
        displayMessage("NaN", "Raleway-Light.ttf", 30, (width/10)+670, height/1.6, WHITE, False)
        #display lower section scores
        displayMessage("NaN", "Raleway-Light.ttf", 30, (2*width)/28, 580, WHITE, False)
        displayMessage("NaN", "Raleway-Light.ttf", 30, (6*width)/28, 580, WHITE, False)
        displayMessage("NaN", "Raleway-Light.ttf", 30, (10*width)/28, 580, WHITE, False)
        displayMessage("NaN", "Raleway-Light.ttf", 30, (14*width)/28, 580, WHITE, False)
        displayMessage("NaN", "Raleway-Light.ttf", 30, (18*width)/28, 580, WHITE, False)
        displayMessage("NaN", "Raleway-Light.ttf", 30, (22*width)/28, 580, WHITE, False)
        displayMessage("NaN", "Raleway-Light.ttf", 30, (26*width)/28, 580, WHITE, False)
        pygame.display.update()

main()