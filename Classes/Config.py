class Config:
	default_language = "FR" # Attribut Statique

	def __init__(self):
		self.char_map_maj = {
			"A": "4",
			"B": "8",
			"E": "3",
			"G": "6",
			"I": "1",
			"L": "1",
			"O": "0",
			"S": "5",
			"T": "7",
			"Z": "2"
		}

		self.char_map_min = {
			"a": "4",
			"b": "8",
			"e": "3",
			"g": "6",
			"i": "1",
			"l": "1",
			"o": "0",
			"s": "5",
			"t": "7",
			"z": "2"
		}

		self.char_map_all = {
			"A": "4",
			"B": "8",
			"E": "3",
			"G": "6",
			"I": "1",
			"L": "1",
			"O": "0",
			"S": "5",
			"T": "7",
			"Z": "2",
			"a": "4",
			"b": "8",
			"e": "3",
			"g": "6",
			"i": "1",
			"l": "1",
			"o": "0",
			"s": "5",
			"t": "7",
			"z": "2"
		}

		self.commonCaracteres = [
			".",
			"$", 
			"?", 
			"!", 
			"*"
		]

		self.allCaracteres = [
			" ", 
			"!", 
			'”', 
			"#", 
			"$", 
			"%", 
			"&", 
			"’", 
			"(", 
			")", 
			"*", 
			"+", 
			",", 
			"-", 
			".", 
			"/", 
			":", 
			";", 
			";", 
			"<", 
			"=", 
			">", 
			"?", 
			"@", 
			"[",
			"\\", 
			"]", 
			"^", 
			"`", 
			"_", 
			"{", 
			"|", 
			"}", 
			"~"
		]

	@staticmethod # Méthode statique
	def get_default_language():
		return Config.default_language
 	
	@property
	def char_map_maj(self):
		return self.__char_map_maj

	@char_map_maj.setter
	def char_map_maj(self, char_map_maj):
		self.__char_map_maj = char_map_maj

	@property
	def char_map_min(self):
		return self.__char_map_min

	@char_map_min.setter
	def char_map_min(self, char_map_min):
		self.__char_map_min = char_map_min

	@property
	def char_map_all(self):
		return self.__char_map_all

	@char_map_all.setter
	def char_map_all(self, char_map_all):
		self.__char_map_all = char_map_all

	@property
	def commonCaracteres(self):
		return self.__commonCaracteres

	@commonCaracteres.setter
	def commonCaracteres(self, commonCaracteres):
		self.__commonCaracteres = commonCaracteres

	@property
	def allCaracteres(self):
		return self.__allCaracteres
	
	@allCaracteres.setter
	def allCaracteres(self, allCaracteres):
		self.__allCaracteres = allCaracteres