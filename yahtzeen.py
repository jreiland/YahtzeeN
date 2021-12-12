import pygame
import sys
import random

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

#temp positions of six dice (to be used for upper section scoring)
SCORING_ONE = pygame.Rect((width/10), height/2.15, 91, 125)
SCORING_TWO = pygame.Rect((width/10)+125, height/2.15, 91, 125)
SCORING_THREE = pygame.Rect((width/10)+250, height/2.15, 91, 125)
SCORING_FOUR = pygame.Rect((width/10)+375, height/2.15, 91, 125)
SCORING_FIVE = pygame.Rect((width/10)+500, height/2.15, 91, 125)
SCORING_SIX = pygame.Rect((width/10)+625, height/2.15, 91, 125)
#padlock icon positions for current roll section
LOCK_ONE = pygame.Rect(54, 135, 80, 80)
LOCK_TWO = pygame.Rect(144, 135, 80, 80)
LOCK_THREE = pygame.Rect(234, 135, 80, 80)
LOCK_FOUR = pygame.Rect(324, 135, 80, 80)
LOCK_FIVE = pygame.Rect(414, 135, 80, 80)
#positions of current roll
CURR_ONE = pygame.Rect(30, 120, 80, 80)
CURR_TWO = pygame.Rect(120, 120, 80, 80)
CURR_THREE = pygame.Rect(210, 120, 80, 80)
CURR_FOUR = pygame.Rect(300, 120, 80, 80)
CURR_FIVE = pygame.Rect(390, 120, 80, 80)
#roll now rect object
ROLL_NOW = pygame.Rect(310, 10, 182, 60)

#displays the given picture file when given a filename/path, Rect object for location, and scale factor
def displayPicture(picture, location, scale):
    image = pygame.image.load(picture).convert_alpha()
    image = pygame.transform.rotozoom(image, 0, scale)
    surface.blit(image, location)

#displays the given text in the specified font (pass None for default/fallback), size, location, color, and underlined as requested
def displayMessage(words, font, fontSize, x, y, color, isUnderlined):
    font = pygame.font.Font(font, fontSize)
    if(isUnderlined):
        font.underline = True
    text = font.render(words, True, color)
    textBounds = text.get_rect()
    textBounds.center = (x, y)
    surface.blit(text, textBounds)

def main():
    #set initial state variables
    dieOneValue = 0
    dieTwoValue = 0
    dieThreeValue = 0
    dieFourValue = 0
    dieFiveValue = 0
    dieOne_isLocked = False
    dieTwo_isLocked = False
    dieThree_isLocked = False
    dieFour_isLocked = False
    dieFive_isLocked = False
    currentRollNum = 1 #start at roll 1 of 3
    currentPlayerNum = 1 #set player one as initial player
    playerOneScores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    playerOneUpper = 0
    playerOneLower = 0
    playerOneTotal = 0
    playerTwoScores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    playerTwoUpper = 0
    playerTwoLower = 0
    playerTwoTotal = 0

    while (True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if(ROLL_NOW.collidepoint(pygame.mouse.get_pos())):
                    print("yay")
                elif(CURR_ONE.collidepoint(pygame.mouse.get_pos())):
                    print("die A")
                elif(CURR_TWO.collidepoint(pygame.mouse.get_pos())):
                    print("die B")
                elif(CURR_THREE.collidepoint(pygame.mouse.get_pos())):
                    print("die C")
                elif(CURR_FOUR.collidepoint(pygame.mouse.get_pos())):
                    print("die D")
                elif(CURR_FIVE.collidepoint(pygame.mouse.get_pos())):
                    print("die E")
                elif(SCORING_ONE.collidepoint(pygame.mouse.get_pos())):
                    print("aces")
                elif(SCORING_TWO.collidepoint(pygame.mouse.get_pos())):
                    print("twos")
                elif(SCORING_THREE.collidepoint(pygame.mouse.get_pos())):
                    print("threes")
                elif(SCORING_FOUR.collidepoint(pygame.mouse.get_pos())):
                    print("fours")
                elif(SCORING_FIVE.collidepoint(pygame.mouse.get_pos())):
                    print("fives")
                elif(SCORING_SIX.collidepoint(pygame.mouse.get_pos())):
                    print("sixes")
                elif(pygame.Rect(0, 525, width/7, (height-525)).collidepoint(pygame.mouse.get_pos())):
                    print("3k")
                elif(pygame.Rect(width/7, 525, width/7, (height-525)).collidepoint(pygame.mouse.get_pos())):
                    print("4k")
                elif(pygame.Rect((2*width)/7, 525, width/7, (height-525)).collidepoint(pygame.mouse.get_pos())):
                    print("fh")
                elif(pygame.Rect((3*width)/7, 525, width/7, (height-525)).collidepoint(pygame.mouse.get_pos())):
                    print("smstr")
                elif(pygame.Rect((4*width)/7, 525, width/7, (height-525)).collidepoint(pygame.mouse.get_pos())):
                    print("lgstr")
                elif(pygame.Rect((5*width)/7, 525, width/7, (height-525)).collidepoint(pygame.mouse.get_pos())):
                    print("yhtz")
                elif(pygame.Rect((6*width)/7, 525, width/7, (height-525)).collidepoint(pygame.mouse.get_pos())):
                    print("chance")





        #game logic goes here
        
        


        #draw UI!

        surface.fill(BKGR_RED)

        pygame.draw.line(surface, BLACK, (0, 700/3),(width, 700/3),2) #top third horizontal line
        pygame.draw.line(surface, BLACK, (0, 2*(700/3)),(width, 2*(700/3)),2) #bottom third horizontal line
        pygame.draw.line(surface, BLACK, (500,0), (500, 700/3),  2) #top third vertical line (for logo/totals area)
        pygame.draw.line(surface, BLACK, (500, 58), (width, 58), 2) #top logo/scoring line
        pygame.draw.line(surface, BLACK, (500, 116), (width, 116), 2) #second scoring line
        pygame.draw.line(surface, BLACK, (500, 174), (width, 174), 2) #third scoring line

        #draw player indicator "box" in upper left of window
        pygame.draw.line(surface, BLACK, (300,0), (300, 75), 2)
        pygame.draw.line(surface, BLACK, (0, 75), (300, 75), 2)

        #miscellaneous UI elements
        pygame.draw.line(surface, BLACK, (0, 525), (width, 525), 2) #lower section score split line
        pygame.draw.line(surface, BLACK, (width/7, 525), (width/7, height), 2) #first/second lower score section
        pygame.draw.line(surface, BLACK, ((2*width)/7, 525), ((2*width)/7, height), 2) #second/third lower score section
        pygame.draw.line(surface, BLACK, ((3*width)/7, 525), ((3*width)/7, height), 2) #third/fourth lower score section
        pygame.draw.line(surface, BLACK, ((4*width)/7, 525), ((4*width)/7, height), 2) #fourth/fifth lower score section
        pygame.draw.line(surface, BLACK, ((5*width)/7, 525), ((5*width)/7, height), 2) #fifth/sixth lower score section
        pygame.draw.line(surface, BLACK, ((6*width)/7, 525), ((6*width)/7, height), 2) #sixth/seventh lower score section
        pygame.draw.rect(surface, GREEN, ROLL_NOW, 0, 3) #rect is at (310, 10), width 182, height 60px

        #display dice for current roll, need to be 80 pixels each with 10 px between each
        displayPicture("ace.png", CURR_ONE, 0.076555)
        displayPicture("two.png", CURR_TWO, 0.076555)
        displayPicture("three.png", CURR_THREE, 0.076555)
        displayPicture("four.png", CURR_FOUR, 0.076555)
        displayPicture("five.png", CURR_FIVE, 0.076555)

        #display die locks
        displayPicture("lock.png", LOCK_ONE, 0.057416)
        displayPicture("lock.png", LOCK_TWO, 0.057416)
        displayPicture("lock.png", LOCK_THREE, 0.057416)
        displayPicture("lock.png", LOCK_FOUR, 0.057416)
        displayPicture("lock.png", LOCK_FIVE, 0.057416)

        #display middle dice
        displayPicture("ace.png", SCORING_ONE, 0.087081)
        displayPicture("two.png", SCORING_TWO, 0.087081)
        displayPicture("three.png", SCORING_THREE, 0.087081)
        displayPicture("four.png", SCORING_FOUR, 0.087081)
        displayPicture("five.png", SCORING_FIVE, 0.087081)
        displayPicture("six.png", SCORING_SIX, 0.087081)

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
        displayMessage("Player " + str(currentPlayerNum) + ": Roll " + str(currentRollNum) + " of 3", "Raleway-Light.ttf", 32, 150, 40, WHITE, False)
        #display "roll now!" button text
        displayMessage("Roll Now!", "Raleway-SemiBold.ttf", 34, 402, 40, BLACK, True)
        #display "upper section" and "lower section" titles
        displayMessage("Upper Section", "Raleway-Light.ttf", 40, width/2, height/2.7, WHITE, True)
        displayMessage("Lower Section", "Raleway-Light.ttf", 40, width/2, 2.12*(700/3), WHITE, True)
        #display "upper section score" and "lower section score"
        displayMessage("Upper Section Score: XXX", "Raleway-SemiBold.ttf", 32, 700, 85, WHITE, False)
        displayMessage("Lower Section Score: XXX", "Raleway-SemiBold.ttf", 32, 700, 143, WHITE, False)
        displayMessage("Total Score: XXX", "Raleway-SemiBold.ttf", 32, 631, 201, WHITE, False)
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
        displayMessage("???", "Raleway-Light.ttf", 30, (width/10)+45, height/1.6, WHITE, False) #ace
        displayMessage("???", "Raleway-Light.ttf", 30, (width/10)+170, height/1.6, WHITE, False) #two
        displayMessage("???", "Raleway-Light.ttf", 30, (width/10)+295, height/1.6, WHITE, False) #three
        displayMessage("???", "Raleway-Light.ttf", 30, (width/10)+420, height/1.6, WHITE, False) #four
        displayMessage("???", "Raleway-Light.ttf", 30, (width/10)+545, height/1.6, WHITE, False) #five
        displayMessage("???", "Raleway-Light.ttf", 30, (width/10)+670, height/1.6, WHITE, False) #six
        #display lower section scores
        displayMessage("???", "Raleway-Light.ttf", 30, (2*width)/28, 580, WHITE, False) #3 of a kind
        displayMessage("???", "Raleway-Light.ttf", 30, (6*width)/28, 580, WHITE, False) #4 of a kind
        displayMessage("???", "Raleway-Light.ttf", 30, (10*width)/28, 580, WHITE, False) #full house
        displayMessage("???", "Raleway-Light.ttf", 30, (14*width)/28, 580, WHITE, False) #small straight
        displayMessage("???", "Raleway-Light.ttf", 30, (18*width)/28, 580, WHITE, False) #large straight
        displayMessage("???", "Raleway-Light.ttf", 30, (22*width)/28, 580, WHITE, False) #YAHTZEE!
        displayMessage("???", "Raleway-Light.ttf", 30, (26*width)/28, 580, WHITE, False) #chance
        pygame.display.update()

main()