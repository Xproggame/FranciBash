class Variable:

    def __init__(self):
        self.liste_var = {}

    def creer(self, identifiant:str, valeur:tuple):

        if valeur[1] == 'chaine de caractere':
            valeurfinale = (
                self.Traiter.chaine_de_caractere(valeur[0]),
                valeur[1]
                )

        if valeur[1] == 'nombre entier':
            valeurfinale = (
                    self.Traiter.nombre_entier(valeur[0]),
                    valeur[1]
                    )

    class Traiter:

	    @staticmethod

	    def chaine_de_caractere(chaine:str):
		    return chaine[1:len(chaine) - 1]
		   
		def nombre_entier(valeur:str):
		    return int(valeur)
