from Output import Output
import unittest
class ConsoleOutput(Output):
    def display(self, *message):
        return print(*message)