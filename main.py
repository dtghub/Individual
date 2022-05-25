

from operator import truediv


def initGameData():
    gameData = {
        "board": [
            "RNBQKBNR",
            "PPPPPPPP",
            "........",
            "........",
            "........",
            "........",
            "pppppppp",
            "rnbqkbnr"
        ]
    }
    return(gameData)


def getColumnLetters():
    return("abcdefgh")

def getRowNumberString():
    return("12345678")

def outputText(stringToOutput):
    print(stringToOutput)


def convertLetterToColumNumber(columLetter):
    listOfColumnLetters = getColumnLetters()
    columnNumber = listOfColumnLetters.index(columLetter)
    return(columnNumber)



def displayBoard(boardToDisplay):

    columnLetters = "   " + getColumnLetters() + "\n"
    rowSeparator = "   --------\n"
    boardOutput = columnLetters + rowSeparator


    for rowNumber in range(0,8):
        boardOutput += str(rowNumber) + " |" + boardToDisplay[rowNumber] + "| " + str(rowNumber) + "\n"

    boardOutput += rowSeparator + columnLetters

    outputText(boardOutput)







def evaluateCoordinatesEntered(coordinatesEntered):
    isValidInput = False
    columnLetters = getColumnLetters()
    rowNumbersString = getRowNumberString()
    if len(coordinatesEntered) == 2:
        if (coordinatesEntered[0] in columnLetters) and (coordinatesEntered[1] in rowNumbersString):
            isValidInput = True
    return(isValidInput)




def getCoordinatesFromPlayer(textToDisplay):
    playerCoordinates = input(textToDisplay)
    isValidInput = evaluateCoordinatesEntered(playerCoordinates)
    return(isValidInput, playerCoordinates)




def getValueAtPositionOnBoard(coordinate, boardToCheck):
    columNumber = convertLetterToColumNumber(coordinate[0])
    valueAtPosition = boardToCheck[int(coordinate[1])][columNumber]
    return(valueAtPosition)


def identifyIfValueRepresentsEmptySquare(valueAtPositionOnBoard):
    if valueAtPositionOnBoard == ".":
        isEmptySquare = True
    else:
        isEmptySquare = False
    return(isEmptySquare)


def testForEmptySquare(coordinatesEntered, chessBoard):
    valueAtPositionOnBoard = getValueAtPositionOnBoard(coordinatesEntered, chessBoard)

    isEmptySquare = identifyIfValueRepresentsEmptySquare(valueAtPositionOnBoard)
    if isEmptySquare:
        outputText("There is no chess piece at " + coordinatesEntered)
        coordinatesEntered = ""
    return(coordinatesEntered)



def inputSquareToMoveFrom(chessBoard):
    promptText = "Please input the coordinates to move from: "
    isValidInput, coordinatesEntered = getCoordinatesFromPlayer(promptText)
    if isValidInput:
        if (len(coordinatesEntered) == 2):
            testForEmptySquare(coordinatesEntered, chessBoard)
    else:
        outputText("Sorry, I don't understand " + coordinatesEntered)
        coordinatesEntered = ""
    return(coordinatesEntered)






def getPlayerMove(gameData):
    isGameInProgress = True

    while isGameInProgress:

        moveFromCoordinate = inputSquareToMoveFrom(gameData["board"])

        




            




    return isGameInProgress, gameData 









def main():
    gameData = initGameData()


    isGameInProgress = True
    while isGameInProgress:


        displayBoard(gameData["board"])
        isGameInProgress, gameData = getPlayerMove(gameData)







main()