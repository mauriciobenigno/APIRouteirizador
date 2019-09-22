#from complementoGrafo import Vertice,Aresta
import sys

class Aresta():
	def __init__(self,destino,peso = 0):
		self.destino = destino
		self.peso = peso	
		
	def setDestino(self,destino):
		self.destino = destino

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

# Grafo
class Grafo:
    def __init__(self, direcionado=True):
            self.lista_Vertices = []

    def addVertice(self, identificador):
        self.lista_Vertices.append(Vertice(identificador))

    def busca_Vertice(self, identificador):
        for i in self.lista_Vertices:
            if identificador == i.getId():
                return i
        else:
            return None

    def nova_Aresta2(self,origem , aresta):
        origem_aux = self.busca_Vertice(origem)
        destino_aux = aresta.getDestino()
        if (origem_aux is not None) and (destino_aux is not None):
            for vert in self.lista_Vertices:
                if vert == origem_aux:
                    vert.addAresta(aresta)
        else:
            print("Um do Vertice ou ambos são invalidos")

    def nova_Aresta(self, origem, destino, peso): 
        origem_aux = self.busca_Vertice(origem)
        destino_aux = self.busca_Vertice(destino)
        if (origem_aux is not None) and (destino_aux is not None):
            for vert in self.lista_Vertices:
                if vert == origem_aux:
                    vert.addAresta(Aresta(destino,peso))
        else:
            print("Um do Vertice ou ambos são invalidos")

    def imprime_Vertices(self):
        for vert in self.lista_Vertices:
            print("Vertice: ",vert.getId())
            arestas = vert.getArestas()
            for aresta in arestas:
                print("-- Destino: ",aresta.getDestino(), " peso: ",aresta.getPeso())

    '''def numVertice(self,id):
        contador = 0
        for vert in self.lista_Vertices:
            if vert.getId() == id:
                return contador
            contador=contador+1

    def dijsktra(self, Grafo, pontoInicio):
        distancias = [len(self.lista_Vertices)]
        navegador = self.lista_Vertices[0]
        historico = []  
        vert = 0

        for i in range(len(distancias)):
            distancias[i] = sys.maxint

        distancias[0] = 0 # a posicao 0 é sempre a inicial e a ultima posicao do vetor é a final
        predecessor = []
        predecessor.append ((navegador,distancias[0]))

        while len(predecessor) > 0:
            vert=vert+1
            predecessor.pop
            for j in range(0 , len(navegador.getArestas())):
                arestasAux = navegador.getArestas()
                peso = arestasAux[i]
                pesoanterior = distancias[self.numVertice(arestasAux.getId())]

                if peso < pesoanterior:'''

        


    '''def minDist(self,distancia,visitado):
        min = sys.maxint
        minIndex = None
        for v in range(0,len(self.lista_Vertices)):
            if visitado[v] == False and distancia[v] <= min:
                min = distancia[v]
                minIndex = v

        return minIndex

    def dijkstra(self, pontoInicial):
        distancia = [len(self.lista_Vertices)]
        visitado =  [len(self.lista_Vertices)]
        for i in range (0,len(self.lista_Vertices)):
            distancia[i] = sys.maxint
            visitado[i] = False
        
        for c in range (0,len(self.lista_Vertices)-1):
            u = self.minDist(distancia,visitado)
            visitado[u]=True
            for v in range(0,len(self.lista_Vertices[u].getArestas())):
                if visitado[v]==False and self.lista_Vertices[u].getArestas() != Null:'''

