from asyncio.windows_events import NULL
import string
import random

class GLC:
    def __init__(self) -> None:
        self.notEnds = []
        self.ends = []
        self.start = NULL
        self.products = {}
    
    def appendNotEnds(self, newNotEnd) -> list:
        '''Append a not end symbol'''
        self.notEnds.append(newNotEnd)
        return self.notEnds

    def appendEnds(self, newEnd) -> None:
        '''Append an end symbol'''
        self.ends.append(newEnd)
        return 

    def setStart(self, newStart) -> None:
        '''Set the start symbol'''
        self.start = newStart
        return

    def appendProducts(self, key, value) -> None:
        '''Append an key value at product dictionary'''
        self.products[key] = value
        return

    def createWordWithNSymbols(self, n) -> str:
        word = random.choices(population=string.ascii_lowercase, weights=None, cum_weights=None, k=n)
        word = "".join(word)
        return word

    def show(self) -> None:
        '''Show the grammar created'''
        pass
