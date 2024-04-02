#!/usr/bin/env python3

class Book:
    def __init__(self, title="", page_count=None):
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        return self._title
    
    @page_count.setter
    def page_count(self, new_page_count):
        if (not type(new_page_count) is int):
            print("page_count must be an integer")
        else:
            self._title = new_page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
        