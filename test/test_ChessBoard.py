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













if __name__ == '__main__':
    unittest.main()