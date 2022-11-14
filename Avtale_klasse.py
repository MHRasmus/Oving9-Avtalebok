
#Definerer klassen Avtalebok
class Avtalebok:
    #Definerer variablene i klassen
    def __init__(self,tittel="",sted=list(),starttidspunkt=0,varighet=0,kategori=""):
        self.tittel = tittel
        self.sted = sted
        self.starttidspunkt = starttidspunkt
        self.varighet = varighet
        self.kategori = kategori



    # lager en liste med katergorier:
    def legg_til_kategori(self,kategori):
        return self.kategori.append(kategori)

    def __str__(self):
        return f"\nTittel: {self.tittel}\nSted: {self.sted}\nStarttidspunkt: {self.starttidspunkt}\nVarighet: {self.varighet}\nKategori: {str(self.kategori)}"
    def __repr__(self):
        return f"\nTittel: {self.tittel},Sted: {self.sted},Starttidspunkt: {self.starttidspunkt},Varighet: {self.varighet}"


#Definerer klassen Kategori
class Kategori:
    def __init__(self, id, navn, prioritet="Vanlig"):
        self.id = id
        self.navn = navn
        self.prioritet = prioritet

    def __str__(self):
        return f"\nId: {self.id} \nNavn: {self.navn} \nPrioritet: {self.prioritet}"


class Sted:
    def __init__(self, id, navn, adresse):
        self.id = id
        self.navn = navn
        self.adresse = adresse
    
    def __str__(self):
        return f"\nId: {self.id}\nNavn: {self.navn}\nAdresse: {self.adresse}"


