from Liste_date_object import Liste_date
from Liste_mot_object import Liste_mot
from Classes.Engine import Engine

options = {
    "leet_min": False,
    "leet_maj": False,
    "leet_all": False,
    "to_capitalize": True,
    "to_upper": True,
    "to_lower": True,
    "remove_accents": True,
    "common_characteres": True,
    "all_characteres": True,
    "n_characteres": True,
    "get_day_number": False,
    "get_month_number": False,
    "get_year_number": False,
    "get_day_text": False,
    "get_month_text": False,
    "get_year_number_two_digits": False
}

words = [
    "alexandre"
]

langs = [
    "FR"
]

dates = [
    "2022-02-09",
    "2023-08-21",
    "2022-06-10"
]

engine = Engine(words, dates, options, langs)
#print(engine.dates)
print(engine.listeFinal)
print(len(engine.listeFinal))