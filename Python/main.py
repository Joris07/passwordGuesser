from Liste_date_object import Liste_date
from Liste_mot_object import Liste_mot

items = ["2022-01-07", "2022-04-10", "2021-10-25"]
liste_date = Liste_date(items)
#liste_date.extractDaysOrMonthsOrYears(0)
#liste_date.separateDateNumbers()
#liste_date.extractYearIn2Digits()
liste_date.returnMonthInLetters()
print(liste_date.getListeFinale())
