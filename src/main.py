
import sqlite3


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


def emphasisedOutputText(stringToOutput):
    emphasisedString = "\n***"
    emphasisedString += stringToOutput
    emphasisedString += "***"
    outputText(emphasisedString)


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







def evaluatePlayerInput(inputFromPlayer):
    isValidInput = False
    columnLetters = getColumnLetters()
    rowNumbersString = getRowNumberString()
    if len(inputFromPlayer) == 2:
        if (inputFromPlayer[0].lower() in columnLetters) and (inputFromPlayer[1] in rowNumbersString):
            isValidInput = True
    return(isValidInput)




def getInputFromPlayer(textToDisplay):
    playerInput = input(textToDisplay)
    isValidInput = evaluatePlayerInput(playerInput)
    return(isValidInput, playerInput)




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


def testForEmptySquare(inputFromPlayer, chessBoard):
    valueAtPositionOnBoard = getValueAtPositionOnBoard(inputFromPlayer, chessBoard)

    isEmptySquare = identifyIfValueRepresentsEmptySquare(valueAtPositionOnBoard)
    if isEmptySquare:
        emphasisedOutputText("There is no chess piece at " + inputFromPlayer)
        inputFromPlayer = ""
    return(inputFromPlayer)



def inputSquareToMoveFrom(chessBoard):
    promptText = "Please input the coordinates to move from\ne.g. 'e2' (or 'q' to exit): "
    isValidInput, inputFromPlayer = getInputFromPlayer(promptText)
    if isValidInput:
        inputFromPlayer = testForEmptySquare(inputFromPlayer, chessBoard)
    elif len(inputFromPlayer) != 1:
        emphasisedOutputText("Sorry, I don't understand '" + inputFromPlayer+ "'")
        inputFromPlayer = ""
    return(inputFromPlayer)



def inputSquareToMoveTo():
    promptText = "Please input the coordinates to move to: "
    isValidInput, inputFromPlayer = getInputFromPlayer(promptText)
    if not(isValidInput) and len(inputFromPlayer) != 1:
        emphasisedOutputText("Sorry, I don't understand '" + inputFromPlayer+ "'")
        inputFromPlayer = ""
    return(inputFromPlayer)


def checkIfBoardTableAlreadyExists(databaseCursor):
    databaseCursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='board'")
    isAlreadyExistingTable = databaseCursor.fetchone()[0] == 1
    return isAlreadyExistingTable




def saveBoard(chessBoard):
    databaseConnection = sqlite3.connect('chessBoard.db')
    databaseCursor = databaseConnection.cursor()

    isAlreadyExistingTable = checkIfBoardTableAlreadyExists(databaseCursor)
    if isAlreadyExistingTable: 
        databaseCursor.execute("DROP TABLE board;")
    
    databaseCursor.execute("""
        CREATE TABLE board (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            row TEXT
        );
        """)
    
    for row in chessBoard:
        sqlInsertString = 'INSERT INTO board(row) VALUES("' + row + '")'
        databaseCursor.execute(sqlInsertString)
    databaseConnection.commit()
    emphasisedOutputText("Current position saved.")




def fetchSavedTableBoard(databaseCursor, chessBoard):
        databaseCursor.execute("select * from board")
        rows = databaseCursor.fetchall()
        chessBoard = []
        for row in rows:
            chessBoard.append(row[1])
        return(chessBoard)






def loadBoard(chessBoard):
    databaseConnection = sqlite3.connect('chessBoard.db')
    databaseCursor = databaseConnection.cursor()

    isAlreadyExistingTable = checkIfBoardTableAlreadyExists(databaseCursor)
    if isAlreadyExistingTable: 
        chessBoard = fetchSavedTableBoard(databaseCursor, chessBoard)
    else:
        emphasisedOutputText("No save game found.")

    databaseConnection.close()
    emphasisedOutputText("Saved board loaded.")
    return(chessBoard)






def checkForUserCommand(inputStringToCheck, chessBoard):
    isGameInProgress = True
    if inputStringToCheck.upper() == "Q":
        outputText("Exiting game.\n\n")
        isGameInProgress = False
    elif inputStringToCheck.upper() == "S":
        saveBoard(chessBoard)
    elif inputStringToCheck.upper() == "L":
        chessBoard = loadBoard(chessBoard)
    else:
        emphasisedOutputText("Sorry, I don't understand " + inputStringToCheck)
    return(isGameInProgress, chessBoard)




def getPlayerMove(gameData):
    isGameInProgress = True

    chessBoard = gameData["board"]

    moveFromCoordinate = inputSquareToMoveFrom(gameData["board"])
    moveToCoordinate = moveFromCoordinate

    if len(moveFromCoordinate) == 2:
        moveToCoordinate = inputSquareToMoveTo()
        if len(moveToCoordinate) == 1:
            isGameInProgress, chessBoard = checkForUserCommand(moveToCoordinate, chessBoard)

    if len(moveFromCoordinate) == 1:
        isGameInProgress,  chessBoard = checkForUserCommand(moveFromCoordinate, chessBoard)

    gameData["board"] = chessBoard
    return gameData, isGameInProgress, moveFromCoordinate, moveToCoordinate



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
        gameData, isGameInProgress, moveFromCoordinate, moveToCoordinate = getPlayerMove(gameData)
        if len(moveFromCoordinate) == 2 and len(moveToCoordinate) == 2 and isGameInProgress:
            gameData["board"] = movePiece(gameData["board"], moveFromCoordinate, moveToCoordinate)







main()