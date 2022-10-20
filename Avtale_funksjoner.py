from Avtale_klasse import Avtalebok
from datetime import datetime



#Definerer funksjon for å lage ny avtale
avtale_dict = dict()
avtaleindex_liste = []
def ny_avtale():
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


#Funksjon som skriver ut index med tilhørende avtale
def print_avtale(Overskrift="Gjeldende avtale"):
    for x in avtaleindex_liste:
        print(f"""\n{Overskrift.upper()}\n***Index, "{x}"***{avtale_dict[x]}""")













