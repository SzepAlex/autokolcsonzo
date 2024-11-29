from autokolcsonzo import Autokolcsonzo

def main():
    kolcsonzo = Autokolcsonzo("Autókölcsönző")

    while True:
        print("\n1. Autó bérlése")
        print("2. Bérlés lemondása")
        print("3. Bérlések listázása")
        print("4. Kilépés")
        valasztas = input("Kérlek válaszd ki a művelet számát: ")

        if valasztas == '1':
            rendszam = input("Kérlek add meg az autó rendszámát: ")
            nap = int(input("Hány napra szeretnéd bérelni az autót? "))
            ar = kolcsonzo.auto_berles(rendszam, nap)
            if ar is not None:
                print(f"A bérleti díj: {ar} Ft")
            else:
                print("Az autó nem elérhető vagy nem létezik.")

        elif valasztas == '2':
            rendszam = input("Kérlek add meg a lemondani kívánt autó rendszámát: ")
            sikeres = kolcsonzo.berles_lemondas(rendszam)
            if sikeres:
                print("Sikeresen lemondtad a bérlést.")
            else:
                print("Ez a bérlés nem létezik.")

        elif valasztas == '3':
            print("Jelenlegi bérlések:")
            for b in kolcsonzo.berlesek_listazasa():
                print(b)

        elif valasztas == '4':
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás. Kérlek, próbáld újra.")

if __name__ == "__main__":
    main()