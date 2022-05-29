from DB import DB
import sqlite3

class TestMemoryDB(DB):

    def dbConnect(self,filename):
        return sqlite3.connect(':memory:')
        



