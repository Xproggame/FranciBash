from Contenant.Appartenance import Appartenance

appartenance = Appartenance()

class Fonction:

    def __init__(self):
        self.listefonct = {}

    def creer(self, nom:str, listparametre:list):
        self.listefonct[nom] = {
            'contenu':[],
            'parametre':[]
        }

        if listparametre != []:

            for parametre in listparametre:
                self.listefonct[nom]['parametre'].append(parametre)

    def contenu(self, ligne:list, nomfonct:str):
        self.listefonct[nomfonct]['contenu'].append(ligne)