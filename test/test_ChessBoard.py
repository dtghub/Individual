import sys
sys.path.append('/home/derek/TSI1/Individual/src')
from ChessBoard import ChessBoard
import unittest




class TestChessBoard(unittest.TestCase):
    chessBoard = ChessBoard()

    @classmethod
    def setUpClass(cls):
        cls.reference_chessBoardList = [
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

        cls.listOfColumnLetters = "abcdefgh"











    def test_initGameData_ListLength(self):
        testBoard = self.reference_chessBoardList
        gameData = self.chessBoard.initGameData()
        self.assertEquals(len(testBoard), len(gameData["board"]))

    def test_initGameData_firstRow(self):
        first_testBoard_Row = self.reference_chessBoardList[1]
        first_gameData_Row = self.chessBoard.initGameData()["board"][1]
        self.assertEquals(first_testBoard_Row, first_gameData_Row)

    def test_initGameData_middleRow(self):
        middle_testBoard_Row = self.reference_chessBoardList[4]
        middle_gameData_Row = self.chessBoard.initGameData()["board"][4]
        self.assertEquals(middle_testBoard_Row, middle_gameData_Row)




    def test_getColumnLetters(self):
        expectedString = "abcdefgh"
        returnedString = self.chessBoard.getColumnLetters()
        self.assertEquals(expectedString, returnedString)

    def test_getRowNumberString(self):
        expectedString = "12345678"
        returnedString = self.chessBoard.getRowNumberString()
        self.assertEquals(expectedString, returnedString)


    # to be done
    # def test_outputText(self, stringToOutput):



    # to be done
    # def test_emphasisedOutputText(self, stringToOutput):



    def test_convertLetterToColumNumber_a(self):
        expectedPositionValue = 0
        returnedPositionValue = self.chessBoard.convertLetterToColumNumber('a')
        self.assertEquals(expectedPositionValue, returnedPositionValue)

    def test_convertLetterToColumNumber_e(self):
        expectedPositionValue = 4
        returnedPositionValue = self.chessBoard.convertLetterToColumNumber('e')
        self.assertEquals(expectedPositionValue, returnedPositionValue)

    def test_convertLetterToColumNumber_h(self):
        expectedPositionValue = 7
        returnedPositionValue = self.chessBoard.convertLetterToColumNumber('h')
        self.assertEquals(expectedPositionValue, returnedPositionValue)

















if __name__ == '__main__':
    unittest.main()