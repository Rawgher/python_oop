"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Class for finding random words from provided dictionary.
    
    >>> wf = WordFinder("./test.txt")
    3 words read

    >>> wf.random() in ["mackerel", "salmon", "trout"]
    True
    """

    def __init__(self, path='./words.txt'):
        """ Open the file provided and then parse through the words in the list"""
        with open(path, 'r') as word_file:
            self.words = self.parse(word_file)
        
        """ This prints the amount of words that were pulled from the list"""
        print(f'{len(self.words)} words read')

    def parse(self, word_file):
        """ Parse the file to grab the list of words """
        return [word.strip() for word in word_file]
    
    def random(self):
        """ Return the randomly selected word """
        return random.choice(self.words)
    

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that ignores comments and blank lines.

    This subclass filters out lines starting with '#' and blank lines.

    >>> swf = SpecialWordFinder("./special_words.txt")
    4 words read

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True
    """
    
    def parse(self, word_file):
        """Parse the file into a list of words, ignoring comments and blank lines."""
        return [word.strip() for word in word_file if word.strip() and not word.startswith('#')]
