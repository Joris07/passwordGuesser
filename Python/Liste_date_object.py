from Config_object import Config

class Liste_date:
	def __init__(self, liste_initiale):
		self.liste_initiale = liste_initiale
		self.liste_finale = liste_initiale[:]
		self.config = Config()

	def getListeInitiale(self):
		return self.liste_initiale
	
	def getListeFinale(self):
		return self.liste_finale
	
	def extractDaysOrMonthsOrYears(self, index): # 0 -> Année | 1 -> Mois | 2 -> Jour
		for date_1 in self.liste_initiale:
			self.liste_finale.append(date_1.split("-")[index])

	def extractYearIn2Digits(self):
		for date in self.liste_initiale:
			self.liste_finale.append(date.split("-")[0][-2]+date.split("-")[0][-1])
	
	def separateDateNumbers(self):
		for date in self.liste_initiale:
			self.liste_finale += date.split("-")

	def returnMonthInLetters(self):
		for date in self.liste_initiale:
			monthNumber = date.split("-")[1]
			if monthNumber in self.config.months_map:
				self.liste_finale.append(self.config.months_map[monthNumber])
    
