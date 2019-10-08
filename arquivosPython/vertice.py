from aresta import Aresta

#implementacao da classe vertice

class Vertice(object):
    """ Propriedades de um vertice """

    def __init__(self, identificador, estado, sinal, acaoControle, visitado = False):

        #propriedades da estrutura do grafo
        self._identificador = identificador       #identificador da estrutura grafo
        self._visitado      = visitado            #variavel usada para controle das funcoes de busca

        #propriedades referentes a identificacao do estados de controle
        self._estado        = estado              #identificador do estado referente ao estado de controle [So, S1, S2.....]
        self._sinal         = sinal               #sinal que trouxe a este estado [u-entrada]
        self._acaoControle  = acaoControle        #acao de controle a ser realizada neste estado


    '''getters e setters'''

    #manipuladores de identificador
    def getId(self):
        return self._identificador

    def setId(self, identificador):
        self._identificador = identificador

    #manipuladores de visita
    def getVisitado(self):
        return self._visitado

    def setVisitado(self, visitado):
        self._visitado = visitado


    #manipuladores de estado
    def getEstado(self):
        return self._estado

    def setEstado(self, estado):
        self._estado = estado


    #manipuladores de sinal
    def getSinal(self):
        return self._sinal

    def setSinal(self, sinal):
        self._sinal = sinal

    #manipuladores de acao de controle
    def getAcaoControle(self):
        return self._acaoControle

    def setAcaoControle(self, acaoControle):
        self._acaoControle = acaoControle

