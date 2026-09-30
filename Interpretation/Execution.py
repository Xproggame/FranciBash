from Interpretation.Token import Token
from Identifiant.Variable import Variable

class Execution:

	def __init__(self, token:Token, variable:Variable):
		self.token = token
		self.variable = variable

	def attribution(self, lignebrut:str):
		self.token.traiter(lignebrut)
		ligne = self.token.ligneactuelle

		if ligne[0][1] == 'variable':

			if ligne[1][1] == 'definition':
				valeur = ligne[2:]
				# en cours
