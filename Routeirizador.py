import json
import requests
import googlemaps
from Grafo import Grafo 
from complementoGrafo import Aresta

class Router:

    def __init__(self):
        #CONSUMO API MAPS#
        self.gmaps = googlemaps.Client(key='AIzaSyAG5pDTY-CY2f8Xy65wjvDaCvLnm2yCJyI')
        print("Iniciou")

    def ConsultaDistancia(self, pontoInicial,PontoDestino):
        requisicao = self.gmaps.distance_matrix(pontoInicial,PontoDestino)['rows'][0]['elements'][0] 
        return requisicao

    def CalculaRota(self, pontoInicial, listaDestinos):
        print("teste")

    def CalculaRotaComFinal(self,pontoInicio,pontoFinal,listaDestinos):
        ''' CRIANDO GRAFO E ADICIONANDO OS PESOS '''
        grafo = Grafo()
        grafo.addVertice(pontoInicio)
        grafo.addVertice(pontoFinal)
        for item in listaDestinos:
            grafo.addVertice(item)
        # Primeiro ponto apontando para os intermediarios
        for ponto in listaDestinos:
            dist = self.gmaps.distance_matrix(pontoInicio,ponto)['rows'][0]['elements'][0] 
            grafo.nova_Aresta(pontoInicio,ponto,int(dist['distance']['value']))
        # Intermediarios apontando para os outros intermediarios
        for ponto in listaDestinos: # itera sobre a lista de pontos
            for pontoDest in listaDestinos: # verifica se o ponto nao esta apontando pra si proprio
                if ponto != pontoDest:
                    dist = self.gmaps.distance_matrix(ponto,pontoDest)['rows'][0]['elements'][0]
                    grafo.nova_Aresta(ponto,pontoDest,int(dist['distance']['value'])) # alimenta o grafo com apontamento e peso
        # Intermediarios apontando para o final
        for ponto in listaDestinos:
            dist = self.gmaps.distance_matrix(ponto,pontoFinal)['rows'][0]['elements'][0]
            grafo.nova_Aresta(ponto,pontoFinal,int(dist['distance']['value']))

        #Imprime o grafo
        grafo.imprime_Vertices()

        #Calcula o menor Caminho
        #print(grafo.nodes(), grafo.edges())     