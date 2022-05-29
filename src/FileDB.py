from DB import DB
import sqlite3
import unittest

class FileDB(DB):

    def dbConnect(self, filename):
        return sqlite3.connect(filename)