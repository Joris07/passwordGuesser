import unicodedata

class Accents:
    def __init__(self, words):
        self.words = words
        self.possibilites = self.run()
    
    def run(self):
        return [''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn') for s in self.words]
    
class RemoveAccents(Accents):
    def __init__(self, words):
        super().__init__(words)