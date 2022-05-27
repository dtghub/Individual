import sqlite3
# import sys
# sys.path.append('/home/derek/TSI1/Individual')
import ConsoleInput
import ConsoleOutput

class ChessBoard:

    game_input = ConsoleInput.ConsoleInput()
    game_output = ConsoleOutput.ConsoleOutput()


    def set_game_input(self, game_input):
        self.game_input = game_input

    def set_game_output(self, game_output):
        self.game_output = game_output








    def initGameData(self):
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






    def getColumnLetters(self):
        return("abcdefgh")

    def getRowNumberString(self):
        return("12345678")

    def outputText(self, stringToOutput):
        self.game_output.display(stringToOutput)


    def emphasisedOutputText(self, stringToOutput):
        emphasisedString = "\n***"
        emphasisedString += stringToOutput
        emphasisedString += "***"
        self.outputText(emphasisedString)


    def convertLetterToColumNumber(self, columLetter):
        listOfColumnLetters = self.getColumnLetters()
        columnNumber = listOfColumnLetters.index(columLetter.lower())
        return(columnNumber)



    def assembleChessBoardString(self, boardToDisplay):
        boardOutput = ""
        for rowNumber in range(8, 0, -1):
            boardOutput += str(rowNumber) + " |" + boardToDisplay[rowNumber] + "| " + str(rowNumber) + "\n"
        return(boardOutput)




    def displayBoard(self, boardToDisplay):

        columnLetters = "   " + self.getColumnLetters() + "\n"
        rowSeparator = "   --------\n"

        boardOutput = "\n" + columnLetters + rowSeparator
        boardOutput += self.assembleChessBoardString(boardToDisplay)
        boardOutput += rowSeparator + columnLetters

        self.outputText(boardOutput)







    def evaluatePlayerInput(self, inputFromPlayer):
        isValidInput = False
        columnLetters = self.getColumnLetters()
        rowNumbersString = self.getRowNumberString()
        if len(inputFromPlayer) == 2:
            if (inputFromPlayer[0].lower() in columnLetters) and (inputFromPlayer[1] in rowNumbersString):
                isValidInput = True
        return(isValidInput)




    def getInputFromPlayer(self, textToDisplay):
        playerInput = self.game_input.get_string(textToDisplay)
        isValidInput = self.evaluatePlayerInput(playerInput)
        return(isValidInput, playerInput)




    def getValueAtPositionOnBoard(self, coordinate, boardToCheck):
        columNumber = self.convertLetterToColumNumber(coordinate[0])
        valueAtPosition = boardToCheck[int(coordinate[1])][columNumber]
        return(valueAtPosition)


    def setValueAtPositionOnBoard(self, coordinate, boardToChange, newValue):
        columNumber = self.convertLetterToColumNumber(coordinate[0])

        rowToChange = list(boardToChange[int(coordinate[1])])
        rowToChange[columNumber] = newValue
        changedRow = "".join(rowToChange)

        boardToChange[int(coordinate[1])] = changedRow
        return(boardToChange)



    def identifyIfValueRepresentsEmptySquare(self, valueAtPositionOnBoard):
        if valueAtPositionOnBoard == ".":
            isEmptySquare = True
        else:
            isEmptySquare = False
        return(isEmptySquare)


    def testForEmptySquare(self, inputFromPlayer, chessBoard):
        valueAtPositionOnBoard = self.getValueAtPositionOnBoard(inputFromPlayer, chessBoard)

        isEmptySquare = self.identifyIfValueRepresentsEmptySquare(valueAtPositionOnBoard)
        if isEmptySquare:
            self.emphasisedOutputText("There is no chess piece at " + inputFromPlayer)
            inputFromPlayer = ""
        return(inputFromPlayer)



    def inputSquareToMoveFrom(self, chessBoard):
        promptText = "Please input the coordinates to move from\ne.g. 'e2' (or 'q' to exit): "
        isValidInput, inputFromPlayer = self.getInputFromPlayer(promptText)
        if isValidInput:
            inputFromPlayer = self.testForEmptySquare(inputFromPlayer, chessBoard)
        elif len(inputFromPlayer) != 1:
            self.emphasisedOutputText("Sorry, I don't understand '" + inputFromPlayer+ "'")
            inputFromPlayer = ""
        return(inputFromPlayer)



    def inputSquareToMoveTo(self):
        promptText = "Please input the coordinates to move to: "
        isValidInput, inputFromPlayer = self.getInputFromPlayer(promptText)
        if not(isValidInput) and len(inputFromPlayer) != 1:
            self.emphasisedOutputText("Sorry, I don't understand '" + inputFromPlayer+ "'")
            inputFromPlayer = ""
        return(inputFromPlayer)


    def checkIfBoardTableAlreadyExists(self, databaseCursor):
        databaseCursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='board'")
        isAlreadyExistingTable = databaseCursor.fetchone()[0] == 1
        return isAlreadyExistingTable




    def saveBoard(self, chessBoard):
        databaseConnection = sqlite3.connect('chessBoard.db')
        databaseCursor = databaseConnection.cursor()

        isAlreadyExistingTable = self.checkIfBoardTableAlreadyExists(databaseCursor)
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
        self.emphasisedOutputText("Current position saved.")




    def fetchSavedTableBoard(self, databaseCursor, chessBoard):
            databaseCursor.execute("select * from board")
            rows = databaseCursor.fetchall()
            chessBoard = []
            for row in rows:
                chessBoard.append(row[1])
            return(chessBoard)






    def loadBoard(self, chessBoard):
        databaseConnection = sqlite3.connect('chessBoard.db')
        databaseCursor = databaseConnection.cursor()

        isAlreadyExistingTable = self.checkIfBoardTableAlreadyExists(databaseCursor)
        if isAlreadyExistingTable: 
            chessBoard = self.fetchSavedTableBoard(databaseCursor, chessBoard)
        else:
            self.emphasisedOutputText("No save game found.")

        databaseConnection.close()
        self.emphasisedOutputText("Preiously saved board has been loaded.")
        return(chessBoard)






    def checkForUserCommand(self, inputStringToCheck, chessBoard):
        isGameInProgress = True
        if inputStringToCheck.upper() == "Q":
            self.outputText("Exiting game.\n\n")
            isGameInProgress = False
        elif inputStringToCheck.upper() == "S":
            self.saveBoard(chessBoard)
        elif inputStringToCheck.upper() == "L":
            chessBoard = self.loadBoard(chessBoard)
        else:
            self.emphasisedOutputText("Sorry, I don't understand " + inputStringToCheck)
        return(isGameInProgress, chessBoard)




    def getPlayerMove(self, gameData):
        isGameInProgress = True

        chessBoard = gameData["board"]

        moveFromCoordinate = self.inputSquareToMoveFrom(gameData["board"])
        moveToCoordinate = moveFromCoordinate

        if len(moveFromCoordinate) == 2:
            moveToCoordinate = self.inputSquareToMoveTo()
            if len(moveToCoordinate) == 1:
                isGameInProgress, chessBoard = self.checkForUserCommand(moveToCoordinate, chessBoard)

        if len(moveFromCoordinate) == 1:
            isGameInProgress,  chessBoard = self.checkForUserCommand(moveFromCoordinate, chessBoard)

        gameData["board"] = chessBoard
        return gameData, isGameInProgress, moveFromCoordinate, moveToCoordinate



    def movePiece(self, chessBoard, moveFromCoordinate, moveToCoordinate):
        valueAtPositionOnBoard = self.getValueAtPositionOnBoard(moveFromCoordinate, chessBoard)
        chessBoard = self.setValueAtPositionOnBoard(moveFromCoordinate, chessBoard, ".")
        chessBoard = self.setValueAtPositionOnBoard(moveToCoordinate, chessBoard, valueAtPositionOnBoard)

        return(chessBoard)





    def main(self):
        gameData = self.initGameData()


        isGameInProgress = True
        while isGameInProgress:

            self.displayBoard(gameData["board"])
            gameData, isGameInProgress, moveFromCoordinate, moveToCoordinate = self.getPlayerMove(gameData)
            if len(moveFromCoordinate) == 2 and len(moveToCoordinate) == 2 and isGameInProgress:
                gameData["board"] = self.movePiece(gameData["board"], moveFromCoordinate, moveToCoordinate)







if __name__ == "__main__":
    chessBoard = ChessBoard()
    chessBoard.main()