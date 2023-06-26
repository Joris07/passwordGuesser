from Config_object import Config

class Liste:
	def __init__(self, liste_initiale):
		self.liste_initiale = liste_initiale
		self.liste_finale = liste_initiale[:]
		self.config = Config()

	@property
	def liste_initale(self):
		return self._liste_initiale

	@liste_initiale.setter
	def liste_initiale(self, liste):
		self._liste_initiale = liste

	@property
	def liste_finale(self):
		return self._liste_finale

	@liste_finale.setter
	def liste_finale(self, liste):
		self._liste_finale = liste

	def fct_addElement(self, valeur):
		if valeur not in self.liste_finale:
			self.liste_finale.append(valeur)