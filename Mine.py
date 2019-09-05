import sys

import random

 

class Cell():         

                def __init__(self, xPos, yPos, status, isHidden):

                                self.xPos = xPos

                                self.yPos = yPos

                                self.status = status

                                self.isHidden = isHidden

 

                def __getitem__(self, key):

                                print('Hello! I am a cell in pos ' + str(self.xPos) + ',' + str(self.yPos))

 

#draw the grid

def drawGrid():

                print('')

                xAxisString = '  '                

                for x in range(int(xLength)):

                                xAxisString = xAxisString + str(x) + ' '

                               

                print(xAxisString)

               

                for y in range(int(yLength)):                                       

                                print(y),

                                for x in range(int(xLength)):

                                                if cellList[x][y].isHidden == False:

                                                                print(str(cellList[x][y].status)),

                                                else:

                                                                print('-'),

                                print('')

                print('')

               

#set grid width, height, bomb count

while(True):

                xLength = raw_input("Enter grid length: ")

                yLength = raw_input("Enter grid height: ")

                numBombs = raw_input("Enter number of bombs: ")

 

                if not(xLength.isdigit()) or not(yLength.isdigit()) or not(numBombs.isdigit()):

                                print 'Grid sizes and bomb count should be numbers'

                                continue

                else:

                                break

                               

#declare a 2d array of size x,y containing instances of the Cell class

cellList = [[Cell(x,y,'-',True) for y in range(int(yLength))] for x in range(int(xLength))]

 

#distribute the bombs

for x in range(0, int(numBombs)):

                currentRandomX = random.randint(0,int(xLength)-1)

                currentRandomY = random.randint(0,int(yLength)-1)

               

                #is the randomly selected cell already a bomb?

                while True:

                                if cellList[currentRandomX][currentRandomY].status == '-':

                                                cellList[currentRandomX][currentRandomY].status = 'B'

                                                #cellList[currentRandomX][currentRandomY].isHidden = False

                                                break

                                else:

                                                currentRandomX = random.randint(0,int(xLength)-1)

                                                currentRandomY = random.randint(0,int(yLength)-1)

 

                                               

#expose all of the bombs (called when bomb is found

def exposeBombs():

                bombCount = 0

                for x in range(0, int(xLength)):   

                                for y in range(0, int(yLength)):  

                                                if cellList[x][y].status == 'B':

                                                                bombCount = bombCount + 1

                                                                cellList[x][y].isHidden = False

                print(str(bombCount) + ' bombs found')

 

#assign the counts for cells adjacent to bombs

for x in range(0, int(xLength)):   

                for y in range(0, int(yLength)):                  

                                countAdjacentBombs = 0

                                #print(str(x) + ',' + str(y))

 

                                try:

                                                #bomb left

                                                if x > 0 and cellList[x][y].status <> 'B' and cellList[x-1][y].status == 'B':                                       

                                                                countAdjacentBombs = countAdjacentBombs + 1

                                                #bomb right

                                                if x < xLength and cellList[x][y].status <> 'B' and cellList[x+1][y].status == 'B':                        

                                                                countAdjacentBombs = countAdjacentBombs + 1

                                                #bomb below

                                                if y > 0 and cellList[x][y].status <> 'B' and cellList[x][y-1].status == 'B':

                                                                countAdjacentBombs = countAdjacentBombs + 1

                                                #bomb above

                                                if y < yLength and cellList[x][y].status <> 'B' and cellList[x][y+1].status == 'B':

                                                                countAdjacentBombs = countAdjacentBombs + 1                                             

                                except:

                                                pass

                                               

                                if countAdjacentBombs > 0:

                                                cellList[x][y].status = str(countAdjacentBombs)

                                y = y + 1

                x = x + 1

 

drawGrid()

               

xInput = ''

 

#check the selected cell for bombs

def check(cellList, xPos, yPos, originalXPos, originalYPos, xLength, yLength):

                status = cellList[int(xPos)][int(yPos)].status

                isHidden = cellList[int(xPos)][int(yPos)].isHidden

                xPos = cellList[int(xPos)][int(yPos)].xPos

                yPos = cellList[int(xPos)][int(yPos)].yPos

               

                if cellList[int(originalXPos)][int(originalYPos)].status == 'B':

                                cellList[int(xPos)][int(yPos)].status = 'B'

                                cellList[int(xPos)][int(yPos)].isHidden = False

                                print('BOOM!!')

                                exposeBombs()

                                drawGrid()

                                print('Bye!')

                                quit()

                               

                elif status == '-':

                                cellList[int(xPos)][int(yPos)].status = 'X'

                                cellList[int(xPos)][int(yPos)].isHidden = False

                               

                                #cell above                                        

                                if int(yPos) > 0: 

                                                check(cellList, int(xPos), int(yPos) - 1, originalXPos, originalYPos, xLength, yLength)

                                               

                                #cell below

                                if int(yPos) + 1 < int(yLength):

                                                check(cellList, int(xPos), int(yPos) + 1, originalXPos, originalYPos, xLength, yLength)

                                               

                                #cell left

                                if int(xPos) > 0:

                                                check(cellList, int(xPos) - 1, int(yPos), originalXPos, originalYPos, xLength, yLength)

                                               

                                #cell right                                           

                                if int(xPos)+ 1 < int(xLength):

                                                check(cellList, int(xPos) + 1, int(yPos), originalXPos, originalYPos, xLength, yLength)

                                               

                elif status.isdigit():

                                cellList[int(xPos)][int(yPos)].isHidden = False

               

               

#get user input for guesses

while True:

                xInput = raw_input("Enter X co-ordinate or Q to quit: ")

               

                if xInput.upper() == 'Q':

                                print('Bye!')

                                break

                               

                if not(xInput.isdigit()):

                                print 'Please enter a number for X axis'

                                continue

                               

                if int(xInput) >= int(xLength):

                                print 'X axis is too big!'

                                continue

               

                yInput = raw_input("Enter Y co-ordinate or Q to quit: ")

                if xInput.upper() == 'Q':

                                print('Bye!')

                                break

                               

                if not(yInput.isdigit()):

                                print 'Please enter a number for Y axis'

                                continue

                               

                if int(yInput) >= int(yLength):

                                print 'Y axis is too big!'

                                continue                             

               

                if cellList[int(xInput)][int(yInput)].isHidden == False:

                                print('This cell has already been uncovered')

                else:     

                                check(cellList, xInput, yInput, xInput, yInput, xLength, yLength)

 

                drawGrid()

 
