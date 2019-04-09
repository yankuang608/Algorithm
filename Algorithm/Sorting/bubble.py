#buble_sort
import random
def Bubble_Sort(A):
    n=len(A)
    for i in range(0,n-1):
        for j in range(n-1,i,-1):
            if A[j]<A[j-1]:
                exchange=A[j-1]
                A[j-1]=A[j]
                A[j]=exchange
    return(A)

#test
n=100
print(Bubble_Sort(random.sample(range(1000),n)))
