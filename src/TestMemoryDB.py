from DB import DB
import sqlite3

class TestMemoryDB(DB):

    def dbConnect(self,filename):
        return sqlite3.connect(':memory:')

    def readBoardFromDB(self, databaseConnection):
        databaseCursor = databaseConnection.cursor()
        databaseCursor.execute("select * from board")
        rows = databaseCursor.fetchall()
        chessBoard = []
        for row in rows:
            chessBoard.append(row[1])
        return(chessBoard)

        



