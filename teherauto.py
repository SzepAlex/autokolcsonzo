from auto import Auto

class Teherauto(Auto):
    def __init__(self, rendszam, berleti_dij):
        super().__init__(rendszam, "Teherautó", berleti_dij)

    def leiras(self):
        return f"Teherautó - Rendszám: {self.rendszam}, Bérleti díj: {self.berleti_dij} Ft"