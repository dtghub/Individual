
import sqlite3 as sl


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



def saveBoard(chessBoard):


    con = sl.connect('chessBoard.db')
    c = con.cursor()

    # Generic cde used to check if table exists   
    #get the count of tables with the name
    c.execute(""" SELECT count(name) FROM sqlite_master WHERE type='table' AND name='board' """)

    #if the count is 1, then table exists
    if c.fetchone()[0] == 1: 
        c.execute("""
        DROP TABLE board;
        """)
        
        print('Table existed.')
    




    c.execute("""
        CREATE TABLE board (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            row TEXT
        );
        """)
    
    for row in chessBoard:
        sqlInsertString = 'INSERT INTO board(row) VALUES("' + row + '")'
        c.execute(sqlInsertString)
        
    con.commit()



def loadBoard(chessBoard):

    

    conn = sl.connect('chessBoard.db')
    c = conn.cursor()

    # Generic cde used to check if table exists   
    #get the count of tables with the name
    c.execute(""" SELECT count(name) FROM sqlite_master WHERE type='table' AND name='board' """)


    # print(c.fetchone()[0])
    #if the count is 1, then table exists
    if c.fetchone()[0] == 1:
        print('Table exists.')
        
        

        c.execute("select * from board")
        
        rows = c.fetchall()
        chessBoard = []
        for row in rows:
            chessBoard.append(row[1])


        #commit the changes to db			
        conn.commit()
    else:
        print("No save game found.")

    #close the connection
    conn.close()

    return(chessBoard)






def checkForUserCommand(inputStringToCheck, chessBoard):
    isGameInProgress = True
    if inputStringToCheck.upper() == "Q":
        outputText("Exirting game.\n\n")
        isGameInProgress = False
    elif inputStringToCheck.upper() == "S":
        saveBoard(chessBoard)
    elif inputStringToCheck.upper() == "L":
        chessBoard = loadBoard(chessBoard)
    else:
        outputText("Sorry, I don't understand " + inputStringToCheck)
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