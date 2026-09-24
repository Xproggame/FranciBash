class Variable:

    def __init__(self):
        self.liste_var = {}

    def creer(self, identifiant:str, valeur:tuple):

        if valeur[1] == 'chaine de caractere':
            valeurfinal = valeur

        if valeur