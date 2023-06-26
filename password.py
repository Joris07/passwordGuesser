import json
import itertools
import unicodedata
import random

def jsonToList(json):
	list = []
	for word in json["words"]:
		list.append(word)
	for date in json["dates"]:
		list.append(date)
	return list

def toCapitalize(items):
	return [x.capitalize() for x in items]

def toLower(items):
	return [x.lower() for x in items]

def toUpper(items):
	return [x.upper() for x in items]

#Tout en l33t
def stringToL33t(message):
    char_map = {
        "a": "4",
        "b": "8",
        "e": "3",
        "g": "6",
        "i": "1",
        "l": "1",
        "o": "0",
        "s": "5",
        "t": "7",
        "z": "2",
    }
    leetspeak = ""
    for char in message:
        if char.lower() in char_map:
            possible_replacements = char_map[char.lower()]
            leet_replacement = possible_replacements
            leetspeak += leet_replacement
        else:
            leetspeak += char
    return leetspeak

def removeAccents(items):
	return [''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn') for s in items]

def findCombination(items):
	my_list = list()
	for L in range(0, len(items)+1):
		for subset in itertools.permutations(items, L):
			my_list.append("".join(str(x) for x in subset))
	return my_list

#YYYY-MM-DD
def returnYear(date):
	return date.split("-")[0]

def returnMonth(date):
	return date.split("-")[1]

def returnDay(date):
	return date.split("-")[2]
	
def returnYearIn2Digits(year):
	return year[-2]+year[-2]

def separateDateNumbers(date):
	return [x for x in date.split("-")]

def addRandomCommonSpecialCharacters(word):
	symbols = [".", "$", "?", "!", "*"]
	return ''.join('%s%s' % (x, random.choice(symbols) if random.random() > 0.5 else '') for x in word)

def addAllRandomSpecialCharacters(word):
	symbols = [" ", "!", '”', "#", "$", "%", "&", "’", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "`", "_", "{", "|", "}", "~"]
	return ''.join('%s%s' % (x, random.choice(symbols) if random.random() > 0.5 else '') for x in word)

def addAllRandomSpecialCharactersLimitNb(word, limit):
	symbols = [" ", "!", '”', "#", "$", "%", "&", "’", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "`", "_", "{", "|", "}", "~"]
	# Vérifier que le nombre de caractères à remplacer est inférieur ou égal à la longueur de la chaîne d'entrée
	if limit > len(word):
		raise ValueError("Le nombre de caractères à remplacer doit être inférieur ou égal à la longueur de la chaîne d'entrée.")

	input_list = list(word)
	replace_indexes = random.sample(range(len(input_list)), limit)
	for index in replace_indexes:
		input_list[index] = random.choice(symbols)

	return ''.join(input_list)

def returnMonthInLetters(monthNumber):
	months_map = {
		"01" : "janvier",
		"02" : "fevrier",
		"03" : "mars",
		"04" : "avril",
		"05" : "mai",
		"06" : "juin",
		"07" : "juillet",
		"08" : "aout",
		"09" : "septembre",
		"10" : "octobre",
		"11" : "novembre",
		"12" : "decembre"
	}
	return months_map[monthNumber] if monthNumber in months_map else ""

#Toutes les combinaisons de l33t
def Leet2Combos(mot):
	possibles = []
	char_map = {"a": "4","b": "8","e": "3","g": "6","i": "1","l": "1","o": "0","s": "5","t": "7","z": "2"}
	for l in mot.lower():
		ll = char_map.get(l, l)
		possibles.append((l,) if ll == l else (l, ll))
	return [''.join(t) for t in itertools.product(*possibles)]
 
# Driver Code
if __name__ == '__main__':
	items = '''{"words": ["DoèO", "jOrés", "GàuRDon"], "dates": ["07/01/2001", "2022/05/25"]}'''
	items = json.loads(items)
	items = jsonToList(items)
	#print(addAllRandomSpecialCharacters("2022"))
	#print(findCombination(items))
	char_map = {"a": "4","b": "8","e": "3","g": "6","i": "1","l": "1","o": "0","s": "5","t": "7","z": "2"}
	print(addAllRandomSpecialCharactersLimitNb("hello", 4))