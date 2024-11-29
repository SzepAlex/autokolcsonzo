from auto import Auto

class Szemelyauto(Auto):
    def __init__(self, rendszam, berleti_dij):
        super().__init__(rendszam, "Személyautó", berleti_dij)

    def leiras(self):
        return f"Személyautó - Rendszám: {self.rendszam}, Bérleti díj: {self.berleti_dij} Ft"