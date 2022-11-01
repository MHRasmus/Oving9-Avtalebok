from Avtale_klasse import *
from datetime import datetime


def ny_avtale(avtale_dict):
    #Bruker skriver inn avtaledeljer
    valgt_tittel = input("Skriv inn tittel: ")
    valgt_sted = input("Skriv inn sted: ")

    #Sjekker om brukervalgt tidspunkt er i gyldig format (ÅÅÅÅ-MM-DD TT:MM)
    while True:
        try:
            valgt_starttidspunkt = datetime.strptime(input("Skriv inn starttidspunkt(DD-MM-ÅÅÅÅ TT:MM): "), "%d-%m-%Y %H:%M")
            break
        except ValueError:
            print("***Feil format på tidspunkt***")
            continue

    #Sjekker om brukervalgt varighet er i gyldig format (int)
    while True:
        try:
            valgt_varighet = int(input("Skriv inn varighet i hele minutter: "))
            break
        except ValueError:
            print("Feil format på varighet, skriv i hele minutter")
            continue

    #Lager dictionary med valgte data
    avtale_dict[valgt_tittel] = Avtalebok(valgt_tittel,valgt_sted,valgt_starttidspunkt,valgt_varighet)

    # Printer ut avtalen som er blitt opprettet
    print(f"""{"-"*70}\nAvtalen din har blitt opprettet:{avtale_dict[valgt_tittel]}\n{"-"*70}""")


# Funksjon for redigering av eksisterende avtaler
def rediger_avtale(avtale_dict, valgt_tittel):
    # Bruker skriver inn avtaledeljer
    valgt_sted = str(input("Skriv inn sted: "))

    # Sjekker om brukervalgt tidspunkt er i gyldig format (DD-MM-ÅÅÅÅ TT:MM)
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
            valgt_varighet = int(input("Skriv inn varighet i hele minutter: "))
            break
        except ValueError:
            print("Feil format på varighet")
            continue

    # Lager dictionary med valgte data
    avtale_dict[valgt_tittel] = Avtalebok(valgt_tittel, valgt_sted, valgt_starttidspunkt, valgt_varighet)

    # Printer ut avtalen som er blitt opprettet
    print(f"""{"-" * 70}\nAvtalen din har blitt redigert:{avtale_dict[valgt_tittel]}\n{"-" * 70}""")


# Funksjon som skriver ut index med tilhørende avtale
def print_avtale(avtale_dict, Overskrift="Valgt avtale",):
    print(f"""\n{"-" * 70}""")
    for x in avtale_dict:
        print(f"""\n{Overskrift.upper()}\n***Index, "{x}"***{avtale_dict[x]}""")
    print(f"""\n{"-" * 70}""")


# Funksjon som lagrer en dictionary som en tekstfil
def lagrer_dict(navn_dictionary, fil):
    try:
        with open(fil, "w", encoding="UTF8") as fila:
            for nokkel in navn_dictionary:
                avtale = navn_dictionary[nokkel]
                fila.write(f"{avtale.tittel};{avtale.sted};{avtale.starttidspunkt};{avtale.varighet}\n")
                
    except:
        print("Feil har oppstått")


# Funksjon som lager en dictonary fra en tekstfil
def henter_avtalebok(navn_dictionary, fil):
    try:
        with open(fil, "r", encoding="UTF8") as fila:
            for linje in fila:
                linje_liste = linje.split(";")
                for element in linje_liste:
                    avtale = Avtalebok(linje_liste[0])
                    avtale.tittel = linje_liste[0]
                    avtale.sted = linje_liste[1]
                    avtale.starttidspunkt = datetime.fromisoformat(linje_liste[2])
                    avtale.varighet = int(linje_liste[3])
                navn_dictionary[linje_liste[0]] = avtale
            
    except ZeroDivisionError:
        print("Fila: dokumentet er tom")
    except FileNotFoundError:
        print("Fant ikke dokumentet")
    except:
        print("Feil har oppstått")


# Funksjon som finner avtaler på en gitt dato
def avtale_dato(navn_dictionary,navn_returnert_dictionary,dato):
    for tittel in navn_dictionary:
        avtale = navn_dictionary[tittel]
        avtale_dato = str(avtale.starttidspunkt)
        avtale_dato_liste = avtale_dato.split(" ")
        for index in avtale_dato_liste:
            if dato == avtale_dato_liste[0]:
                navn_returnert_dictionary[tittel] = avtale    
    return navn_returnert_dictionary


# Funksjon som leter etter titler til avtaler i en gitt streng
def avtale_sok(navn_dictionary,navn_returnert_dictionary, streng):
    for tittel in navn_dictionary:
        avtale = navn_dictionary[tittel]
        tittel_lower = tittel.lower()
        streng_lower = streng.lower()
        if streng_lower.find(tittel_lower) >= 0:
            navn_returnert_dictionary[tittel] = avtale
    return navn_returnert_dictionary


# Funksjon for menyvalg
def menyvalg():
    while True:
        try:
            print(
                f"\nValgmuligheter: \n1 = Lese inn avtaler fra fil \n2 = Legge til en ny avtale "
                f"\n3 = Skrive ut alle avtalene \n4 = Slett en avtale \n5 = Rediger en avtale "
                f"\n6 = Lagre avtalene i en fil \n9 = Avslutte")
            valg_bruker = int(input("Skriv inn tallet som stemmer overens med ønsket valg: "))
            if valg_bruker in [1, 2, 3, 4, 5, 6, 9]:
                break
            else:
                print("Dette tallet stemmer ikke overens med noen av valgene, velg på nytt.")
        except ValueError:
            print("Du må skrive inn et tall.")
    return valg_bruker


def ny_kategori(kategori_dict):
    # Bruker skriver inn kategorideljer
    valgt_navn = input("Skriv inn navn: ")

    while True:
        try:
            valgt_id = int(input("Skriv inn id: "))
            break
        except ValueError:
            print("Id må være et gyldig tall")
            continue

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


# Funksjon som lager en tekstfil fra en dictonary med kategorier
def lagrer_kategorier(navn_dictionary, fil):
    try:
        with open(fil, "w", encoding="UTF8") as fila:
            for nokkel in navn_dictionary:
                kategori = navn_dictionary[nokkel]
                fila.write(f"{kategori.id};{kategori.navn};{kategori.prioritet}\n")

    except:
        print("Feil har oppstått")


# Funksjon som lager en dictonary fra en tekstfil med kategorier
def henter_kategorier(navn_dictionary, fil):
    try:
        with open(fil, "r", encoding="UTF8") as fila:
            for linje in fila:
                linje_liste = linje.strip().split(";")
                id = int(linje_liste[0])
                navn_dictionary[id] = Kategori(id, linje_liste[1], linje_liste[2])
    except ZeroDivisionError:
        print("Fila: dokumentet er tom")
    except FileNotFoundError:
        print("Fant ikke dokumentet")
    except:
        print("Feil har oppstått")


# Funksjon som skriver ut index med tilhørende verdi/klasse
def print_dictonary(navn_dictionary, overskrift=""):
    print(f"""\n{"-" * 70}\n{overskrift}""")
    for x in navn_dictionary:
        print(f"""\n*** Index: {x} ***{navn_dictionary[x]}""")
    print(f"""\n{"-" * 70}""")

