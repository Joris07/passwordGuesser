from Classes.Config import Config
import unicodedata
import itertools
import random

class Liste_mot:
	def __init__(self, liste_initiale):
		self.liste_initiale = liste_initiale
		self.liste_finale = liste_initiale[:]
		self.config = Config()

	def fct_getListeFinale(self):
		return self.liste_finale

	def fct_addElement(self, mot):
		if mot not in self.liste_finale:
			self.liste_finale.append(mot)
	
	def fct_toCapitalize(self):
		for mot in self.liste_initiale:
			self.fct_addElement(mot.capitalize())

	def fct_toLower(self):
		for mot in self.liste_initiale:
			self.fct_addElement(mot.lower())

	def fct_toUpper(self):
		for mot in self.liste_initiale:
			self.fct_addElement(mot.upper())
	
	def fct_removeAccents(self):
		for mot in self.liste_initiale:
			self.fct_addElement(''.join(c for c in unicodedata.normalize('NFD', mot) if unicodedata.category(c) != 'Mn'))

	def fct_stringToL33t(self):
		possibles = []
		for mot in self.liste_initiale:
			for l in mot:
				ll = self.config.char_map.get(l, l)
				possibles.append((l,) if ll == l else (l, ll))
			for result in [''.join(t) for t in itertools.product(*possibles)]:
				self.fct_addElement(result)

	def fct_addRandomCommonSpecialCharacters(self):
		for mot in self.liste_initiale:
			for result in [''.join('%s%s' % (x, random.choice(self.config.commonCaracteres) if random.random() > 0.5 else '') for x in mot)]:
				self.fct_addElement(result)

	def fct_addAllRandomSpecialCharacters(self):
		for mot in self.liste_initiale:
			for result in [''.join('%s%s' % (x, random.choice(self.config.allCaracteres) if random.random() > 0.5 else '') for x in mot)]:
				self.fct_addElement(result)

	def fct_addAllRandomSpecialCharactersLimitNb(self, limit):
		for mot in self.liste_initiale:
			# calcule le nombre de caractères à ajouter
			num_chars = random.randint(0, limit)
			# ajoute les caractères aléatoires
			for i in range(num_chars):
				index = random.randint(0, len(mot))
				mot = mot[:index] + random.choice(self.config.allCaracteres) + mot[index:]
			self.fct_addElement(mot)