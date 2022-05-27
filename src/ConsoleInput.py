from Input import Input
import unittest
class ConsoleInput(Input):

    def get_string(self, message):
        return input(message)