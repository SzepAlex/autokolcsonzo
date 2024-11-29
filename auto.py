from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, rendszam, auto_tipus, berleti_dij):
        self.rendszam = rendszam
        self.auto_tipus = auto_tipus
        self.berleti_dij = berleti_dij
        self.elerheto = True

    @abstractmethod
    def leiras(self):
        pass