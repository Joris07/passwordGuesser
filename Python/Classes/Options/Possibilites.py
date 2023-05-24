class Possibilites:
	def __init__(self):
		self.possibilites = self.run()
  
	def run(self):
		pass
  
	@property
	def possibilites(self):
		return self.__possibilites

	@possibilites.setter
	def possibilites(self, possibilites):
		self.__possibilites = possibilites