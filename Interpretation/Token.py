from curses.ascii import isdigit

from Fonction.Fonction import Fonction

class Token:

    def __init__(self, fonction:Fonction):
        self.ligneactuelle = []
        self.fonction = fonction

    def traiter(self, lignebrut:str):
        ligne_actu_non_tok = lignebrut.split()
        mode = 'normal'
        chaine_actu = ''

        for element in self.ligneactuelle:

            if element != '':

                if element[0] == '\"' or element[0] == '\'' or mode == 'chaine de caractere':
                    place_dernier_cara = len(element) - 1

                    if element[place_dernier_cara] != '\"' and element[place_dernier_cara] != '\'':
                        mode = 'chaine de caractere'
                        chaine_actu += f'{element} '

                    else:
                        mode = 'normal'
                        chaine_actu += element
                        self.ligneactuelle.append((chaine_actu, 'chaine de caractere'))
                        chaine_actu = ''

                elif element[0] == '-':
                    self.ligneactuelle.append((element, 'parametre'))

                elif isdigit(element[0]):

                    if element.find('.') != -1:
                        self.ligneactuelle.append((element, 'nombre decimal'))

                    else:
                        self.ligneactuelle.append((element, 'nombre entier'))

                elif element == 'Vrai' or element == 'Faux':
                    self.ligneactuelle.append((element, 'Binaire'))

                else:
                    pass

                    # en cours