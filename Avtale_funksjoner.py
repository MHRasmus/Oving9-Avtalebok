from Avtale_klasse import *
from datetime import datetime


def ny_avtale(avtale_dict,sted_dict,sted_liste,kategori_dict,kategori_liste):
    #Bruker skriver inn avtaledeljer
    valgt_tittel = input("Skriv inn tittel: ")

    #Printer først eksisterende steder:
    s_liste = list()
    for x in sted_dict.keys():
        s_liste.append(int(x))
    print_avtale(sted_dict,"Eksisterende steder:")
    while True:
            try:
                innskrevet_sted = int(input("Skriv inn id til ønsket sted eller legg til nytt sted ved å skrive et annet tall: "))
                if innskrevet_sted in s_liste:
                    valgt_sted = innskrevet_sted
                    break
                else:
                    ny_sted(sted_dict,sted_liste)
                    valgt_sted = sted_liste[-1]
                    break
            except ValueError:
                print("Id må være heltall")
                continue

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

    #Lar brukeren legge til eksisterende eller ny kategori
    #Printer først eksisterende avtaler
    k_liste = list()
    intern_liste = list()
    for y in kategori_dict.keys():
        k_liste.append(int(y))
    print_avtale(kategori_dict, "Eksisterende kategorier")

    while True:
        try:
            innskrevet_kategori = int(input("Skriv inn Id på kategorien du vil legge til: "))
            if innskrevet_kategori in k_liste:
                intern_liste.append(innskrevet_kategori)
            else:
                ny_kategori(kategori_dict,kategori_liste)
                intern_liste.append(kategori_liste[-1])
            legg_til_ny = input("Vil du legge til en kategori til? [Y/N]: ")
            if legg_til_ny in ["Y", "y"]:
                continue
            else:
                valgt_kategori = str(intern_liste)[1:-1]
                break

        except ValueError:
            print("Id på kategori må være et heltall")



    #Lager dictionary med valgte data
    avtale_dict[valgt_tittel] = Avtalebok(valgt_tittel,valgt_sted,valgt_starttidspunkt,valgt_varighet,valgt_kategori)

    # Printer ut avtalen som er blitt opprettet
    print(f"""{"-"*70}\nAvtalen din har blitt opprettet:{avtale_dict[valgt_tittel]}\n{"-"*70}""")

# Funksjon for redigering av eksisterende avtaler
def rediger_avtale(avtale_dict, valgt_tittel,sted_dict,sted_liste,kategori_dict,kategori_liste):
    #Printer ut eksisterende steder og lar bruker velge nytt sted:
    s_liste = list()
    for x in sted_dict.keys():
        s_liste.append(int(x))
    print_avtale(sted_dict, "Eksisterende steder:")
    while True:
        try:
            innskrevet_sted = int(
                input("Skriv inn id til ønsket sted eller legg til nytt sted ved å skrive et annet tall: "))
            if innskrevet_sted in s_liste:
                valgt_sted = innskrevet_sted
                break
            else:
                ny_sted(sted_dict, sted_liste)
                valgt_sted = sted_liste[-1]
                break
        except ValueError:
            print("Id må være heltall")
            continue

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

    #Lar brukeren endre kategori:
    k_liste = list()
    intern_liste = list()
    for y in kategori_dict.keys():
        k_liste.append(int(y))
    print_avtale(kategori_dict, "Eksisterende kategorier")
    while True:
        try:
            innskrevet_kategori = int(input("Skriv inn Id på kategorien du vil legge til: "))
            if innskrevet_kategori in k_liste:
                intern_liste.append(innskrevet_kategori)
            else:
                ny_kategori(kategori_dict, kategori_liste)
                intern_liste.append(kategori_liste[-1])
            legg_til_ny = input("Vil du legge til en kategori til? [Y/N]: ")
            if legg_til_ny in ["Y", "y"]:
                continue
            else:
                valgt_kategori = str(intern_liste)[1:-1]
                break

        except ValueError:
            print("Id på kategori må være et heltall")

    # Lager dictionary med valgte data
    avtale_dict[valgt_tittel] = Avtalebok(valgt_tittel,valgt_sted,valgt_starttidspunkt,valgt_varighet,valgt_kategori)

    # Printer ut avtalen som er blitt opprettet
    print(f"""{"-" * 70}\nAvtalen din har blitt redigert:{avtale_dict[valgt_tittel]}\n{"-" * 70}""")

# Funksjon som skriver ut index med tilhørende avtale
def print_avtale(avtale_dict, Overskrift="Valgt avtale",):
    print(f"""\n{"-" * 70}""")
    for x in avtale_dict:
        print(f"""\n{Overskrift.upper()}\n***Index, "{x}"***{avtale_dict[x]}""")
    print(f"""\n{"-" * 70}""")

# Funksjon som lagrer en dictionary som en tekstfil
def lagrer_dict(navn_dictionary, fil, kategori_dict, kategori_fil, sted_dict, sted_fil):
    # Lager en tekstfil med kategorier
    lagrer_kategorier(kategori_dict, kategori_fil)

    # Lager en tekstfil med steder
    lagrer_sted(sted_dict, sted_fil)
    #Lager en tekstfil med avtaler
    try:
        with open(fil, "w", encoding="UTF8") as fila:
            for nokkel in navn_dictionary:
                avtale = navn_dictionary[nokkel]
                fila.write(f"{avtale.tittel};{avtale.sted};{avtale.starttidspunkt};{avtale.varighet};{avtale.kategori}")
    except:
        print("Feil har oppstått")

# Funksjon som lager en dictonary fra en tekstfil
#Laster først inn filene med kategorier og steder
def henter_avtalebok(navn_dictionary,fil,kategori_dictionary,kategori_fil,kategori_liste,sted_dictionary,sted_fil,sted_liste):
    #Henter kategori fil
    henter_kategorier(kategori_dictionary,kategori_fil,kategori_liste)

    #Henter sted fil
    henter_sted(sted_dictionary,sted_fil,sted_liste)

    #Leser inn avtaler fra avtale_fil og lager dictionary
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
                    avtale.kategori = linje_liste[4]

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
                f"\n6 = Lagre avtalene i en fil \n7 = Legge til ny kategori \n8 = Legge til nytt sted"
                f"\n9 = Avslutte"
                f"\n10 = Søk avtaler etter sted \n11 = Skriv ut kategorier \n12 = Skrive ut steder")
            valg_bruker = int(input("Skriv inn tallet som stemmer overens med ønsket valg: "))
            if valg_bruker in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
                break
            else:
                print("Dette tallet stemmer ikke overens med noen av valgene, velg på nytt.")
        except ValueError:
            print("Du må skrive inn et tall.")
    return valg_bruker

def ny_kategori(kategori_dict,kategori_liste):
    # Bruker skriver inn kategorideljer
    valgt_navn = input("Skriv inn navn: ")

    while True:
        try:
            valgt_id = int(input("Skriv inn id i heltall: "))
            kategori_liste.append(valgt_id)
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
    return kategori_dict

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
def henter_kategorier(navn_dictionary,fil,kategori_liste):
    try:
        with open(fil, "r", encoding="UTF8") as fila:
            for linje in fila:
                linje_liste = linje.strip().split(";")
                id = int(linje_liste[0])
                kategori_liste.append(int(linje_liste[0]))
                navn_dictionary[id] = Kategori(id, linje_liste[1], linje_liste[2])
        return navn_dictionary,kategori_liste
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

# Funksjon som leser inn nytt sted fra bruker
def ny_sted(sted_dict,sted_liste):
    # Id
    while True:
        try:
            valgt_id = int(input("Skriv inn id: "))
            sted_liste.append(valgt_id)
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
    return sted_dict,sted_liste

# Funksjon som lager en tekstfil fra en dictonary med kategorier
def lagrer_sted(navn_dictionary, fil):
    try:
        with open(fil, "w", encoding="UTF8") as fila:
            for nokkel in navn_dictionary:
                sted = navn_dictionary[nokkel]
                fila.write(f"{sted.id};{sted.navn};{sted.adresse}\n")

    except:
        print("Feil har oppstått")

# Funksjon som lager en dictonary fra en tekstfil med steder
def henter_sted(navn_dictionary,fil,sted_liste):
    try:
        with open(fil, "r", encoding="UTF8") as fila:
            for linje in fila:
                linje_liste = linje.strip().split(";")
                id = int(linje_liste[0])
                navn_dictionary[id] = Sted(id, linje_liste[1], linje_liste[2])
                sted_liste.append(id)
        return navn_dictionary,sted_liste
    except ZeroDivisionError:
        print("Fila: dokumentet er tom")
    except FileNotFoundError:
        print("Fant ikke dokumentet")
    except:
        print("Feil har oppstått")


def søk_etter_sted(avtalebok_dict,avtale_fil,søkeord):
    sted_avtalebok = dict()
    try:
        with open(avtale_fil,"r",encoding="UTF8") as fila:
            for linje in fila:
                linje_liste = linje.strip().split(";")
                if linje_liste[1] not in sted_avtalebok:
                    sted_avtalebok[linje_liste[1]] = linje_liste[0]
                elif type(sted_avtalebok[linje_liste[1]]) == list:
                    sted_avtalebok[linje_liste[1]].append(linje_liste[0])
                else:
                    sted_avtalebok[linje_liste[1]] = [sted_avtalebok[linje_liste[1]], linje_liste[0]]
        if søkeord in sted_avtalebok.keys():
            resultat = sted_avtalebok[søkeord]
        else:
            print("Ingen avtaler har dette stedet")
    except ZeroDivisionError:
        print("Fila: dokumentet er tom")
    except FileNotFoundError:
        print("Fant ikke dokumentet")
    except:
        print("Feil har oppstått")

    #Printer alle avtalene som har valgte sted:
    print(f"Disse avtalene har steds-id:{søkeord}")
    for x in resultat:
        print(avtalebok_dict[x])

