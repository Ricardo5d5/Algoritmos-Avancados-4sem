'''
Aula do 11/05/2022

'''
class No:
    info=0
    proximo=None
    def __init__(self, info,proximo=None):
        self.info=info
        self.proximo=proximo


class Pilha:
    inicio=None
    altura=0
    def __init__(self):
        self.inicio=None
        self.altura=0
    
    def empilha(self, x): 
        no=No(x)
        no.proximo=self.inicio
        self.inicio=no
        self.altura+=1
        
    def imprime(self):
        ponteiro=self.inicio
        while ponteiro!=None:
            print(ponteiro.info, end="->")
            ponteiro=ponteiro.proximo
        print()
        
    def desempilha(self):
        if self.inicio==None:
            return None
        n=self.inicio.info
        self.inicio=self.inicio.proximo
        self.altura-=1
        return n

    def vazia(self):
        return self.inicio==None
    
    def topo(self):
        return self.inicio.info

class Grafo:
    vertices=None
    
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
    
    def marcarAresta(self, v1, v2):
        for v in self.vertices:
            if v.info==v1:
                v=v.proximo
                print ('v1:',v1, '\nv2:',v2)
                while v.info != v2:
                    v=v.proximo
                v.info='x'
        for v in self.vertices:
            if v.info==v2:
                v=v.proximo
                while v.info != v1:
                    v=v.proximo
                v.info='x'
                
    def arestaDesmarcada(self, vtc):
        for v in self.vertices:
            if v.info==vtc:
                v=v.proximo
                while v!=None and v.info=='x':
                    v=v.proximo
                return v
        return None
    
    def caminhoEuleriano(self):
        S=Pilha()
        verticeInicial=None
        for v in self.vertices:
            grauV=self.grauDoVertice(v.info)
            if grauV%2==1:
                verticeInicial=v.info
                break
        if verticeInicial==None:
            verticeInicial=self.vertices[0].info
        
        S.empilha(verticeInicial)
        caminho=[]
        while not S.vazia():
            u=S.topo()
            w=self.arestaDesmarcada(u)
            if w!=None:
                S.empilha(w.info)
                print('Empilhando: ', w.info)
                self.marcarAresta(u, w.info)
            else:
                t=S.desempilha()
                caminho.append(t)
        print('Caminho euleriano: ', caminho)
        
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
g.insereVertice('e')


g.insereAresta('a','c')
g.insereAresta('a','b')
g.insereAresta('b','c')
g.insereAresta('b','d')
g.insereAresta('b','e')
g.insereAresta('c','e')
g.insereAresta('c','d')
g.insereAresta('d','e')
g.insereAresta('d','e')


g.listaTodasArestas()
g.caminhoEuleriano()
