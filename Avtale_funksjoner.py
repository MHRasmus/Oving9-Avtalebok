from Avtale_klasse import Avtalebok
from datetime import datetime

#Definerer funksjon for å lage ny avtale
avtale_dict = dict()
avtaleindex_liste = []
def ny_avtale():
        #Lager et dictionary for lagring av avtalene
    lag_avtale = input("Lag ny avtale? [Y/N]: ")
    while lag_avtale == "Y":
        #Bruker skriver inn avtaledeljer
        valgt_tittel = str(input("Skriv inn tittel: "))
        valgt_sted = str(input("Skriv inn sted: "))

        #Sjekker om brukervalgt tidspunkt er i gyldig format (ÅÅÅÅ-MM-DD TT:MM)
        while True:
            try:
                valgt_starttidspunkt = datetime.strptime(input("Skriv inn starttidspunkt(ÅÅÅÅ-MM-DD TT:MM): "), "%Y-%m-%d %H:%M")
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
                print("Feil format på varighet")
                continue

        #Lager dictionary med valgte data
        avtale_dict[valgt_tittel] = Avtalebok(valgt_tittel,valgt_sted,valgt_starttidspunkt,valgt_varighet)

        #Legger keys inn i en liste
        avtaleindex_liste.append(valgt_tittel)
        print(f"""{"-"*70}\nAvtalen din har blitt opprettet:{avtale_dict[valgt_tittel]}\n{"-"*70}""")
        lag_avtale = input("Lag ny avtale? [Y/N]: ")

#Funksjon som skriver ut index med tilhørende avtale
def print_avtale(Overskrift="Gjeldende avtale"):
    for x in avtaleindex_liste:
        print(f"""\n{Overskrift.upper()}\n***Index {x}***{avtale_dict[x]}""")


# Funksjon som lagrer en dictionary som en tekstfil
def lagrer_dict(navn_dictionary):
    try:
        with open("avtalebok.txt", "w", encoding="UTF8") as fila:
            for nokkel in navn_dictionary:
                avtale = navn_dictionary[nokkel]
                fila.write(f"{avtale.tittel};{avtale.sted};{avtale.starttidspunkt};{avtale.varighet}\n")
                
    except:
        print("Feil har oppstått")


# Funksjon som henter avtaleboken fra tekstfil
def henter_avtalebok(navn_dictionary):
    try:
        with open("avtalebok.txt", "r", encoding="UTF8") as fila:
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
        print("Fila: avtalebok.txt er tom")
    except FileNotFoundError:
        print("Fant ikke avtalebok.txt")
    except:
        print("Feil har oppstått")

