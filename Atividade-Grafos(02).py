'''
Nome: Ricardo Silva dos Santos
4° termo em Big Data no Agronegócio
Disciplina: Algoritmos Avançados
Professor: Adriano Nakamura

Atividade - Grafos (02)
Vence 4 de maio de 2022 às 13:30
Instruções
Implemente uma função que retorne a ordem do grafo
Implemente uma função que retorne o número de arestas do grafo
Implemente uma função que verifique se um grafo é completo retornando True em caso afirmativo, ou False, caso contrário
Implemente uma função que verifique se um grafo é totalmente desconexo retornando True em caso afirmativo, ou False, caso contrário
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


    #Atividade - Grafos (02)
    #Exercicio 1
    def ordemGrafo(self):
        return len(self.vertices)
    
    #Exercicio 2
    def numArestas(self):
        somaArestas = 0
        for v in self.vertices:
            grauVertice = 0
            v = v.proximo
            while v != None:
                grauVertice += 1
                v = v.proximo
            somaArestas = somaArestas + grauVertice
        return somaArestas / 2
    
    #Exercicio 3
    def grafoCompleto(self):
        Kn = len(self.vertices)
        Kn = (Kn * (Kn - 1)) / 2
        somaArestas = 0

        print("Kn:", Kn)
        for v in self.vertices:
            grauVertice = 0
            v = v.proximo
            while v != None:
                grauVertice += 1
                v=v.proximo
            somaArestas = somaArestas + grauVertice
        if (somaArestas / 2) != Kn:
            return False
        else:
            return True
    
    #Exercicio 4
    def grafoTotalDesconexo(self):
        
        for v in self.vertices:
            grauVertice = 0
            v = v.proximo
            while v != None:
                grauVertice += 1
                v = v.proximo
            if grauVertice != 0:
                return False            
        return True   

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
    
    def eAdjacente(self,v, no):
        if no==None:
            return False
        if v==no.info:
            return True
        return self.eAdjacente(v, no.proximo)
    
    def existeAresta(self, v1, v2):
        for v in self.vertices:
            if v.info==v1:
                return self.eAdjacente(v2,v.proximo)
'''
                v=v.proximo
                while v!=None:
                    if v.info==v2:
                        return True
                    v=v.proximo
                break
        return False
''' 
    

def arestasDoVertice(v, no):
    if no!=None:
        print(v,'->',no.info)
        arestasDoVertice(v,no.proximo)
    
def listaTodasArestas(grafo):
    for v in grafo:
        arestasDoVertice(v.info, v.proximo)


    


g=Grafo()
g.insereVertice('a')
g.insereVertice('b')
g.insereVertice('c')
g.insereVertice('d')
g.insereAresta('a','b')
g.insereAresta('a','d')
g.insereAresta('b','c')
g.insereAresta('c','d')
g.insereAresta('a','c')
g.insereAresta('b','d')

'''g.insereVertice('e')

g.insereAresta('a','b')
g.insereAresta('a','e')
g.insereAresta('b','c')
g.insereAresta('d','c')
g.insereAresta('b','d')
g.insereAresta('c','d')
g.insereAresta('e','d')'''

g.listaTodasArestas()
g.verticesAdjacentes('d')
vtc='d'
print('Grau do vertice ',vtc,':', g.grauDoVertice(vtc))
print('Grau do grafo: ', g.grauDoGrafo())
if g.grafoRegular():
    print('O grafo é regular!')
else:
    print('O grafo NÃO é regular!')
v1='a'
v2='c'
if g.existeAresta(v1, v2):
    print('Existe uma aresta entre ', v1, 'e', v2)
else:
    print('NÃO existe uma aresta entre ', v1, 'e', v2)

print()
print("listaTodasArestas:")    
listaTodasArestas(g.vertices)

print()
print("Atividade - Grafos (02)")
print("Exercicio 1")
print("Ordem do Grafo:", g.ordemGrafo())

print("Exercicio 2")
print("Número de Arestas:", g.numArestas())

print("Exercicio 3")
print("Grafo é Completo?", g.grafoCompleto())

print("Exercicio 4")
print("Grafo é Totalmente Desconexo?", g.grafoTotalDesconexo())
