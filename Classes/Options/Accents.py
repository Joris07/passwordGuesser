import unicodedata
from .Words import Words

class Accents(Words):
    def __init__(self, words):
        super().__init__(words)
    
    def run(self):
        return [''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn') for s in self.words]

class RemoveAccents(Accents):
    def __init__(self, words):
        super().__init__(words)