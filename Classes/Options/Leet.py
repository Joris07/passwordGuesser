from ..Config import Config
from .Words import Words
import itertools

class Leet(Words):
	def __init__(self, words, associative):
		self.associative = associative
		super().__init__(words)

	def run(self):
		# Traitement en fonction des params
		possibilities = []
		for mot in self.words:
			possibles = []
			for l in mot:
				ll = self.associative.get(l, l)
				possibles.append((l,) if ll == l else (l, ll))
			for result in [''.join(t) for t in itertools.product(*possibles)]:
				possibilities.append(result)
		return possibilities

	@property
	def associative(self):
		return self.__associative

	@associative.setter
	def associative(self, associative):
		self.__associative = associative
	
class LeetMin(Leet):
	def __init__(self, words):
		self.config = Config()
		super().__init__(words, self.config.char_map_min)
		
class LeetMaj(Leet):
	def __init__(self, words):
		self.config = Config()
		super().__init__(words, self.config.char_map_maj)

class LeetAll(Leet):
	def __init__(self, words):
		self.config = Config()
		super().__init__(words, self.config.char_map_all)