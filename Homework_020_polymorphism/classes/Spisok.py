from classes.Methods import Methods


class Spisok(Methods):

    def __init__(self, some_list):
        super().__init__()
        self.some_list = some_list

    def length(self):
        return len(self.some_list)

    def include(self, sub_string):
        if sub_string in self.some_list:
            response = True
        else:
            response = False
        return response

    def adding(self, new_item):
        new_list = self.some_list.append(new_item)
        return new_list