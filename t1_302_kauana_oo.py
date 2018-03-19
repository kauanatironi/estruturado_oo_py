class pessoa():

	def __init__(self, nome, peso, altura): #init para inicializar -- tbm é o contrutor
		self.nome = nome #self para variavel global/instanciar
		self.peso = peso 
		self.altura = altura
		self.imc = 0
		self.roupas = []

	def calcularIMC(self):
 		self.imc = self.peso/(self.altura*self.altura)
 		return self.imc 

	def mostrarIMC(self):
		print ("O IMC do " + self.nome , "é " , self.calcularIMC())



	def __str__(self): #como o to_string..
		return "a" , str(self.nome), "tem" , str(self.peso), "kg, e", str(self.altura), "de altura"
  

class roupa():
	def __init__(self, cor, tipo):
		self.cor = cor
		self.tipo = tipo
	
	def adicionarRoupas(self, pessoa, roupa, cor):
		pessoa.roupas.append(roupa)
		pessoa.roupas.append(cor)
		return pessoa.roupas
#não precisa ser herança


if __name__ == '__main__':  #para passar os dados

	pessoa1 = pessoa("ana", 60, 1.7)
	pessoa1.calcularIMC()
	roupa1 = roupa("calça", 'azul')

	print (pessoa1.__str__()) #pegar os dados passados no to_string
	print ("e veste " + str(roupa1.adicionarRoupas(pessoa1, roupa1.cor, roupa1.tipo))) #complementar com a roupa/usando o método
	
	print("o cálculo de seu IMC é ") 
	pessoa1.mostrarIMC()