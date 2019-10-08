from grafo import Grafo
#from buscaProfundidade import *
#from PRIM import *

# Cria e imprime o grafo.
grafo = Grafo(direcionado = False)

grafo.novoVertice('1', 'a', '0.1', 'nada')
grafo.novoVertice('2', 'b', '0.2', 'nada')
grafo.novoVertice('3', 'c', '0.3', 'nada')
grafo.novoVertice('4', 'd', '0.4', 'nada')
print(grafo._vertices[3])

k= grafo._vertices[3]

print(k.getSinal())
print(grafo.buscaVerticeEstado('b'))

#PRIM(grafo, k)

print(grafo._vertices[1].getVisitado())

print('tamanho')
print(len(grafo._vertices))
print("\n\n")




grafo.setaVisitadosFalso()
grafo.novaAresta('1', '3', '5')
grafo.novaAresta('2', '4', '3')
grafo.novaAresta('4', '2', '1')
grafo.novaAresta('1', '1', '1')
grafo.novaAresta('4', '4', '9')

grafo.exibeMatrizAdjacencia()

#buscaProfundidade(grafo, grafo._vertices[1])