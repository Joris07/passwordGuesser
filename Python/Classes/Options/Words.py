from .Possibilites import Possibilites

class Words(Possibilites):
	def __init__(self, words):
		self.words = words
		super().__init__()
  
	@property
	def words(self):
		return self.__words

	@words.setter
	def words(self, words):
		self.__words = words