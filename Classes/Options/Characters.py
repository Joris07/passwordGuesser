from ..Config import Config
import random
from .Words import Words  

class Characters(Words):
    def __init__(self, words, associative, ncharacteres=False):
        self.associative = associative
        self.ncharacteres = ncharacteres
        super().__init__(words)

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

    @property
    def associative(self):
        return self.__associative

    @associative.setter
    def associative(self, associative):
        self.__associative = associative

    @property
    def ncharacteres(self):
        return self.__ncharacteres

    @ncharacteres.setter
    def ncharacteres(self, ncharacteres):
        self.__ncharacteres = ncharacteres

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