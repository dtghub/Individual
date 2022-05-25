

from operator import truediv


def initGameData():
    gameData = {
        "board": [
            "",
            "rnbqkbnr",
            "pppppppp",
            "........",
            "........",
            "........",
            "........",
            "PPPPPPPP",
            "RNBQKBNR",
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
    columnNumber = listOfColumnLetters.index(columLetter.lower())
    return(columnNumber)



def assembleChessBoardString(boardToDisplay):
    boardOutput = ""
    for rowNumber in range(8, 0, -1):
        boardOutput += str(rowNumber) + " |" + boardToDisplay[rowNumber] + "| " + str(rowNumber) + "\n"
    return(boardOutput)




def displayBoard(boardToDisplay):

    columnLetters = "   " + getColumnLetters() + "\n"
    rowSeparator = "   --------\n"

    boardOutput = "\n" + columnLetters + rowSeparator
    boardOutput += assembleChessBoardString(boardToDisplay)
    boardOutput += rowSeparator + columnLetters

    outputText(boardOutput)







def evaluateCoordinatesEntered(coordinatesEntered):
    isValidInput = False
    columnLetters = getColumnLetters()
    rowNumbersString = getRowNumberString()
    if len(coordinatesEntered) == 2:
        if (coordinatesEntered[0].lower() in columnLetters) and (coordinatesEntered[1] in rowNumbersString):
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


def setValueAtPositionOnBoard(coordinate, boardToChange, newValue):
    columNumber = convertLetterToColumNumber(coordinate[0])

    rowToChange = list(boardToChange[int(coordinate[1])])
    rowToChange[columNumber] = newValue
    changedRow = "".join(rowToChange)

    boardToChange[int(coordinate[1])] = changedRow
    return(boardToChange)



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
        outputText("\n\nThere is no chess piece at " + coordinatesEntered)
        coordinatesEntered = ""
    return(coordinatesEntered)



def inputSquareToMoveFrom(chessBoard):
    promptText = "Please input the coordinates to move from\ne.g. 'e2' (or 'q' to exit): "
    isValidInput, coordinatesEntered = getCoordinatesFromPlayer(promptText)
    if isValidInput:
        coordinatesEntered = testForEmptySquare(coordinatesEntered, chessBoard)
    elif len(coordinatesEntered) != 1:
        outputText("Sorry, I don't understand " + coordinatesEntered)
        coordinatesEntered = ""
    return(coordinatesEntered)



def inputSquareToMoveTo():
    promptText = "Please input the coordinates to move to: "
    isValidInput, coordinatesEntered = getCoordinatesFromPlayer(promptText)
    if not(isValidInput) and len(coordinatesEntered) != 1:
        outputText("Sorry, I don't understand " + coordinatesEntered)
        coordinatesEntered = ""
    return(coordinatesEntered)





def checkForQuitCommand(inputStringToCheck):
    isGameInProgress = True
    if inputStringToCheck.upper() == "Q":
        outputText("Exirting game.\n\n")
        isGameInProgress = False
    else:
        outputText("Sorry, I don't understand " + inputStringToCheck)
    return(isGameInProgress)




def getPlayerMove(gameData):
    isGameInProgress = True

    

    moveFromCoordinate = inputSquareToMoveFrom(gameData["board"])
    moveToCoordinate = moveFromCoordinate

    if len(moveFromCoordinate) == 2:
        moveToCoordinate = inputSquareToMoveTo()
        if len(moveToCoordinate) == 1:
            isGameInProgress = checkForQuitCommand(moveToCoordinate)

    if len(moveFromCoordinate) == 1:
        isGameInProgress = checkForQuitCommand(moveFromCoordinate)


    return isGameInProgress, moveFromCoordinate, moveToCoordinate



def movePiece(chessBoard, moveFromCoordinate, moveToCoordinate):
    valueAtPositionOnBoard = getValueAtPositionOnBoard(moveFromCoordinate, chessBoard)
    chessBoard = setValueAtPositionOnBoard(moveFromCoordinate, chessBoard, ".")
    chessBoard = setValueAtPositionOnBoard(moveToCoordinate, chessBoard, valueAtPositionOnBoard)

    return(chessBoard)





def main():
    gameData = initGameData()


    isGameInProgress = True
    while isGameInProgress:

        displayBoard(gameData["board"])
        isGameInProgress, moveFromCoordinate, moveToCoordinate = getPlayerMove(gameData)
        if moveFromCoordinate != "" and moveToCoordinate != "" and isGameInProgress:
            gameData["board"] = movePiece(gameData["board"], moveFromCoordinate, moveToCoordinate)







main()