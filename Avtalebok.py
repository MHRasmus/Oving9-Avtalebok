
import Avtale_funksjoner as Af

fil = "Avtalebok.txt"
avtalebok_dict = dict()
fil_hentet = False

valg = Af.menyvalg()
while valg != 9:
    fil_hentet_status = fil_hentet
    if valg == 1:
        #fil = input("Skriv inn navnet på filen som du vil lese inn avtaler fra: ")
        Af.henter_avtalebok(avtalebok_dict, fil)
        fil_hentet = True
    elif valg == 2:
        Af.ny_avtale(avtalebok_dict)
    elif valg == 3:
        Af.print_avtale(avtalebok_dict)
    elif valg == 4:
        Af.print_avtale(avtalebok_dict)
        try:
            print("\nFor å komme ut av denne menyen uten å slette noe, "
                  "Skriv noe som ikke er navnet til noen av avtalene.")
            slett = input("Skriv inn navnet på avtalen du vil slette: ")
            avtalebok_dict.pop(slett)
        except KeyError:
            print("Finner ikke en avtale med det navnet.")
    elif valg == 5:
        Af.print_avtale(avtalebok_dict)
        try:
            rediger = input("\nSkriv inn navnet på avtalen du vil redigere: ")
            print(f"{avtalebok_dict[rediger]}\n")
            Af.rediger_avtale(avtalebok_dict, rediger)
        except KeyError:
            print("Finner ikke en avtale med det navnet.")
    elif valg == 6:
        #fil = input("Skriv inn navnet på filen som avtalene skal lagres i #NB! husk .txt#: ")
        if fil_hentet_status == False:
            Af.henter_avtalebok(avtalebok_dict, fil)
            fil_hentet = True
        Af.lagrer_dict(avtalebok_dict, fil)
    else:
        pass
    valg = Af.menyvalg()
