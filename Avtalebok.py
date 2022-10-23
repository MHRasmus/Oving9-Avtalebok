
import Avtale_funksjoner as Af

avtalebok_dict = dict()

valg = Af.menyvalg()
while valg != 9:
    if valg == 1:
        fil = input("Skriv inn navnet på filen som skall leses inn: ")
        Af.henter_avtalebok(avtalebok_dict, fil)
    elif valg == 2:
        fil = input("Skriv inn navnet på filen som avtalene skall skrives til: ")
        Af.lagrer_dict(avtalebok_dict, fil)
    elif valg == 3:
        Af.ny_avtale(avtalebok_dict)
    elif valg == 4:
        Af.print_avtale(avtalebok_dict)
    elif valg == 5:
        Af.print_avtale(avtalebok_dict)
        try:
            print("\nFor å komme ut av denne menyen uten å slette noe. "
                  "Skriv noe som ikke er navnet til noen av avtalene.")
            slett = input("Skriv inn navnet på avtalen du vill slette: ")
            avtalebok_dict.pop(slett)
        except KeyError:
            print("Finner ikke en avtale med det navnet.")
    elif valg == 6:
        Af.print_avtale(avtalebok_dict)
        try:
            rediger = input("\nSkriv inn navnet på avtalen du vill redigere: ")
            print(f"{avtalebok_dict[rediger]}\n")
            Af.rediger_avtale(avtalebok_dict, rediger)
        except KeyError:
            print("Finner ikke en avtale med det navnet.")
    else:
        pass
    valg = Af.menyvalg()
