class Aresta():
	def __init__(self,destino,peso = 0):
		self.destino = destino
		self.peso = peso	
		
	def setDestino(self,vertice):
		self.destino = vertice

	def setpeso(self,peso):
		self.peso = peso
		
	def getDestino(self):
		return self.destino
		
	def	getPeso(self):
		return self.peso
		        
class Vertice():
	def __init__(self,id):
		self.id = id
		self.lista_arestas = []
	
	def setId(self,id):
		self.id=id
	
	def addAresta(self, aresta):
		self.lista_arestas.append(aresta)
	
	def getId(self):
		return self.id

	def getArestas(self):
		return self.lista_arestas
