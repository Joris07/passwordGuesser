from .Possibilites import Possibilites

class Date(Possibilites):
    def __init__(self, dates):
        self.__dates = dates # Attribut privé __dates
        super().__init__()

    @property
    def dates(self):
        return self.__dates

    @dates.setter
    def dates(self, new_dates):
        self.__dates = new_dates