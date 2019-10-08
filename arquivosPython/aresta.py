

''' propriedades de uma aresta'''
class Aresta():
    def __init__(self, origem, destino, peso):
	    self._origem    = origem          #vertice de origem definido pelo identificador
	    self._destino   = destino         #vertice destino definido pelo identificador  
	    self._peso      = peso            #valor do sinal de entrada do estado de controle

    #retorna o vertice de origem da aresta
    def getOrigem(self):
        return self._origem

    #seta o indice vertice de origem da aresta pelo identificador      
    def setOrigem(self, identificador): 
        self._origem = buscaVerticeId(identificador)


    #retorna o vertice de destino da aresta
    def getDestino(self):
        return self._destino

    #seta o destino de uma aresta pelo identificador
    def setDestino(self, identificador):
        self._destino = identificador
	
	
    #retorna o peso da aresta (sinal de entrada)
    def	getPeso(self):
        return self._peso
    
    #seta o peso da aresta (sinal de entrada)
    def setPeso(self, peso):
        self._peso = peso
	
	#exibe origem, destino e peso da aresta
    def __str__(self):
        return "A(%s----%s---->%s)" % (self._origem, self._peso, self._destino)