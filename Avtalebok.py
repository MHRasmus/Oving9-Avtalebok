import Avtale_funksjoner as Af

avtale_fil = "Avtalebok.txt"
kategori_fil = "Kategorier.txt"
sted_fil = "Steder.txt"

avtalebok_dict = dict()
kategori_dict = dict()
kategori_liste = list()
sted_dict = dict()
sted_liste = list()

fil_hentet = False

valg = Af.menyvalg()
while valg != 9:
    fil_hentet_status = fil_hentet
    if valg == 1:
        Af.henter_avtalebok(avtalebok_dict,avtale_fil,kategori_dict,kategori_fil,sted_dict,sted_fil)
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
        #avtale_fil = input("Skriv inn navnet på filen som avtalene skal lagres i #NB! husk .txt#: ")
        if fil_hentet_status == False:
            Af.henter_avtalebok(avtalebok_dict, avtale_fil, kategori_dict, kategori_fil, sted_dict, sted_fil)
            fil_hentet = True
        Af.lagrer_dict(avtalebok_dict,avtale_fil,kategori_dict,kategori_fil,sted_dict,sted_fil)
    elif valg == 7:
        Af.ny_kategori(kategori_dict,kategori_liste)
    elif valg == 8:
        Af.ny_sted(sted_dict,sted_liste)

    elif valg == 10:
        Af.lagrer_kategorier(kategori_dict,kategori_fil)
    elif valg == 11:
        Af.print_dictonary(kategori_dict)
    elif valg == 12:
        Af.lagrer_sted(sted_dict,sted_fil)
    elif valg == 13:
        Af.print_dictonary(sted_dict)




    else:
        pass
    valg = Af.menyvalg()
