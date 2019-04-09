import math
class heap:
    def __init__(self,A):
        self.A=A
        self.heapsize=len(A)
        self.length=len(A)
    def exchange(self,m,n):
        exchange=self.A[m]
        self.A[m]=self.A[n]
        self.A[n]=exchange
    def Max_Heapify(self,i):
        l=2*i+1#left child
        r=2*i+2#right child
        if l<self.heapsize and self.A[l]>self.A[i]:
            largest=l
        else:
            largest=i
        if r<self.heapsize and self.A[r]>self.A[largest]:
            largest=r
        if not largest==i:
            self.exchange(i,largest)
            self.Max_Heapify(largest)
    def Build_Max_Heap(self):
        self.heapsize=self.length
        for  i in range((self.length-2)//2,-1,-1):#parent=floor((i-1)/2)
            self.Max_Heapify(i)

    def Heap_Sort(self):
        self.Build_Max_Heap()
        for i in range(self.length-1,0,-1):
            self.exchange(0,i)
            self.heapsize-=1
            self.Max_Heapify(0)
        return(self.A)
    def Maximum(self):
        return(self.A[0])
    def Extra_Max(self):
        self.exchange(0,self.heapsize-1)
        self.heapsize-=1
        self.Max_Heapify(0)
        return(self.A[self.heapsize])
    def Increase_Key(self,i,key):
        if self.A[i]>key:
            raise Exception('new key must be greater')
        else:
            self.A[i]=key
            while i>0 and self.A[(i-1)//2]<self.A[i]:
                self.exchange((i-1)//2,i)
                i=(i-1)//2
    def Insert(self,key):
        self.heapsize+=1
        self.A.append(float('-inf'))
        self.Increase_Key(self.heapsize-1,key)
test=heap([1,2,3,4,5,6,7,8])
test.Build_Max_Heap()
test.Increase_Key(2,10)
test.Insert(19)
print(test.A)
