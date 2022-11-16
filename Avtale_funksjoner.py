from Avtale_klasse import *
from datetime import datetime


# Funksjon for å lage inholdet i avtalen
def lage_avtale(avtale_dict, valgt_tittel, sted_dict, kategori_dict):
    # Lar brukeren legge til eksisterende eller nytt sted
    print_dictonary(sted_dict, "Eksisterende steder:")
    while True:
        try:
            innskrevet_sted = int(input("Skriv inn id til ønsket sted eller legg til nytt sted ved å skrive et "
                                        "annet tall: "))
            if innskrevet_sted in sted_dict:
                valgt_sted = sted_dict[innskrevet_sted]
                break
            else:
                valgt_sted = ny_sted(sted_dict)
                break
        except ValueError:
            print("Id må være heltall")
            continue

    # Sjekker om brukervalgt tidspunkt er i gyldig format (ÅÅÅÅ-MM-DD TT:MM)
    while True:
        try:
            valgt_starttidspunkt = datetime.strptime(input("Skriv inn starttidspunkt(DD-MM-ÅÅÅÅ TT:MM): "),
                                                     "%d-%m-%Y %H:%M")
            break
        except ValueError:
            print("***Feil format på tidspunkt***")
            continue

    # Sjekker om brukervalgt varighet er i gyldig format (int)
    while True:
        try:
            valgt_varighet = 60  # int(input("Skriv inn varighet i hele minutter: "))
            break
        except ValueError:
            print("Feil format på varighet, skriv i hele minutter")
            continue

    # Lar brukeren legge til eksisterende eller ny kategori
    intern_liste = list()

    print_dictonary(kategori_dict, "Eksisterende kategorier")
    while True:
        try:
            innskrevet_kategori = int(input("Skriv inn Id på kategorien du vil legge til: "))
            if innskrevet_kategori in kategori_dict:
                intern_liste.append(kategori_dict[innskrevet_kategori])
            else:
                intern_liste.append(ny_kategori(kategori_dict))

            legg_til_ny = input("Vil du legge til en kategori til? [Y/N]: ")
            if legg_til_ny in ["Y", "y"]:
                continue
            else:
                valgt_kategori = intern_liste
                break

        except ValueError:
            print("Id på kategori må være et heltall")

    # Lager dictionary med valgte data
    avtale_dict[valgt_tittel] = Avtalebok(valgt_tittel, valgt_sted, valgt_starttidspunkt,
                                          valgt_varighet, valgt_kategori)


# Funksjon som lager en ny avtaler
def ny_avtale(avtale_dict, sted_dict, kategori_dict):
    # Bruker skriver inn avtaledeljer
    valgt_tittel = input("Skriv inn tittel: ")

    # Lager inholdet i avtalen
    lage_avtale(avtale_dict, valgt_tittel, sted_dict, kategori_dict)

    # Printer ut avtalen som er blitt opprettet
    print(f"""{"-"*70}\nAvtalen din har blitt opprettet:{avtale_dict[valgt_tittel]}\n{"-"*70}""")


# Funksjon for redigering av eksisterende avtaler
def rediger_avtale(avtale_dict, valgt_tittel, sted_dict, kategori_dict):
    # Lager inholdet i avtalen
    lage_avtale(avtale_dict, valgt_tittel, sted_dict, kategori_dict)

    # Printer ut avtalen som er blitt redigert
    print(f"""{"-" * 70}\nAvtalen din har blitt redigert:{avtale_dict[valgt_tittel]}\n{"-" * 70}""")

# Funksjon som leser inn en ny kategori fra bruker
def ny_kategori(kategori_dict):
    # Id
    while True:
        try:
            valgt_id = int(input("Skriv inn id: "))
            break
        except ValueError:
            print("Id må være et gyldig tall")
            continue

    # Navn
    valgt_navn = input("Skriv inn navn: ")

    # Adresse
    while True:
        prioritet_list = ["Vanlig", "Viktig", "Svært viktig"]
        try:
            print(f"\nPrioritets valg: \n1 = Vanlig \n2 = Viktig \n3 = Svært viktig")
            valgt_prioritet = int(input("Skriv inn tallet som stemmer overens med ønsket prioritet: "))
            prioritet = prioritet_list[valgt_prioritet-1]
            break
        except ValueError:
            print("Prioritet må være et gyldig tall")
            continue

    # Lager dictionary med valgte data
    kategori_dict[valgt_id] = Kategori(valgt_id, valgt_navn, prioritet)

    # Printer ut kategorien som er blitt opprettet
    print(f"Kategorien som har blitt opprettet:{kategori_dict[valgt_id]}")
    return kategori_dict[valgt_id]


# Funksjon som leser inn nytt sted fra bruker
def ny_sted(sted_dict):
    # Id
    while True:
        try:
            valgt_id = int(input("Skriv inn id: "))
            break
        except ValueError:
            print("Id må være et gyldig tall")
            continue

    # Navn
    valgt_navn = input("Skriv inn navn: ")

    # Adresse
    valgt_gateadresse = input("Skriv inn gateadresse: ")
    while True:
        try:
            valgt_postnummer = int(input("Skriv inn postnummer: "))
            break
        except ValueError:
            print("Postnummer må være et gyldig tall")
            continue

    valgt_poststed = input("Skriv inn poststed: ")
    valgt_adresse = f"{valgt_gateadresse}, {valgt_postnummer} {valgt_poststed}"

    # Lager dictionary med valgte data for sted
    sted_dict[valgt_id] = Sted(valgt_id, valgt_navn, valgt_adresse)

    # Printer ut stedet som er blitt opprettet
    print(f"Stedet som har blitt opprettet:{sted_dict[valgt_id]}")
    return sted_dict[valgt_id]


# Funksjon som lagrer dictionary som en tekstfil
def lagrer_dict(navn_dictionary, fil):
    try:
        with open(fil, "w", encoding="UTF8") as fila:
            for nokkel in navn_dictionary:
                fila.write(f"{repr(navn_dictionary[nokkel])}\n")
    except:
        print("Feil har oppstått")


# Funksjon som lager en dictonary fra en tekstfil med avtaler
def henter_avtalebok(navn_dictionary, fil):
    # Leser inn avtaler fra avtale_fil og lager dictionary
    try:
        with open(fil, "r", encoding="UTF8") as fila:
            for linje in fila:
                linje_liste = linje.strip().split(";")
                tittel = linje_liste[0]

                sted_liste = linje_liste[1].strip().split(":")
                id_sted = int(sted_liste[0])
                sted = Sted(id_sted, sted_liste[1], sted_liste[2])

                starttidspunkt = datetime.fromisoformat(linje_liste[2])
                varighet = int(linje_liste[3])

                kategorier_liste = list()
                for kategorier in linje_liste[4].strip("[]: ").split(":"):
                    kategori_liste = kategorier.strip(" , ").split(",")
                    id_kategori = int(kategori_liste[0])
                    kategorier_liste.append(Kategori(id_kategori, kategori_liste[1], kategori_liste[2]))

                navn_dictionary[tittel] = Avtalebok(tittel, sted, starttidspunkt, varighet, kategorier_liste)
            
    except ZeroDivisionError:
        print("Fila: dokumentet er tom")
    except FileNotFoundError:
        print("Fant ikke dokumentet")


# Funksjon som lager en dictonary fra en tekstfil med kategorier
def henter_kategorier(navn_dictionary, fil):
    try:
        with open(fil, "r", encoding="UTF8") as fila:
            for linje in fila:
                linje_liste = linje.strip(" :\n").split(",")
                id = int(linje_liste[0])
                navn_dictionary[id] = Kategori(id, linje_liste[1], linje_liste[2])
        return navn_dictionary
    except ZeroDivisionError:
        print("Fila: dokumentet er tom")
    except FileNotFoundError:
        print("Fant ikke dokumentet")
    except:
        print("Feil har oppstått")


# Funksjon som lager en dictonary fra en tekstfil med steder
def henter_sted(navn_dictionary, fil):
    try:
        with open(fil, "r", encoding="UTF8") as fila:
            for linje in fila:
                linje_liste = linje.strip().split(":")
                id = int(linje_liste[0])
                navn_dictionary[id] = Sted(id, linje_liste[1], linje_liste[2])
        return navn_dictionary
    except ZeroDivisionError:
        print("Fila: dokumentet er tom")
    except FileNotFoundError:
        print("Fant ikke dokumentet")
    except:
        print("Feil har oppstått")


# Funksjon som finner avtaler på en gitt dato
def avtale_dato(navn_dictionary, navn_returnert_dictionary, dato):
    for tittel in navn_dictionary:
        avtale = navn_dictionary[tittel]
        avtale_dato = str(avtale.starttidspunkt)
        avtale_dato_liste = avtale_dato.split(" ")
        for index in avtale_dato_liste:
            if dato == avtale_dato_liste[0]:
                navn_returnert_dictionary[tittel] = avtale    
    return navn_returnert_dictionary


# Funksjon som leter etter titler til avtaler i en gitt streng
def avtale_sok(navn_dictionary, navn_returnert_dictionary, streng):
    for tittel in navn_dictionary:
        avtale = navn_dictionary[tittel]
        tittel_lower = tittel.lower()
        streng_lower = streng.lower()
        if streng_lower.find(tittel_lower) >= 0:
            navn_returnert_dictionary[tittel] = avtale
    return navn_returnert_dictionary


# Funksjon som søker etter avtaler som fåregår på et bestemt sted
def søk_etter_sted(avtalebok_dict, søkeord):
    avtale_list = list()
    for a in avtalebok_dict:
        avtale = avtalebok_dict[a]
        sted = int(avtale.sted.id)
        if sted == søkeord:
            avtale_list.append(avtale)
    return avtale_list


# Funksjon for menyvalg
def menyvalg():
    while True:
        try:
            print(
                f"\nValgmuligheter: \n1 = Lese inn avtaler fra fil \n2 = Legge til en ny avtale "
                f"\n3 = Skrive ut alle avtalene \n4 = Slett en avtale \n5 = Rediger en avtale"
                f"\n6 = Legge til ny kategori \n7 = Skriv ut kategorier \n8 = Legg til kategori i eksisterende avtale"
                f"\n9 = Legge til nytt sted\n10 = Skrive ut steder\n11 = Søk avtaler etter sted "
                f"\n12 = Lagre avtalene i en fil \n13 = Avslutte")
            valg_bruker = int(input("Skriv inn tallet som stemmer overens med ønsket valg: "))
            if valg_bruker in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
                break
            else:
                print("Dette tallet stemmer ikke overens med noen av valgene, velg på nytt.")
        except ValueError:
            print("Du må skrive inn et tall.")
    return valg_bruker


# Funksjon som skriver ut index med tilhørende verdi/klasse
def print_dictonary(navn_dictionary, overskrift=""):
    print(f"""\n{"-" * 70}\n{overskrift}""")
    for x in navn_dictionary:
        print(f"""\n*** Index: {x} ***{navn_dictionary[x]}""")
    print(f"""\n{"-" * 70}""")


# Funksjon som legger til en ekstra kategori i en avtale
def legg_til_extra_kategori(avtalebok_dict, kategori_dict):
    print_dictonary(avtalebok_dict, "Avtaler")
    innskrevet_avtale = input("\nSkriv inn navnet på avtalen du vil legge til en kategori i: ")
    print(f"{avtalebok_dict[innskrevet_avtale]}\n")
    print_dictonary(kategori_dict, "Kategorier")
    innskrevet_kategori = int(input("Skriv inn Id på kategorien du vil legge til: "))
    if innskrevet_kategori in kategori_dict:
        valgt_kategori = kategori_dict[innskrevet_kategori]
    else:
        valgt_kategori = ny_kategori(kategori_dict)
    avtalebok_dict[innskrevet_avtale].legg_til_kategori(valgt_kategori)
    print(f"{avtalebok_dict[innskrevet_avtale]}\n")
