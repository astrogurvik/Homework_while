from classes.Methods import Methods


class Stroka(Methods):

    def __init__(self, some_string):
        super().__init__()
        self.some_string = some_string

    def length(self):
        return len(self.some_string)

    def include(self, sub_string):
        if sub_string in self.some_string:
            response = True
        else:
            response = False
        return response

    def replacing(self, old, new):
        new_string = self.some_string.replace(old, new)
        return new_string

