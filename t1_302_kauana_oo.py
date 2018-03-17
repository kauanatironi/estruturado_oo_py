class pessoa():

	def __init__(self, nome, peso, altura): #init para instanciar
		self.nome = nome
		self.peso = peso #variavel global
		self.altura = altura
		self.imc = 0

	def calcularIMC(self):
 		self.imc = self.peso/(self.altura*self.altura)
 		return self.imc 

	def imprimir(self):
		print ("O IMC do %s eh %f") % (self.nome, self.calcularIMC())

	def __str__(self):
		return "a" , str(self.nome), "tem" , str(self.peso), "kg, e", str(self.altura), "de altura"


class roupa(pessoa):
	def __init__(self, cor, tipo):
		self.cor = cor
		self.tipo = tipo
		super(pessoa, self).__init__(nome, peso, altura)
