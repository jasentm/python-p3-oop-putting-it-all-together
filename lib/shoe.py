#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand="", size=None, condition=""):
        self.brand = brand
        self.size = size
        self.condition = condition
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, new_size):
        if (not type(new_size) is int):
            print("size must be an integer")
        else:
            self._size = new_size

    def cobble(self):
        self.condition = 'New'
        print("Your shoe is as good as new!")
    