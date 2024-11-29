from szemelyauto import Szemelyauto  # Importáld a Szemelyauto osztályt
from teherauto import Teherauto       # Importáld a Teherauto osztályt
from berles import Berles              # Importáld a Berles osztályt

class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = [
            Szemelyauto("GER-888", 10000),
            Teherauto("TOR-999", 12000),
            Szemelyauto("LIV-111", 15000)
        ]
        self.berlesek = []

    def auto_berles(self, autonev, nap):
        auto = next((a for a in self.autok if a.rendszam == autonev and a.elerheto), None)
        if auto:
            berles = Berles(auto, nap)
            self.berlesek.append(berles)
            auto.elerheto = False
            return berles.berlet_arat()
        else:
            return None

    def berles_lemondas(self, autonev):
        berles = next((b for b in self.berlesek if b.auto.rendszam == autonev), None)
        if berles:
            self.berlesek.remove(berles)
            berles.auto.elerheto = True
            return True
        return False

    def berlesek_listazasa(self):
        return [berles.auto.leiras() for berles in self.berlesek]