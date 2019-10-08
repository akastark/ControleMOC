from vertice import Vertice
from aresta import Aresta

#implementacao da classe grafo

class Grafo(object):
    """ Propriedades de um grafo """

    def __init__(self, direcionado):
        
        #definicoes da estrutura grafo
        self._vertices      = []
        self._arestas       = []
        self._direcionado   = direcionado



    #insere um novo vertice o grafo
    def novoVertice(self, identificador, estado, sinal, acaoControle):
        self._vertices.append(Vertice(identificador, estado, sinal, acaoControle))


    #retorna o indice, do vertice na lista de vertices do grafo
    def buscaVerticeId(self, identificador):
        j = 0
        for i in self._vertices:
            if identificador == i.getId():
                return j
            j += 1
        else:
            return None

    #retorna o objeto na lista de vertices do grafo
    def buscaVerticeIdObjeto(self, identificador):
        for i in self._vertices:
            if identificador == i.getId():
                return i
        else:
            return None

    #retorna o identificador do vertice com sinal correspondente
    def buscaVerticeSinal(self, sinal):
        for i in self._vertices:
            if sinal == i.getSinal():
                return i._identificador;
        else:
            return None

    #retorna o identificador do vertice referente ao estado procurado
    def buscaVerticeEstado(self, estado):
        for i in self._vertices:
            if estado == i.getEstado():
                return i._identificador;
        else:
            return None

    #busca o vertice pela acao de controle desejada
    def buscaVerticeEstado(self, acaoControle):
        for i in self._vertices:
            if acaoControle == i.getAcaoControle():
                return i._identificador;
        else:
            return None

    #retorna uma lista com todos os vertices
    def getVertices(self):
        """ Retorna a lista de vértices do grafo. """
        return list(range(len(self._vertices)))



    #insere aresta pelos identificadores dos estados
    def novaAresta(self, origem, destino, peso):  
        origemIndex = self.buscaVerticeId(origem)
        destinoIndex = self.buscaVerticeId(destino)

        if (origemIndex is not None) and (destinoIndex is not None):
            self._arestas.append(Aresta(origemIndex, destinoIndex, peso))
            print("okkkkkkk")
        else:
            print("vertice invalido")

    #busca uma aresta pelos identificadores
    def buscaAresta(self, x, y):
        origemIndex = self.buscaVerticeId(x)
        destinoIndex = self.buscaVerticeId(y)

        #print(self._arestas)
        for k in self._arestas:
            origem = k.getOrigem()
            destino = k.getDestino()
        
            if (origem == origemIndex) and (destino == destinoIndex):       #se os indices forem iguais
                #print(self._vertices[origem].getId(), k.getPeso(), self._vertices[destino].getId())
                return k.getPeso()
        else:
            return 0


    #seta todos os vertices como não visitados
    def setaVisitadosFalso(self):
        for m in self._vertices:
            m.setVisitado(False)




    #exibe matriz de adjacencias
    def exibeMatrizAdjacencia(self):

        tam = len(self._vertices)
        
        print("    | ", end="")
        for vert in self._vertices:
            print(vert.getEstado() + " | ", end="")
        
        for vert in self._vertices:
            print("")
            print("| " + vert.getEstado() + " |", end="")

            #j = 0
            #while(j < tam):
            for vert2 in self._vertices:
                #print(" ", end="")
                print(" " + str(self.buscaAresta(vert.getId(), vert2.getId())) + " |", end="")
                #print(" |", end="")
                #j += 1



                




