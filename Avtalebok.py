import Avtale_funksjoner as af


#Lager et menyvalg for å kjøre gjennom funksjonen
#og ha mulighet til å lagre flere avtaler samtidig
lag_avtale = input("Lag ny avtale? [Y/N]: ")
while lag_avtale == "Y":
    af.ny_avtale()
    lag_avtale = input("Lag ny avtale? [Y/N]: ")


#Lager et menyvalg for om man vil printe ut de lagrete avtalene
print_avtaler = input("Se lagrede avtaler? [Y/N]: ")
while print_avtaler == "Y":
    af.print_avtale()
    break


