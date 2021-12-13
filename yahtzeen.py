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
BKGR_RED = (148, 10, 10)
WHITE =    (255, 255, 255)
BLACK =    (0, 0, 0)

#positions of six dice (to be used for upper section scoring)
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
#roll now button rect object
ROLL_NOW = pygame.Rect(310, 10, 182, 60)

#initial die values
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
frequencyList = [0, 0, 0, 0, 0, 0]

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

def rollDice():
    global dieOneValue
    global dieTwoValue
    global dieThreeValue
    global dieFourValue
    global dieFiveValue
    if (not(dieOne_isLocked)):
        dieOneValue = random.randrange(1,7)
    if (not(dieTwo_isLocked)):
        dieTwoValue = random.randrange(1,7)
    if (not(dieThree_isLocked)):
        dieThreeValue = random.randrange(1,7)
    if (not(dieFour_isLocked)):
        dieFourValue = random.randrange(1,7)
    if (not(dieFive_isLocked)):
        dieFiveValue = random.randrange(1,7)

#displays the die at the given position (dieID) and for given number in current roll area
def displayDieFromNum(dieID, num):
    if (num == 1):
        displayPicture("ace.png", dieID, 0.076555)
    elif (num == 2):
        displayPicture("two.png", dieID, 0.076555)
    elif (num == 3):
        displayPicture("three.png", dieID, 0.076555)
    elif (num == 4):
        displayPicture("four.png", dieID, 0.076555)
    elif (num == 5):
        displayPicture("five.png", dieID, 0.076555)
    elif (num == 6):
        displayPicture("six.png", dieID, 0.076555)

#CAUTION: this function only creates a list valid for the time it is called
#any roll can change this frequency list
def makeFrequencyList():
    global frequencyList
    global dieOneValue
    global dieTwoValue
    global dieThreeValue
    global dieFourValue
    global dieFiveValue
    for i in range(0, len(frequencyList)):
        frequencyList[i] = 0
    frequencyList[dieOneValue - 1] = frequencyList[dieOneValue - 1] + 1
    frequencyList[dieTwoValue - 1] = frequencyList[dieTwoValue - 1] + 1
    frequencyList[dieThreeValue - 1] = frequencyList[dieThreeValue - 1] + 1
    frequencyList[dieFourValue - 1] = frequencyList[dieFourValue - 1] + 1
    frequencyList[dieFiveValue - 1] = frequencyList[dieFiveValue - 1] + 1

#unlocks all dice for next player
def unlockDice():
    global dieOne_isLocked
    global dieTwo_isLocked
    global dieThree_isLocked
    global dieFour_isLocked
    global dieFive_isLocked

    dieOne_isLocked = False
    dieTwo_isLocked = False
    dieThree_isLocked = False
    dieFour_isLocked = False
    dieFive_isLocked = False

#resets value of all dice for next player
def clearDice():
    global dieOneValue
    global dieTwoValue
    global dieThreeValue
    global dieFourValue
    global dieFiveValue

    dieOneValue = 0
    dieTwoValue = 0
    dieThreeValue = 0
    dieFourValue = 0
    dieFiveValue = 0


def main():
    #set initial state variables
    global dieOne_isLocked
    global dieTwo_isLocked
    global dieThree_isLocked
    global dieFour_isLocked
    global dieFive_isLocked
    global frequencyList
    global dieOneValue
    global dieTwoValue
    global dieThreeValue
    global dieFourValue
    global dieFiveValue
    currentRollNum = 0 #start at roll 1 of 3
    currentPlayerNum = 1 #set player one as initial player
    playerOneScores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    playerOneUpper = 0
    playerOneLower = 0
    playerOneTotal = 0
    playerTwoScores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    playerTwoUpper = 0
    playerTwoLower = 0
    playerTwoTotal = 0
    alreadyScoredP1 = [False, False, False, False, False, False, False, False, False, False, False, False]
    alreadyScoredP2 = [False, False, False, False, False, False, False, False, False, False, False, False]

 
    while (True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if(ROLL_NOW.collidepoint(pygame.mouse.get_pos())):
                    if (currentRollNum < 3):
                        rollDice()
                        currentRollNum = currentRollNum + 1
                elif(CURR_ONE.collidepoint(pygame.mouse.get_pos())):
                    dieOne_isLocked = not(dieOne_isLocked)
                elif(CURR_TWO.collidepoint(pygame.mouse.get_pos())):
                    dieTwo_isLocked = not(dieTwo_isLocked)
                elif(CURR_THREE.collidepoint(pygame.mouse.get_pos())):
                    dieThree_isLocked = not(dieThree_isLocked)
                elif(CURR_FOUR.collidepoint(pygame.mouse.get_pos())):
                    dieFour_isLocked = not(dieFour_isLocked)
                elif(CURR_FIVE.collidepoint(pygame.mouse.get_pos())):
                    dieFive_isLocked = not(dieFive_isLocked)
                elif(SCORING_ONE.collidepoint(pygame.mouse.get_pos())):
                    if (currentPlayerNum == 1):
                        if (alreadyScoredP1[0] == False):
                            makeFrequencyList()
                            playerOneScores[0] = frequencyList[0]
                            alreadyScoredP1[0] = True
                            playerOneUpper = playerOneUpper + playerOneScores[0]
                            playerOneTotal = playerOneLower + playerOneUpper
                            currentPlayerNum = currentPlayerNum + 1
                            currentRollNum = 0
                            unlockDice()
                            clearDice()
                    elif (currentPlayerNum == 2):
                        if (alreadyScoredP2[0] == False):
                            makeFrequencyList()
                            playerTwoScores[0] = frequencyList[0]
                            alreadyScoredP2[0] = True
                            playerTwoUpper = playerTwoUpper + playerTwoScores[0]
                            playerTwoTotal = playerTwoLower + playerTwoUpper
                            currentPlayerNum = currentPlayerNum - 1
                            currentRollNum = 0
                            unlockDice()
                            clearDice()
                elif(SCORING_TWO.collidepoint(pygame.mouse.get_pos())):
                    if (currentPlayerNum == 1):
                        if (alreadyScoredP1[1] == False):
                            makeFrequencyList()
                            playerOneScores[1] = frequencyList[1]
                            alreadyScoredP1[1] = True
                            playerOneUpper = playerOneUpper + playerOneScores[1]
                            playerOneTotal = playerOneLower + playerOneUpper
                            currentPlayerNum = currentPlayerNum + 1
                            currentRollNum = 0
                            unlockDice()
                            clearDice()
                    elif (currentPlayerNum == 2):
                        if (alreadyScoredP2[1] == False):
                            makeFrequencyList()
                            playerTwoScores[1] = frequencyList[1]
                            alreadyScoredP2[1] = True
                            playerTwoUpper = playerTwoUpper + playerTwoScores[1]
                            playerTwoTotal = playerTwoLower + playerTwoUpper
                            currentPlayerNum = currentPlayerNum - 1
                            currentRollNum = 0
                            unlockDice()
                            clearDice()
                elif(SCORING_THREE.collidepoint(pygame.mouse.get_pos())):
                    if (currentPlayerNum == 1):
                        if (alreadyScoredP1[2] == False):
                            makeFrequencyList()
                            playerOneScores[2] = frequencyList[2]
                            alreadyScoredP1[2] = True
                            playerOneUpper = playerOneUpper + playerOneScores[2]
                            playerOneTotal = playerOneLower + playerOneUpper
                            currentPlayerNum = currentPlayerNum + 1
                            currentRollNum = 0
                            unlockDice()
                            clearDice()
                    elif (currentPlayerNum == 2):
                        if (alreadyScoredP2[2] == False):
                            makeFrequencyList()
                            playerTwoScores[2] = frequencyList[2]
                            alreadyScoredP2[2] = True
                            playerTwoUpper = playerTwoUpper + playerTwoScores[2]
                            playerTwoTotal = playerTwoLower + playerTwoUpper
                            currentPlayerNum = currentPlayerNum - 1
                            currentRollNum = 0
                            unlockDice()
                            clearDice()
                elif(SCORING_FOUR.collidepoint(pygame.mouse.get_pos())):
                    if (currentPlayerNum == 1):
                        if (alreadyScoredP1[3] == False):
                            makeFrequencyList()
                            playerOneScores[3] = frequencyList[3]
                            alreadyScoredP1[3] = True
                            playerOneUpper = playerOneUpper + playerOneScores[3]
                            playerOneTotal = playerOneLower + playerOneUpper
                            currentPlayerNum = currentPlayerNum + 1
                            currentRollNum = 0
                            unlockDice()
                            clearDice()
                    elif (currentPlayerNum == 2):
                        if (alreadyScoredP2[3] == False):
                            makeFrequencyList()
                            playerTwoScores[3] = frequencyList[3]
                            alreadyScoredP2[3] = True
                            playerTwoUpper = playerTwoUpper + playerTwoScores[3]
                            playerTwoTotal = playerTwoLower + playerTwoUpper
                            currentPlayerNum = currentPlayerNum - 1
                            currentRollNum = 0
                            unlockDice()
                            clearDice()
                elif(SCORING_FIVE.collidepoint(pygame.mouse.get_pos())):
                    if (currentPlayerNum == 1):
                        if (alreadyScoredP1[4] == False):
                            makeFrequencyList()
                            playerOneScores[4] = frequencyList[4]
                            alreadyScoredP1[4] = True
                            playerOneUpper = playerOneUpper + playerOneScores[4]
                            playerOneTotal = playerOneLower + playerOneUpper
                            currentPlayerNum = currentPlayerNum + 1
                            currentRollNum = 0
                            unlockDice()
                            clearDice()
                    elif (currentPlayerNum == 2):
                        if (alreadyScoredP2[4] == False):
                            makeFrequencyList()
                            playerTwoScores[4] = frequencyList[4]
                            alreadyScoredP2[4] = True
                            playerTwoUpper = playerTwoUpper + playerTwoScores[4]
                            playerTwoTotal = playerTwoLower + playerTwoUpper
                            currentPlayerNum = currentPlayerNum - 1
                            currentRollNum = 0
                            unlockDice()
                            clearDice()
                elif(SCORING_SIX.collidepoint(pygame.mouse.get_pos())):
                    if (currentPlayerNum == 1):
                        if (alreadyScoredP1[5] == False):
                            makeFrequencyList()
                            playerOneScores[5] = frequencyList[5]
                            alreadyScoredP1[5] = True
                            playerOneUpper = playerOneUpper + playerOneScores[5]
                            playerOneTotal = playerOneLower + playerOneUpper
                            currentPlayerNum = currentPlayerNum + 1
                            currentRollNum = 0
                            unlockDice()
                            clearDice()
                    elif (currentPlayerNum == 2):
                        if (alreadyScoredP2[5] == False):
                            makeFrequencyList()
                            playerTwoScores[5] = frequencyList[5]
                            alreadyScoredP2[5] = True
                            playerTwoUpper = playerTwoUpper + playerTwoScores[5]
                            playerTwoTotal = playerTwoLower + playerTwoUpper
                            currentPlayerNum = currentPlayerNum - 1
                            currentRollNum = 0
                            unlockDice()
                            clearDice()
                elif(pygame.Rect(0, 525, width/7, (height-525)).collidepoint(pygame.mouse.get_pos())): #three of a kind
                    if (currentPlayerNum == 1):
                        if (alreadyScoredP1[6] == False):
                            makeFrequencyList()
                            if (frequencyList.count(3) == 1):
                                playerOneScores[6] = 3*(frequencyList.index(3) - 1)
                                alreadyScoredP1[6] = True
                                playerOneLower = playerOneLower + playerOneScores[6]
                                playerOneTotal = playerOneLower + playerOneUpper
                                currentPlayerNum = currentPlayerNum + 1
                                currentRollNum = 0
                                unlockDice()
                                clearDice()
                            else:
                                #not a three of a kind
                                playerOneScores[6] = 0
                                alreadyScoredP1[6] = True
                                currentPlayerNum = currentPlayerNum + 1
                                currentRollNum = 0
                                unlockDice()
                                clearDice()
                    elif (currentPlayerNum == 2):
                        if (alreadyScoredP2[6] == False):
                            makeFrequencyList()
                            if (frequencyList.count(3) == 1):
                                playerTwoScores[6] = 3*(frequencyList.index(3) - 1)
                                alreadyScoredP1[6] = True
                                playerTwoLower = playerTwoLower + playerTwoScores[6]
                                playerTwoTotal = playerTwoLower + playerTwoUpper
                                currentPlayerNum = currentPlayerNum - 1
                                currentRollNum = 0
                                unlockDice()
                                clearDice()
                            else:
                                #not a three of a kind
                                playerTwoScores[6] = 0
                                alreadyScoredP2[6] = True
                                currentPlayerNum = currentPlayerNum - 1
                                currentRollNum = 0
                                unlockDice()
                                clearDice()
                elif(pygame.Rect(width/7, 525, width/7, (height-525)).collidepoint(pygame.mouse.get_pos())): #four of a kind
                    if (currentPlayerNum == 1):
                        if (alreadyScoredP1[7] == False):
                            makeFrequencyList()
                            if (frequencyList.count(4) == 1):
                                playerOneScores[7] = 4*(frequencyList.index(4) - 1)
                                alreadyScoredP1[7] = True
                                playerOneLower = playerOneLower + playerOneScores[7]
                                playerOneTotal = playerOneLower + playerOneUpper
                                currentPlayerNum = currentPlayerNum + 1
                                currentRollNum = 0
                                unlockDice()
                                clearDice()
                            else:
                                #not a four of a kind
                                playerOneScores[7] = 0
                                alreadyScoredP1[7] = True
                                currentPlayerNum = currentPlayerNum + 1
                                currentRollNum = 0
                                unlockDice()
                                clearDice()
                    elif (currentPlayerNum == 2):
                        if (alreadyScoredP2[7] == False):
                            makeFrequencyList()
                            if (frequencyList.count(4) == 1):
                                playerTwoScores[7] = 4*(frequencyList.index(4) - 1)
                                alreadyScoredP1[7] = True
                                playerTwoLower = playerTwoLower + playerTwoScores[7]
                                playerTwoTotal = playerTwoLower + playerTwoUpper
                                currentPlayerNum = currentPlayerNum - 1
                                currentRollNum = 0
                                unlockDice()
                                clearDice()
                            else:
                                #not a four of a kind
                                playerTwoScores[7] = 0
                                alreadyScoredP2[7] = True
                                currentPlayerNum = currentPlayerNum - 1
                                currentRollNum = 0
                                unlockDice()
                                clearDice()
                elif(pygame.Rect((2*width)/7, 525, width/7, (height-525)).collidepoint(pygame.mouse.get_pos())): #full house
                    if (currentPlayerNum == 1):
                        if (alreadyScoredP1[8] == False):
                            makeFrequencyList()
                            if ((frequencyList.count(3) == 1) and (frequencyList.count(2) == 1)):
                                playerOneScores[8] = 25
                                alreadyScoredP1[8] = True
                                playerOneLower = playerOneLower + playerOneScores[8]
                                playerOneTotal = playerOneLower + playerOneUpper
                                currentPlayerNum = currentPlayerNum + 1
                                currentRollNum = 0
                                unlockDice()
                                clearDice()
                            else:
                                #not a full house
                                playerOneScores[8] = 0
                                alreadyScoredP1[8] = True
                                currentPlayerNum = currentPlayerNum + 1
                                currentRollNum = 0
                                unlockDice()
                                clearDice()
                    elif (currentPlayerNum == 2):
                        if (alreadyScoredP2[8] == False):
                            makeFrequencyList()
                            if ((frequencyList.count(3) == 1) and (frequencyList.count(2) == 1)):
                                playerTwoScores[8] = 25
                                alreadyScoredP1[8] = True
                                playerTwoLower = playerTwoLower + playerTwoScores[8]
                                playerTwoTotal = playerTwoLower + playerTwoUpper
                                currentPlayerNum = currentPlayerNum - 1
                                currentRollNum = 0
                                unlockDice()
                                clearDice()
                            else:
                                #not a full house
                                playerTwoScores[8] = 0
                                alreadyScoredP2[8] = True
                                currentPlayerNum = currentPlayerNum - 1
                                currentRollNum = 0
                                unlockDice()
                                clearDice()
                elif(pygame.Rect((3*width)/7, 525, width/7, (height-525)).collidepoint(pygame.mouse.get_pos())):
                    print("smstr")
                elif(pygame.Rect((4*width)/7, 525, width/7, (height-525)).collidepoint(pygame.mouse.get_pos())):
                    print("lgstr")
                elif(pygame.Rect((5*width)/7, 525, width/7, (height-525)).collidepoint(pygame.mouse.get_pos())): #yahtzee
                    if (currentPlayerNum == 1):
                        if (alreadyScoredP1[11] == False):
                            makeFrequencyList()
                            if (frequencyList.count(5) == 1):
                                playerOneScores[11] = 50
                                alreadyScoredP1[11] = True
                                playerOneLower = playerOneLower + playerOneScores[11]
                                playerOneTotal = playerOneLower + playerOneUpper
                                currentPlayerNum = currentPlayerNum + 1
                                currentRollNum = 0
                                unlockDice()
                                clearDice()
                            else:
                                #not a yahtzee
                                playerOneScores[11] = 0
                                alreadyScoredP1[11] = True
                                currentPlayerNum = currentPlayerNum + 1
                                currentRollNum = 0
                                unlockDice()
                                clearDice()
                    elif (currentPlayerNum == 2):
                        if (alreadyScoredP2[11] == False):
                            makeFrequencyList()
                            if (frequencyList.count(5) == 1):
                                playerTwoScores[11] = 50
                                alreadyScoredP1[11] = True
                                playerTwoLower = playerTwoLower + playerTwoScores[11]
                                playerTwoTotal = playerTwoLower + playerTwoUpper
                                currentPlayerNum = currentPlayerNum - 1
                                currentRollNum = 0
                                unlockDice()
                                clearDice()
                            else:
                                #not a yahtzee
                                playerTwoScores[11] = 0
                                alreadyScoredP2[11] = True
                                currentPlayerNum = currentPlayerNum - 1
                                currentRollNum = 0
                                unlockDice()
                                clearDice()
                elif(pygame.Rect((6*width)/7, 525, width/7, (height-525)).collidepoint(pygame.mouse.get_pos())):
                    if (currentPlayerNum == 1):
                        if (alreadyScoredP1[12] == False):
                            playerOneScores[12] = dieOneValue + dieTwoValue + dieThreeValue + dieFourValue + dieFiveValue
                            alreadyScoredP1[12] = True
                            playerOneLower = playerOneLower + playerOneScores[12]
                            playerOneTotal = playerOneLower + playerOneUpper
                            currentPlayerNum = currentPlayerNum + 1
                            currentRollNum = 0
                            unlockDice()
                            clearDice()
                    elif (currentPlayerNum == 2):
                        if (alreadyScoredP2[12] == False):
                            playerTwoScores[12] = dieOneValue + dieTwoValue + dieThreeValue + dieFourValue + dieFiveValue
                            alreadyScoredP2[12] = True
                            playerTwoLower = playerTwoLower + playerTwoScores[12]
                            playerTwoTotal = playerTwoLower + playerTwoUpper
                            currentPlayerNum = currentPlayerNum - 1
                            currentRollNum = 0
                            unlockDice()
                            clearDice()

        #draw current roll state
        displayDieFromNum(CURR_ONE, dieOneValue)
        if (dieOne_isLocked):
            displayPicture("lock.png", LOCK_ONE, 0.057416)
        displayDieFromNum(CURR_TWO, dieTwoValue)
        if (dieTwo_isLocked):
            displayPicture("lock.png", LOCK_TWO, 0.057416)
        displayDieFromNum(CURR_THREE, dieThreeValue)
        if (dieThree_isLocked):
            displayPicture("lock.png", LOCK_THREE, 0.057416)
        displayDieFromNum(CURR_FOUR, dieFourValue)
        if (dieFour_isLocked):
            displayPicture("lock.png", LOCK_FOUR, 0.057416)
        displayDieFromNum(CURR_FIVE, dieFiveValue)
        if (dieFive_isLocked):
            displayPicture("lock.png", LOCK_FIVE, 0.057416)
        
        pygame.display.update()

        #draw "general" UI elements

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
        if (currentPlayerNum == 1):
            displayMessage("Upper Section Score: " + str(playerOneUpper), "Raleway-SemiBold.ttf", 32, 700, 85, WHITE, False)
            displayMessage("Lower Section Score: " + str(playerOneLower), "Raleway-SemiBold.ttf", 32, 700, 143, WHITE, False)
            displayMessage("Total Score: " + str(playerOneTotal), "Raleway-SemiBold.ttf", 32, 631, 201, WHITE, False)
        elif (currentPlayerNum == 2):
            displayMessage("Upper Section Score: " + str(playerTwoUpper), "Raleway-SemiBold.ttf", 32, 700, 85, WHITE, False)
            displayMessage("Lower Section Score: " + str(playerTwoLower), "Raleway-SemiBold.ttf", 32, 700, 143, WHITE, False)
            displayMessage("Total Score: " + str(playerTwoTotal), "Raleway-SemiBold.ttf", 32, 631, 201, WHITE, False)
        #display each lower section category name
        displayMessage("3 of a Kind", "Smooch-Regular.ttf", 27, width/14, 542, WHITE, False)
        displayMessage("4 of a Kind", "Smooch-Regular.ttf", 27, (3*width)/14, 542, WHITE, False)
        displayMessage("Full House", "Smooch-Regular.ttf", 27, (5*width)/14, 542, WHITE, False)
        displayMessage("Sm. Straight", "Smooch-Regular.ttf", 27, (7*width)/14, 542, WHITE, False)
        displayMessage("Lg. Straight", "Smooch-Regular.ttf", 27, (9*width)/14, 542, WHITE, False)
        displayMessage("Yahtzee!", "Smooch-Regular.ttf", 27, (11*width)/14, 542, WHITE, False)
        displayMessage("Chance", "Smooch-Regular.ttf", 27, (13*width)/14, 542, WHITE, False)

        #prepare to display scores
        if (currentPlayerNum == 1):
            theseAces = playerOneScores[0]
            theseTwos = playerOneScores[1]
            theseThrees = playerOneScores[2]
            theseFours = playerOneScores[3]
            theseFives = playerOneScores[4]
            theseSixes = playerOneScores[5]
            this3Kind = playerOneScores[6]
            this4Kind = playerOneScores[7]
            thisFullHouse = playerOneScores[8]
            thisSmStr = playerOneScores[9]
            thisLgStr = playerOneScores[10]
            thisYahtzee = playerOneScores[11]
            thisChance = playerOneScores[12]
        elif (currentPlayerNum == 2):
            theseAces = playerTwoScores[0]
            theseTwos = playerTwoScores[1]
            theseThrees = playerTwoScores[2]
            theseFours = playerTwoScores[3]
            theseFives = playerTwoScores[4]
            theseSixes = playerTwoScores[5]
            this3Kind = playerTwoScores[6]
            this4Kind = playerTwoScores[7]
            thisFullHouse = playerTwoScores[8]
            thisSmStr = playerTwoScores[9]
            thisLgStr = playerTwoScores[10]
            thisYahtzee = playerTwoScores[11]
            thisChance = playerTwoScores[12]

        #display upper section scores
        displayMessage(str(theseAces), "Raleway-Light.ttf", 30, (width/10)+45, height/1.6, WHITE, False) #ace
        displayMessage(str(theseTwos), "Raleway-Light.ttf", 30, (width/10)+170, height/1.6, WHITE, False) #two
        displayMessage(str(theseThrees), "Raleway-Light.ttf", 30, (width/10)+295, height/1.6, WHITE, False) #three
        displayMessage(str(theseFours), "Raleway-Light.ttf", 30, (width/10)+420, height/1.6, WHITE, False) #four
        displayMessage(str(theseFives), "Raleway-Light.ttf", 30, (width/10)+545, height/1.6, WHITE, False) #five
        displayMessage(str(theseSixes), "Raleway-Light.ttf", 30, (width/10)+670, height/1.6, WHITE, False) #six
        #display lower section scores
        displayMessage(str(this3Kind), "Raleway-Light.ttf", 30, (2*width)/28, 580, WHITE, False) #3 of a kind
        displayMessage(str(this4Kind), "Raleway-Light.ttf", 30, (6*width)/28, 580, WHITE, False) #4 of a kind
        displayMessage(str(thisFullHouse), "Raleway-Light.ttf", 30, (10*width)/28, 580, WHITE, False) #full house
        displayMessage(str(thisSmStr), "Raleway-Light.ttf", 30, (14*width)/28, 580, WHITE, False) #small straight
        displayMessage(str(thisLgStr), "Raleway-Light.ttf", 30, (18*width)/28, 580, WHITE, False) #large straight
        displayMessage(str(thisYahtzee), "Raleway-Light.ttf", 30, (22*width)/28, 580, WHITE, False) #YAHTZEE!
        displayMessage(str(thisChance), "Raleway-Light.ttf", 30, (26*width)/28, 580, WHITE, False) #chance

main()