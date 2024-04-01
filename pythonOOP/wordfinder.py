"""Word Finder: finds random words from a dictionary."""

from random import randint

class WordFinder:
    """Machine that finds a random word from a dictionary"""
    
    def __init__(self, path):
        """Opens file and returns number of words in file"""
        words = open(path)
        
        self.ls = []
        for word in words:
            self.ls.append(word[:-1])
        
        words.close()
        
        print(f'{len(self.ls)} words read')
    
    def random(self):
        """returns random word from file"""
        return self.ls[randint(0, len(self.ls) - 1)]
    
class SpecialWordFinder(WordFinder):
    """Handles files that have comments and spaces in addition to words"""
    
    def __init__(self, path):
        """Handles special file with comments and spaces"""
        super().__init__(path)
        self.specialList = []
        
        for word in self.ls:
            if word != '' and word[0] != '#':
                self.specialList.append(word)
    
    def random(self):
        return self.specialList[randint(0, len(self.specialList) - 1)]
                    
                   