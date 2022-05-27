import sys
sys.path.append('../src')
sys.path.append('/home/derek/TSI1/Individual/src')

import ChessBoard
import unittest
import TestInput
import TestOutput




class TestChessBoard(unittest.TestCase):
    chessBoard = ChessBoard.ChessBoard()
    test_input = TestInput.TestInput()
    test_output = TestOutput.TestOutput()

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

        cls.chessBoard.set_game_output(cls.test_output)
        cls.chessBoard.set_game_input(cls.test_input)
        cls.listOfColumnLetters = "abcdefgh"



    def setUp(self):
        self.test_output.reset_list_of_test_outputs()









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






    def test_outputText(self):
        self.chessBoard.outputText("Testing text output")
        outputText = self.test_output.get_list_of_test_outputs()
        self.assertEquals(outputText[0], ["Testing text output"])



    def test_emphasisedOutputText(self):
        self.chessBoard.emphasisedOutputText("Test output emphasised")
        outputText = self.test_output.get_list_of_test_outputs()
        self.assertEquals(outputText[0], ["\n***Test output emphasised***"])





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









    def test_getInputFromPlayer_e1(self):
        player_enters = "e2"
        self.test_input.set_list_of_test_inputs([player_enters])
        isValidInput, playerInput = self.chessBoard.getInputFromPlayer("Howdy")
        self.assertTrue(isValidInput)
        self.assertEquals(playerInput, player_enters)


    def test_getInputFromPlayer_m2(self):
        player_enters = "m2"
        self.test_input.set_list_of_test_inputs([player_enters])
        isValidInput, playerInput = self.chessBoard.getInputFromPlayer("Howdy")
        self.assertFalse(isValidInput)
        self.assertEquals(playerInput, player_enters)







if __name__ == '__main__':
    unittest.main()