from abc import ABC, abstractmethod

# Parent Possibilites
class Possibilites(ABC):
    def __init__(self):
        self._possibilites = self.run() #Attribut d'objet _possibilites
    
    # Classe abstraite (rôle de l'interface)
    @abstractmethod
    def run(self):
        pass
        
    # Getter
    @property
    def possibilites(self):
        return self._possibilites

    # Setter 
    @possibilites.setter
    def possibilites(self, possibilites):
        self._possibilites = possibilites
        
    def printData(self):
        print(self._possibilites)