from Config_object import Config

class Liste_mot:
	def __init__(self, liste_initiale):
		self.liste_initiale = liste_initiale
		self.liste_finale = liste_initiale[:]
		self.config = Config()
	
	def toCapitalize(self):
		self.liste_finale.append([x.capitalize() for x in self.liste_finale])
	