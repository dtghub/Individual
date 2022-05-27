from Output import Output

class TestOutput(Output):

    list_of_test_outputs = []

    #allows e.g. list to be reset to []
    def reset_list_of_test_outputs(self):
        self.list_of_test_outputs = []

    def get_list_of_test_outputs(self):
        return self.list_of_test_outputs

    def display(self, *message):
        self.list_of_test_outputs.append([*message])