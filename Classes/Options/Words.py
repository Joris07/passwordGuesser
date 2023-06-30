from .Possibilites import Possibilites

# Words hérite de Possibilites
class Words(Possibilites):
    def __init__(self, words):
        self._words = words # _words attribut protegé
        super().__init__()
  
    @property
    def words(self):
        return self._words

    @words.setter
    def words(self, new_words):
        self._words = new_words