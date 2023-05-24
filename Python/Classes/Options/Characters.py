from ..Config import Config
import random

class Characters:
    def __init__(self, words, associative, ncharacteres = False):
        self.words = words
        self.associative = associative
        self.ncharacteres = ncharacteres
        self.possibilites = self.run()
    
    def run(self):
        possibilities = []
        for word in self.words:
            ncharacteres = self.ncharacteres if self.ncharacteres else len(word)
            for i in range(random.randint(0, ncharacteres)):
                position = random.randint(0, len(word))
                caractere = random.choice(self.associative)
                word = word[:position] + caractere + word[position:]
            possibilities.append(word)
        return possibilities
    
class CommonCharacteres(Characters):
    def __init__(self, words):
        self.config = Config()
        super().__init__(words, self.config.commonCaracteres)
        
class AllCharacteres(Characters):
    def __init__(self, words):
        self.config = Config()
        super().__init__(words, self.config.allCaracteres)

class NCharacters(Characters):
    def __init__(self, words, limit):
        self.config = Config()
        super().__init__(words, self.config.allCaracteres, limit)



