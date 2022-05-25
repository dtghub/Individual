

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

    print(boardOutput)







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







def getPlayerMove(gameData):
    isGameInProgress = True

    while isGameInProgress:

        
        promptText = "Please input the coordinates to move from: "
        isValidInput, coordinatesEntered = getCoordinatesFromPlayer(promptText)
        if isValidInput and (len(coordinatesEntered) == 2):
            valueAtPositionOnBoard = getValueAtPositionOnBoard(coordinatesEntered, gameData["board"])
            if valueAtPositionOnBoard == ".":
                isChessPieceOnSquare = False
            else:
                isChessPieceOnSquare = True

            




    return isGameInProgress, gameData 









def main():
    gameData = initGameData()


    isGameInProgress = True
    while isGameInProgress:


        displayBoard(gameData["board"])
        isGameInProgress, gameData = getPlayerMove(gameData)







main()