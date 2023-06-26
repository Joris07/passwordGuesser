from .Possibilites import Possibilites

class Words(Possibilites):
	def __init__(self, words):
		self.words = words
		super().__init__()
  
	@property
	def words(self):
		return self._words

	@words.setter
	def words(self, words):
		self._words = words