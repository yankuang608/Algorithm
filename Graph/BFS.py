class Queue:
    def __init__(self):
        self.list=[]
    def isEmpty(self):
        return (self.list==[])
    def len(self):
        return (len(self.list))
    def enQueue(self,item):
        self.list.insert(0,item)
    def deQueue(self):
        if self.isEmpty():
            return False
        else:
            return self.list.pop()
        
        
class vertex:
    def __init__(self,name):
        self.name=name
        self.color='white'
        self.ancestor=[]
        self.distance=float('inf')

A=vertex('A')
B=vertex('B')
C=vertex('C')
D=vertex('D')
E=vertex('E')
F=vertex('F')
graph={A:[B,C],
       B:[A,C,D,E],
       C:[A,B,E],
       D:[B,F],
       E:[B,C],
       F:[D]
       }
def BFS(graph,s):
    s.color='grey'
    s.distance=0
    Q = Queue()
    Q.enQueue(s)
    while not Q.isEmpty():
        node=Q.deQueue()
        for v in graph.get(node):
            if v.color=='white':
                v.color='grey'
                v.distance=node.distance+1
                v.ancestor.append(node.name)#v.ancestor+=node also works!
                Q.enQueue(v)
        node.color='black'
#test
BFS(graph,A)
print(B.ancestor)
    
    
    

    
