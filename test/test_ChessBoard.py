import sys
sys.path.append('/home/derek/TSI1/Individual/src')
from ChessBoard import ChessBoard
import unittest




class TestChessBoard(unittest.TestCase):
    chessBoard = ChessBoard()




    def test_initGameData(self):
        reference_chessBoardList = [
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
        
        gameData = self.chessBoard.initGameData()

        self.assertEquals(len(reference_chessBoardList), len(gameData["board"]))













if __name__ == '__main__':
    unittest.main()