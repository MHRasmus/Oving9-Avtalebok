import Avtale_funksjoner as Af

avtale_fil = "Avtalebok.txt"
kategori_fil = "Kategorier.txt"
sted_fil = "Steder.txt"

avtalebok_dict = dict()
kategori_dict = dict()
sted_dict = dict()

#fil_hentet = False

#Af.henter_avtalebok(avtalebok_dict, avtale_fil)
#Af.henter_kategorier(kategori_dict, kategori_fil)
#Af.henter_sted(sted_dict, sted_fil)

valg = Af.menyvalg()
while valg != 13:
    #fil_hentet_status = fil_hentet
    if valg == 1:
        Af.henter_avtalebok(avtalebok_dict, avtale_fil)
        Af.henter_kategorier(kategori_dict, kategori_fil)
        Af.henter_sted(sted_dict, sted_fil)
        #fil_hentet = True
    elif valg == 2:
        Af.ny_avtale(avtalebok_dict, sted_dict, kategori_dict)
    elif valg == 3:
        Af.print_dictonary(avtalebok_dict, "Avtaler:")
    elif valg == 4:
        Af.print_dictonary(avtalebok_dict, "Avtaler:")
        try:
            print("\nFor å komme ut av denne menyen uten å slette noe, "
                  "Skriv noe som ikke er navnet til noen av avtalene.")
            slett = input("Skriv inn navnet på avtalen du vil slette: ")
            avtalebok_dict.pop(slett)
        except KeyError:
            print("Finner ikke en avtale med det navnet.")
    elif valg == 5:
        Af.print_dictonary(avtalebok_dict, "Avtaler:")
        try:
            rediger = input("\nSkriv inn navnet på avtalen du vil redigere: ")
            print(f"{avtalebok_dict[rediger]}\n")
            Af.rediger_avtale(avtalebok_dict, rediger, sted_dict, kategori_dict)
        except KeyError:
            print("Finner ikke en avtale med det navnet.")
    elif valg == 6:
        Af.print_dictonary(kategori_dict, "Lagrede kategorier:")
        Af.ny_kategori(kategori_dict)
    elif valg == 7:
        Af.print_dictonary(kategori_dict, "Kategorier:")
    elif valg == 8:
        try:
            Af.legg_til_extra_kategori(avtalebok_dict, kategori_dict)
        except ValueError:
            print("Id på kategori må være et heltall")
        #except KeyError:
            #print("Finner ikke en avtale med det navnet.")
    elif valg == 9:
        Af.print_dictonary(sted_dict, "Lagrede steder:")
        Af.ny_sted(sted_dict)
    elif valg == 10:
        Af.print_dictonary(sted_dict, "Steder:")
    elif valg == 11:
        Af.print_dictonary(sted_dict, "Eksisterende steder:")
        id_sted = int(input("Skriv inn id-en på stedet du vil finne tilhørende avtaler til: "))
        søk_liste = Af.søk_etter_sted(avtalebok_dict, id_sted)
        print('\n'.join(map(str, søk_liste)))
    elif valg == 12:
        Af.lagrer_dict(avtalebok_dict, avtale_fil)
        Af.lagrer_dict(kategori_dict, kategori_fil)
        Af.lagrer_dict(sted_dict, sted_fil)
    else:
        pass
    valg = Af.menyvalg()
