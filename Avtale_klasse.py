
#Definerer klassen Avtalebok
class Avtalebok:
    #Definerer variablene i klassen
    def __init__(self,tittel="",sted="",starttidspunkt=0,varighet=0):
        self.tittel = tittel
        self.sted = sted
        self.starttidspunkt = starttidspunkt
        self.varighet = varighet

    def __str__(self):
        return f"\nTittel: {self.tittel}\nSted: {self.sted}\nStarttidspunkt: {self.starttidspunkt}\nVarighet: {self.varighet}"
    def __repr__(self):
        return f"\nTittel: {self.tittel},Sted: {self.sted},Starttidspunkt: {self.starttidspunkt},Varighet: {self.varighet}"




