import pytest 

class LeafElement:
    def __init__(self, *args):
        self.position = args[0]

    def show_details(self):
        pass


class CompositeElement:
    def __init__(self, *args):
        self.position = args[0]
        self.children = []

    def add(self, child):
        pass 


    def remove(self, child):
        pass

    def show_details(self):
        pass
