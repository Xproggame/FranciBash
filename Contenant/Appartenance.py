class Appartenance:

    def __init__(self):
        self.contenant = {}
        self.contenuprece = {'numligne':'', 'ligne':''}

    def creercontenant(self, lignebrut:str, niveau:int, numligne:str, appartenance:str):
        self.contenant[numligne] = {'ligne':lignebrut, 'niveau':niveau, 'contenu':[], 'appartenance':appartenance}

    def ajouter(self, lignebrut:str, appartenance:str, numligne:str):
        niveau = 0
        niveaucontenant = self.contenant[appartenance]['niveau']

        for caractere in lignebrut:

            if caractere == ' ':
                niveau += 1

            else:
                break

        if niveau == niveaucontenant + 1:
            lignebrut = lignebrut[niveau:]
            self.contenant[appartenance]['contenu'].append({'ligne':lignebrut, 'numligne':numligne})
            self.contenuprece = {'numligne':numligne, 'ligne':lignebrut}
            return True

        if niveau <= niveaucontenant and niveau != 0:

            while True:
                potcontenant = self.contenant[appartenance]['appartenance']

                if niveau == self.contenant[potcontenant]['niveau'] + 1:
                    lignebrut = lignebrut[niveau:]
                    self.contenant[potcontenant]['contenu'].append({'ligne':lignebrut, 'numligne':numligne})
                    self.contenuprece = {'numligne':numligne, 'ligne':lignebrut}
                    return True

                else:
                    lignebrut = lignebrut[niveau:]
                    appartenance = self.contenant[appartenance]['appartenance']
                    self.contenuprece = {'numligne': numligne, 'ligne': lignebrut}
                    return True

        if niveau == niveaucontenant + 2:
            nouvappartenance = self.contenuprece['numligne']
            ancligne = self.contenuprece['ligne']
            self.creercontenant(ancligne, niveau - 1, nouvappartenance, appartenance)
            self.ajouter(lignebrut, nouvappartenance, numligne)

        if niveau == 0:
            return False

        else:
            # erreur
            return None