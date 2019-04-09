'''
DFS
'''
class vertex:
    def __init__(self,name):
        self.name=name
        self.d=None
        self.f=None
        self.color='white'
        self.ancestor=None
time=0
topological_sort=[]
def DFS(G):
    global time
    for vertex in G.keys():
        if vertex.color=='white':
            DFS_VISIT(G,vertex)

def DFS_VISIT(G,vertex):
    global time
    global topological_sort
    time+=1
    vertex.d=time
    vertex.color='grey'
    for u in G[vertex]:
        if u.color=='white':
            DFS_VISIT(G,u)
    time+=1
    vertex.f=time
    vertex.color='black'
    topological_sort.insert(0,vertex.name)

A=vertex('A')
B=vertex('B')
C=vertex('C')
D=vertex('D')
E=vertex('E')
F=vertex('F')
graph={A:[B],
       B:[C,D],
       C:[],
       D:[C],
       E:[B,F],
       F:[C]
       }
#test
DFS(graph)
print(A.d,A.f)
print(topological_sort)
