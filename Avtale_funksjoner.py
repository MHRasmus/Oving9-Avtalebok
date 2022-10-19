from Avtale_klasse import Avtalebok
from datetime import datetime

#Definerer funksjon for å lage ny avtale
def ny_avtale():
    #Lager et dictionary for lagring av avtalene
    avtale_dict = dict()
    try:
        valgt_tittel = input("Skriv inn tittel: ")
        valgt_sted = input("Skriv inn sted: ")
    except TypeError:
        print("Skriv inn gyldig ord")

    try:
        valgt_starttidspunkt = datetime.strptime(input("Skriv inn starttidspunkt(ÅÅÅÅ-MM-DD,TT:MM:SS): "), "%Y-%m-%d %H:%M:%S")
        formatert_tid = datetime.isoformat(valgt_starttidspunkt)
    except ValueError:
        print("Feil format på innskrevet tidspunkt")

    try:
        valgt_varighet = int(input("Skriv inn varighet i minutter: "))
    except ValueError:
        print("Skriv inn en gyldig varighet i minutter")
   


ny_avtale()