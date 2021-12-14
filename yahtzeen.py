import pygame
import sys
import random
from player import Player

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
dieValues = [0, 0, 0, 0, 0]
diceLockedList = [False, False, False, False, False]
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
    global dieValues

    if (not(diceLockedList[0])):
        dieValues[0] = random.randrange(1,7)
    if (not(diceLockedList[1])):
        dieValues[1] = random.randrange(1,7)
    if (not(diceLockedList[2])):
        dieValues[2] = random.randrange(1,7)
    if (not(diceLockedList[3])):
        dieValues[3] = random.randrange(1,7)
    if (not(diceLockedList[4])):
        dieValues[4] = random.randrange(1,7)

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
#the list is the frequency of each value, represented for (index + 1) in a roll
def makeFrequencyList():
    global frequencyList

    for i in range(0, len(frequencyList)):
        frequencyList[i] = 0

    for j in range(0, 6):
        if (dieValues.count(j + 1) > 0):
            frequencyList[j] = dieValues.count(j + 1)

#scores die type of num (1-6) for thisPlayer (should be currentPlayer)
def scoreUpperSection(thisPlayer, num):
    global frequencyList
    makeFrequencyList()
    thisPlayer.allScores[num - 1] = num*frequencyList[num - 1]
    thisPlayer.alreadyScored[num - 1] = True
    thisPlayer.upperScore = thisPlayer.upperScore + thisPlayer.allScores[num - 1]
    thisPlayer.totalScore = thisPlayer.lowerScore + thisPlayer.upperScore

#scores x of a kind for thisPlayer, where x is num (note: num = 5 = Yahtzee)
def scoreOfAKind(thisPlayer, num):
    global frequencyList
    global dieValues
    arrayPos = 0 #where to place score

    makeFrequencyList()
    if (frequencyList.count(num) == 1):
        if (num == 3 or num == 4):
            thisPlayer.allScores[num + 3] = sum(dieValues)
        elif (num == 5):
            thisPlayer.allScores[11] = 50
        thisPlayer.alreadyScored[arrayPos] = True
        thisPlayer.lowerScore = thisPlayer.lowerScore + thisPlayer.allScores[arrayPos]
        thisPlayer.totalScore = thisPlayer.lowerScore + thisPlayer.upperScore
    else:
        #not a three of a kind
        thisPlayer.alreadyScored[arrayPos] = True

#resets value of and unlocks all dice for next player
def clearDice():
    global dieValues
    global diceLockedList

    dieValues = [0, 0, 0, 0, 0]
    diceLockedList = [False, False, False, False, False]


def finishGame(p1Score, p2Score):
    while (True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
        #display final scores and win messages
        surface.fill(BKGR_RED)
        displayMessage("Game Over!", "Smooch-Regular.ttf", 100, width/2, height/6, WHITE, False)
        displayMessage("Player 1's Score........." + str(p1Score), "Raleway-SemiBold.ttf", 60, width/2, (2*height)/6, WHITE, False)
        displayMessage("Player 2's Score........." + str(p2Score), "Raleway-SemiBold.ttf", 60, width/2, (3*height)/6, WHITE, False)
        if (p1Score > p2Score):
            displayMessage("Player 1 wins by " + str(p1Score - p2Score) + " points!", "Raleway-SemiBold.ttf", 60, width/2, (4*height)/5, WHITE, False)
        elif (p2Score > p1Score):
            displayMessage("Player 2 wins by " + str(p2Score - p1Score) + " points!", "Raleway-SemiBold.ttf", 60, width/2, (4*height)/5, WHITE, False)
        else:
            displayMessage("It's a tie!", "Raleway-SemiBold.ttf", 60, width/2, (4*height)/5, WHITE, False)
        pygame.display.update()


def main():
    #set initial state variables
    global diceLockedList
    global dieValues
    global frequencyList
    currentRollNum = 0 #start at roll 1 of 3

    player1 = Player(1)
    player2 = Player(2)
    currentPlayer = player1

    while (True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)): #quit game
                pygame.quit()
                sys.exit()
            if (event.type == pygame.MOUSEBUTTONDOWN): #mouse click events
                if(ROLL_NOW.collidepoint(pygame.mouse.get_pos())):
                    if (currentRollNum < 3):
                        rollDice()
                        currentRollNum = currentRollNum + 1
                elif(CURR_ONE.collidepoint(pygame.mouse.get_pos())): #clicked leftmost rolled die
                    diceLockedList[0] = not(diceLockedList[0])
                elif(CURR_TWO.collidepoint(pygame.mouse.get_pos())):
                    diceLockedList[1] = not(diceLockedList[1])
                elif(CURR_THREE.collidepoint(pygame.mouse.get_pos())):
                    diceLockedList[2] = not(diceLockedList[2])
                elif(CURR_FOUR.collidepoint(pygame.mouse.get_pos())):
                    diceLockedList[3] = not(diceLockedList[3])
                elif(CURR_FIVE.collidepoint(pygame.mouse.get_pos())): #clicked rightmost rolled die
                    diceLockedList[4] = not(diceLockedList[4])
                elif(SCORING_ONE.collidepoint(pygame.mouse.get_pos())): #score for aces
                    if (currentPlayer.alreadyScored[0] == False):
                        scoreUpperSection(currentPlayer, 1)

                        if (currentPlayer.playerNumber == 1):
                            currentPlayer = player2
                        else:
                            currentPlayer = player1
                        currentRollNum = 0
                        clearDice()
                elif(SCORING_TWO.collidepoint(pygame.mouse.get_pos())): #score for twos
                    if (currentPlayer.alreadyScored[1] == False):
                        scoreUpperSection(currentPlayer, 2)

                        if (currentPlayer.playerNumber == 1):
                            currentPlayer = player2
                        else:
                            currentPlayer = player1
                        currentRollNum = 0
                        clearDice()
                elif(SCORING_THREE.collidepoint(pygame.mouse.get_pos())): #score for threes
                    if (currentPlayer.alreadyScored[2] == False):
                        scoreUpperSection(currentPlayer, 3)

                        if (currentPlayer.playerNumber == 1):
                            currentPlayer = player2
                        else:
                            currentPlayer = player1
                        currentRollNum = 0
                        clearDice()
                elif(SCORING_FOUR.collidepoint(pygame.mouse.get_pos())): #score for fours
                    if (currentPlayer.alreadyScored[3] == False):
                        scoreUpperSection(currentPlayer, 4)
                        
                        if (currentPlayer.playerNumber == 1):
                            currentPlayer = player2
                        else:
                            currentPlayer = player1
                        currentRollNum = 0
                        clearDice()
                elif(SCORING_FIVE.collidepoint(pygame.mouse.get_pos())): #score for fives
                    if (currentPlayer.alreadyScored[4] == False):
                        scoreUpperSection(currentPlayer, 5)
                        
                        if (currentPlayer.playerNumber == 1):
                            currentPlayer = player2
                        else:
                            currentPlayer = player1
                        currentRollNum = 0
                        clearDice()
                elif(SCORING_SIX.collidepoint(pygame.mouse.get_pos())): #score for sixes
                    if (currentPlayer.alreadyScored[5] == False):
                        scoreUpperSection(currentPlayer, 6)
                        
                        if (currentPlayer.playerNumber == 1):
                            currentPlayer = player2
                        else:
                            currentPlayer = player1
                        currentRollNum = 0
                        clearDice()
                elif(pygame.Rect(0, 525, width/7, (height-525)).collidepoint(pygame.mouse.get_pos())): #three of a kind
                    if (currentPlayer.alreadyScored[6] == False):
                        scoreOfAKind(currentPlayer, 3)

                        if (currentPlayer.playerNumber == 1):
                            currentPlayer = player2
                        else:
                            currentPlayer = player1

                        currentRollNum = 0
                        clearDice()
                elif(pygame.Rect(width/7, 525, width/7, (height-525)).collidepoint(pygame.mouse.get_pos())): #four of a kind
                    if (currentPlayer.alreadyScored[7] == False):
                        scoreOfAKind(currentPlayer, 4)

                        if (currentPlayer.playerNumber == 1):
                            currentPlayer = player2
                        else:
                            currentPlayer = player1
                            
                        currentRollNum = 0
                        clearDice()
                elif(pygame.Rect((2*width)/7, 525, width/7, (height-525)).collidepoint(pygame.mouse.get_pos())): #full house
                    if (currentPlayer.alreadyScored[8] == False):
                        makeFrequencyList()
                        if ((frequencyList.count(3) == 1) and (frequencyList.count(2) == 1)):
                            currentPlayer.allScores[8] = 25
                            currentPlayer.alreadyScored[8] = True
                            currentPlayer.lowerScore = currentPlayer.lowerScore + currentPlayer.allScores[8]
                            currentPlayer.totalScore = currentPlayer.lowerScore + currentPlayer.upperScore
                        else:
                            #not a full house
                            currentPlayer.alreadyScored[8] = True

                        if (currentPlayer.playerNumber == 1):
                            currentPlayer = player2
                        else:
                            currentPlayer = player1

                        currentRollNum = 0
                        clearDice()
                elif(pygame.Rect((3*width)/7, 525, width/7, (height-525)).collidepoint(pygame.mouse.get_pos())): #small straight
                    if (currentPlayer.alreadyScored[9] == False):
                        #check if we have small straight
                        smStrOne = [1, 2, 3, 4]
                        smStrTwo = [2, 3, 4, 5]
                        smStrThree = [3, 4, 5, 6]
                        #algorithm for checking subarray from: https://thispointer.com/python-check-if-a-list-contains-all-the-elements-of-another-list/
                        validSmStr = False
                        #check for three possibilities of small straights
                        validSmStr = all(elem in dieValues for elem in smStrOne)

                        if (not(validSmStr)):
                            validSmStr = all(elem in dieValues for elem in smStrTwo)
                        
                        if (not(validSmStr)):
                            validSmStr = all(elem in dieValues for elem in smStrThree)
                        
                        if (validSmStr):
                            currentPlayer.allScores[9] = 30
                            currentPlayer.alreadyScored[9] = True
                            currentPlayer.lowerScore = currentPlayer.lowerScore + currentPlayer.allScores[9]
                            currentPlayer.totalScore = currentPlayer.lowerScore + currentPlayer.upperScore
                        else:
                            currentPlayer.alreadyScored[9] = True

                        if (currentPlayer.playerNumber == 1):
                            currentPlayer = player2
                        else:
                            currentPlayer = player1
                            
                        currentRollNum = 0
                        clearDice()
                elif(pygame.Rect((4*width)/7, 525, width/7, (height-525)).collidepoint(pygame.mouse.get_pos())): #large straight
                    if (currentPlayer.alreadyScored[10] == False):
                        #check if valid large straight
                        lgStrOne = [1, 2, 3, 4, 5]
                        lgStrTwo = [2, 3, 4, 5, 6]
                        #algorithm for checking subarray from: https://thispointer.com/python-check-if-a-list-contains-all-the-elements-of-another-list/
                        validLgStr = False
                        #check two possibilites of large straights
                        validLgStr = all(elem in dieValues for elem in lgStrOne)
                        
                        if (not(validLgStr)):
                            validLgStr = all(elem in dieValues for elem in lgStrTwo)

                        if (validLgStr):
                            currentPlayer.allScores[10] = 40
                            currentPlayer.alreadyScored[10] = True
                            currentPlayer.lowerScore = currentPlayer.lowerScore + currentPlayer.allScores[10]
                            currentPlayer.totalScore = currentPlayer.lowerScore + currentPlayer.upperScore
                        else:
                            currentPlayer.alreadyScored[10] = True

                        if (currentPlayer.playerNumber == 1):
                            currentPlayer = player2
                        else:
                            currentPlayer = player1
                            
                        currentRollNum = 0
                        clearDice()
                elif(pygame.Rect((5*width)/7, 525, width/7, (height-525)).collidepoint(pygame.mouse.get_pos())): #yahtzee
                    if (currentPlayer.alreadyScored[11] == False):
                        scoreOfAKind(currentPlayer, 5)
                        
                        if (currentPlayer.playerNumber == 1):
                            currentPlayer = player2
                        else:
                            currentPlayer = player1
                            
                        currentRollNum = 0
                        clearDice()
                elif(pygame.Rect((6*width)/7, 525, width/7, (height-525)).collidepoint(pygame.mouse.get_pos())): #chance
                    if (currentPlayer.alreadyScored[12] == False):
                        currentPlayer.allScores[12] = sum(dieValues)
                        currentPlayer.alreadyScored[12] = True
                        currentPlayer.lowerScore = currentPlayer.lowerScore + currentPlayer.allScores[12]
                        currentPlayer.totalScore = currentPlayer.lowerScore + currentPlayer.upperScore

                        if (currentPlayer.playerNumber == 1):
                            currentPlayer = player2
                        else:
                            currentPlayer = player1
                            
                        currentRollNum = 0
                        clearDice()

        #draw current roll state
        displayDieFromNum(CURR_ONE, dieValues[0])
        if (diceLockedList[0]):
            displayPicture("lock.png", LOCK_ONE, 0.057416)
        displayDieFromNum(CURR_TWO, dieValues[1])
        if (diceLockedList[1]):
            displayPicture("lock.png", LOCK_TWO, 0.057416)
        displayDieFromNum(CURR_THREE, dieValues[2])
        if (diceLockedList[2]):
            displayPicture("lock.png", LOCK_THREE, 0.057416)
        displayDieFromNum(CURR_FOUR, dieValues[3])
        if (diceLockedList[3]):
            displayPicture("lock.png", LOCK_FOUR, 0.057416)
        displayDieFromNum(CURR_FIVE, dieValues[4])
        if (diceLockedList[4]):
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
        displayMessage("Player " + str(currentPlayer.playerNumber) + ": Roll " + str(currentRollNum) + " of 3", "Raleway-Light.ttf", 32, 150, 40, WHITE, False)

        #display "roll now!" button text
        displayMessage("Roll Now!", "Raleway-SemiBold.ttf", 34, 402, 40, BLACK, True)

        #display "upper section" and "lower section" titles
        displayMessage("Upper Section", "Raleway-Light.ttf", 40, width/2, height/2.7, WHITE, True)
        displayMessage("Lower Section", "Raleway-Light.ttf", 40, width/2, 2.12*(700/3), WHITE, True)

        #display "upper section score" and "lower section score"
        displayMessage("Upper Section Score: " + str(currentPlayer.upperScore), "Raleway-SemiBold.ttf", 32, 700, 85, WHITE, False)
        displayMessage("Lower Section Score: " + str(currentPlayer.lowerScore), "Raleway-SemiBold.ttf", 32, 700, 143, WHITE, False)
        displayMessage("Total Score: " + str(currentPlayer.totalScore), "Raleway-SemiBold.ttf", 32, 631, 201, WHITE, False)

        #display each lower section category name
        displayMessage("3 of a Kind", "Smooch-Regular.ttf", 27, width/14, 542, WHITE, False)
        displayMessage("4 of a Kind", "Smooch-Regular.ttf", 27, (3*width)/14, 542, WHITE, False)
        displayMessage("Full House", "Smooch-Regular.ttf", 27, (5*width)/14, 542, WHITE, False)
        displayMessage("Sm. Straight", "Smooch-Regular.ttf", 27, (7*width)/14, 542, WHITE, False)
        displayMessage("Lg. Straight", "Smooch-Regular.ttf", 27, (9*width)/14, 542, WHITE, False)
        displayMessage("Yahtzee!", "Smooch-Regular.ttf", 27, (11*width)/14, 542, WHITE, False)
        displayMessage("Chance", "Smooch-Regular.ttf", 27, (13*width)/14, 542, WHITE, False)

        #display upper section scores
        displayMessage(str(currentPlayer.allScores[0]), "Raleway-Light.ttf", 30, (width/10)+45, height/1.6, WHITE, False) #ace
        displayMessage(str(currentPlayer.allScores[1]), "Raleway-Light.ttf", 30, (width/10)+170, height/1.6, WHITE, False) #two
        displayMessage(str(currentPlayer.allScores[2]), "Raleway-Light.ttf", 30, (width/10)+295, height/1.6, WHITE, False) #three
        displayMessage(str(currentPlayer.allScores[3]), "Raleway-Light.ttf", 30, (width/10)+420, height/1.6, WHITE, False) #four
        displayMessage(str(currentPlayer.allScores[4]), "Raleway-Light.ttf", 30, (width/10)+545, height/1.6, WHITE, False) #five
        displayMessage(str(currentPlayer.allScores[5]), "Raleway-Light.ttf", 30, (width/10)+670, height/1.6, WHITE, False) #six
        #display lower section scores
        displayMessage(str(currentPlayer.allScores[6]), "Raleway-Light.ttf", 30, (2*width)/28, 580, WHITE, False) #3 of a kind
        displayMessage(str(currentPlayer.allScores[7]), "Raleway-Light.ttf", 30, (6*width)/28, 580, WHITE, False) #4 of a kind
        displayMessage(str(currentPlayer.allScores[8]), "Raleway-Light.ttf", 30, (10*width)/28, 580, WHITE, False) #full house
        displayMessage(str(currentPlayer.allScores[9]), "Raleway-Light.ttf", 30, (14*width)/28, 580, WHITE, False) #small straight
        displayMessage(str(currentPlayer.allScores[10]), "Raleway-Light.ttf", 30, (18*width)/28, 580, WHITE, False) #large straight
        displayMessage(str(currentPlayer.allScores[11]), "Raleway-Light.ttf", 30, (22*width)/28, 580, WHITE, False) #YAHTZEE!
        displayMessage(str(currentPlayer.allScores[12]), "Raleway-Light.ttf", 30, (26*width)/28, 580, WHITE, False) #chance

        #if all moves have been made, display results; game must be restarted to play again
        if (player1.alreadyScored.count(True) == 13 and player2.alreadyScored.count(True) == 13):
            finishGame(player1.totalScore, player2.totalScore)
            break

main()