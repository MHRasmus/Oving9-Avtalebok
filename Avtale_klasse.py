
# Definerer klassen Avtalebok
class Avtalebok:
    # Definerer variablene i klassen
    def __init__(self, tittel="", sted="", starttidspunkt=0, varighet=0, kategori=list()):
        self.tittel = tittel
        self.sted = sted
        self.starttidspunkt = starttidspunkt
        self.varighet = varighet
        self.kategori = kategori

    def legg_til_kategori(self, kategori):
        self.kategori.append(kategori)

    def __str__(self):
        return f"\nTittel: {self.tittel}\nSted: {(str(self.sted))}\nStarttidspunkt: {self.starttidspunkt}" \
               f"\nVarighet: {self.varighet}\nKategori: {' '.join(map(str, self.kategori))}"

    def __repr__(self):
        return f"{self.tittel};{repr(self.sted)};{self.starttidspunkt};{self.varighet};{repr(self.kategori)}"


# Definerer klassen Kategori
class Kategori:
    def __init__(self, id, navn, prioritet="Vanlig"):
        self.id = id
        self.navn = navn
        self.prioritet = prioritet

    def __str__(self):
        return f"\n  Id: {self.id} \n  Navn: {self.navn} \n  Prioritet: {self.prioritet}"

    def __repr__(self):
        return f"{self.id},{self.navn},{self.prioritet}: "


# Definerer klassen Sted
class Sted:
    def __init__(self, id, navn, adresse):
        self.id = id
        self.navn = navn
        self.adresse = adresse

    def __str__(self):
        return f"\n  Id: {self.id}\n  Navn: {self.navn}\n  Adresse: {self.adresse}"

    def __repr__(self):
        return f"{self.id}:{self.navn}:{self.adresse}"
