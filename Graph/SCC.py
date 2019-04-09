'''
Strongly connected component
'''
class vertex:
    def __init__(self,name):
        self.name=name
        self.d=None
        self.f=None
        self.color='white'
        self.ancestor=None

class graph(vertex):
    def __init__(self,Adj):
        V=[]
        for u in Adj.keys():
            if u not in V:
                V.append(u)
            for v in Adj[u]:
                if v not in V:
                    V.append(v)
        self.Adj=Adj
        self.V=V
    def refresh(self):
        for vertex in self.V:
            vertex.d=None
            vertex.f=None
            vertex.color='white'
            vertex.ancestor=None
time=0
topoSort=[]
def DFS(G):
    global time
    for vertex in G.V:
        if vertex.color=='white':
            DFS_VISIT(G,vertex)
    return topoSort

def DFS_VISIT(G,vertex):
    global time
    global topoSort
    time+=1
    vertex.d=time
    vertex.color='grey'
    for u in G.Adj[vertex]:
        if u.color=='white':
            u.ancestor=vertex
            DFS_VISIT(G,u)
    time+=1
    vertex.f=time
    vertex.color='black'
    topoSort.insert(0,vertex)

def G_T(G):
    G_T={}
    for u in G.Adj.keys():
        for v in G.Adj[u]:
            if v not in G_T.keys():
                G_T[v]=[u]
            else:
                G_T[v].append(u)
    G_T=graph(G_T)
    return(G_T)

def DFS_G_T(G_T,topoSort):
    global time
    time=0
    G_T.refresh()
    for i in range(len(topoSort)):
        if topoSort[i].color=='white':
            DFS_VISIT(G_T,topoSort[i])

def SCC(G):
    topoSort=DFS(G)
    gt=G_T(G)
    DFS_G_T(gt,topoSort)
    for v in gt.V:
        if v.ancestor==None:
            print('Root:',v.name)
        else:
            print(v.ancestor.name,'->',v.name)

#test
A=vertex('A')
B=vertex('B')
C=vertex('C')
D=vertex('D')
E=vertex('E')
F=vertex('F')
G=vertex('G')
H=vertex('H')
G={
    A:[B],
    B:[C,E,F],
    C:[D,G],
    D:[C,H],
    E:[A,F],
    F:[G],
    G:[F,H],
    H:[H]
}
G=graph(G)
SCC(G)

