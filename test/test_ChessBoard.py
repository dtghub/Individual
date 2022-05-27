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











    def test_initGameData_ListLength(self):
        testBoard = self.reference_chessBoardList
        gameData = self.chessBoard.initGameData()
        self.assertEquals(len(testBoard), len(gameData["board"]))

    def test_initGameData_firstRow(self):
        first_testBoard_Row = self.reference_chessBoardList[1]
        first_gameData_Row = self.chessBoard.initGameData()["board"][1]
        self.assertEquals(first_testBoard_Row, first_gameData_Row)

    def test_initGameData_middleRow(self):
        first_testBoard_Row = self.reference_chessBoardList[4]
        first_gameData_Row = self.chessBoard.initGameData()["board"][4]
        self.assertEquals(first_testBoard_Row, first_gameData_Row)









if __name__ == '__main__':
    unittest.main()