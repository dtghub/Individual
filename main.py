

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



def displayBoard(gameData):

    columnLetters = "   abcdefgh\n"
    rowSeparator = "   --------\n"
    boardOutput = columnLetters + rowSeparator


    for rowNumber in range(0,8):
        boardOutput += str(rowNumber) + " |" + gameData["board"][rowNumber] + "\n"

    boardOutput += rowSeparator + columnLetters

    print(boardOutput)








def main():
    gameData = initGameData()
    displayBoard(gameData)


main()