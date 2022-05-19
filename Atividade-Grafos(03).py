'''

Nome: Ricardo Silva dos Santos
4° termo em Big Data no Agronegócio
Disciplina: Algoritmos Avançados
Professor: Adriano Nakamura

Atividade - Grafos (03) - Bonificação
Vence hoje às 23:59
Instruções
Implemente uma função que verifique se existe um caminho entre 2 vértices
(bônus de 2 pontos para quem resolver utilizando recursividade)
Serão bonificados os primeiros 7 alunos que enviarem a implementação de acordo.
Meu trabalho

'''


class No:
    info = 0
    proximo = None
    def __init__(self, info, proximo = None):
        self.info = info
        self.proximo = proximo

class Grafo:
    vertices = None


    def __init__(self):
        self.vertices=[]
    
    def insereVertice(self, v):
        self.vertices.append(No(v))
        
    def insereAresta(self, v1, v2):
        no1=No(v1)
        no2=No(v2)
        for v in self.vertices:
            if v.info==v1:
                while(v.proximo!=None):
                    v=v.proximo
                v.proximo=no2
                break
            
        for v in self.vertices:
            if v.info==v2:
                while(v.proximo!=None):
                    v=v.proximo
                v.proximo=no1
                break
            
    def listaTodasArestas(self):
        for v in self.vertices:
            vertice=v.info
            while(v.proximo!=None):
                v=v.proximo
                print('Aresta:',vertice, ',',v.info)
    
    def verticesAdjacentes(self, vtc):
        for v in self.vertices:
            if v.info==vtc:
                v=v.proximo
                print('Vertices adjacentes a ',vtc)
                while v!=None:
                    print(str(v.info))
                    v=v.proximo
                break
            
    def grauDoVertice(self, vtc):
        for v in self.vertices:
            if v.info==vtc:
                v=v.proximo
                contador=0
                while v!=None:
                    contador+=1
                    v=v.proximo
                return contador    
        
    def grauDoGrafo(self):
        grauGrafo=0
        for v in self.vertices:
            grauVertice=0
            v=v.proximo
            while v!=None:
                grauVertice+=1
                v=v.proximo
            if grauVertice>grauGrafo:
                grauGrafo=grauVertice
        return grauGrafo   
        
    def grafoRegular(self):
        grauGrafo=0
        for v in self.vertices:
            grauVertice=0
            v=v.proximo
            while v!=None:
                grauVertice+=1
                v=v.proximo
            if grauGrafo==0:
                grauGrafo=grauVertice
            elif grauGrafo!=grauVertice:
                return False
        return True   
    
    def eAdjacente(self, v, no):
        if no==None:
            return False
        if v==no.info:
            return True
        return self.eAdjacente(v, no.proximo)

    def existeAresta(self, v1, v2):
        for v in self.vertices:
            if v.info==v1:
                return self.eAdjacente(v2, v.proximo)

        '''        v=v.proximo
                while v!=None:
                    if v.info==v2:
                        return True
                    v=v.proximo
                break
        return False
'''
    
    
    #========================================================================
   
    #Atividade - Grafos (03)
    #Bonificação
    def mostraLista(self):
        print("Lista de Adjacências:")
        for v in self.vertices:
            print(v.info, ':', end='  ')
            while (v.proximo != None):
                v = v.proximo
                print(v.info, end=' ')
                if (v.proximo != None):
                    print( '->', end='  ')
            print()

    def mostraAresta(self, vtc):
        aresta = []
        for v in self.vertices:
            if v.info == vtc:
                v = v.proximo
                while v != None:
                    aresta.append(v.info)
                    v = v.proximo
                return aresta

    def existeCaminho(self, vtc1, vtc2):
        pilha = [(vtc1, [vtc1])]
        
        while pilha:
            vertice, caminho = pilha.pop()
            #print('g.mostraAresta(vertice):', g.mostraAresta(vertice))
            for proximo in set(g.mostraAresta(vertice)) - set(caminho):
                if proximo == vtc2:
                    yield caminho + [proximo]
                else:
                    pilha.append((proximo, caminho + [proximo]))
                    #print('pilha (else):', pilha)

    #=====================================================================

    
def arestasDoVertice(v, no):
    if no!=None:
        print(v,'->',no.info)
        arestasDoVertice(v, no.proximo)
    
def listaTodasArestas(grafo):
    for v in grafo:
        arestasDoVertice(v.info, v.proximo)

  


g=Grafo()
g.insereVertice('a')
g.insereVertice('b')
g.insereVertice('c')
g.insereVertice('d')
g.insereVertice('e')
g.insereVertice('f')
g.insereAresta('a','b')
g.insereAresta('a','d')
g.insereAresta('b','c')
g.insereAresta('c','d')
#g.insereAresta('a','c')
#g.insereAresta('b','d')
g.insereAresta('d','e')
#g.insereAresta('e','f')

'''g.insereVertice('e')

g.insereAresta('a','b')
g.insereAresta('a','e')
g.insereAresta('b','c')
g.insereAresta('d','c')
g.insereAresta('b','d')
g.insereAresta('c','d')
g.insereAresta('e','d')'''


v1='a'
v2='e'


print()
print("Atividade - Grafos (03)")
print("Bonificação")
print()
caminho = list(g.existeCaminho(v1, v2))
if len(caminho) > 0:
    if len(caminho) == 1:
        print('Existe ',len(caminho), " caminho entre '", v1, "' e '", v2, "'", sep='')
    else:
        print('Existem ',len(caminho), " caminho entre '", v1, "' e '", v2, "'", sep='')
        print('O menor caminho é:', min(caminho, key = len))
    print(caminho)
else:
    print('Não existe caminho entre', v1, 'e', v2)

