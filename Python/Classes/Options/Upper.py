from .Words import Words

class Upper(Words):
	def __init__(self, words):
		super().__init__(words)

	def run(self):
		return [word.upper() for word in self.words]
	
class ToUpper(Upper):
	def __init__(self, words):
		super().__init__(words)