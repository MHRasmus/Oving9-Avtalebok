import Avtale_funksjoner as af

#Definerer funksjon for å lage ny avtale
avtale_dict = dict()
avtaleindex_liste = []

#Lager et menyvalg for å kjøre gjennom funksjonen
#og ha mulighet til å lagre flere avtaler samtidig
lag_avtale = input("Lag ny avtale? [Y/N]: ")
while lag_avtale == "Y":
    af.ny_avtale(avtale_dict, avtaleindex_liste)
    lag_avtale = input("Lag ny avtale? [Y/N]: ")


#Lager et menyvalg for om man vil printe ut de lagrete avtalene
print_avtaler = input("Se lagrede avtaler? [Y/N]: ")
while print_avtaler == "Y":
    af.print_avtale(avtale_dict, avtaleindex_liste)
    break


