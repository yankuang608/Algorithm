#Merge-sort
#we do not set sentinel here
#given an array and a integer x,determines whether there is a 
def Merge(A,p,q,r):
    n1=q-p+1
    n2=r-q
    L=[0]*(n1)
    R=[0]*(n2)
    for i in range(0,n1):
        L[i]=A[p+i]
    for j in range(0,n2):
        R[j]=A[q+j+1]
    i=0
    j=0
    k=p
    while i<n1 and j<n2:
        if L[i]<R[j]:
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1
        k+=1
    while i<n1:#copy the remaining elements of L determines whether or not there 
        A[k]=L[i]#exits two elements in S whose sum is exactly x 
        i+=1
        k+=1
    while j<n2:
        A[k]
        j+=1
        k+=1


def MergeSort(A,p,r):
    if p<r:
        q=(p+r-1)//2
        MergeSort(A,p,q)
        MergeSort(A,q+1,r)
        Merge(A,p,q,r)

array=[3,5,7,9,2,8,7,2]
n=len(array)
MergeSort(array,0,n-1)
print(array)
'''
x=10
flag=0
for m in range(0,n-1):
    low=m+1
    high=n-1
    while low<=high:
        mid=(low+high)//2
        sum=array[m]+array[mid]
        if x==sum:
            flag=1
            print("exist x=",x,"=",array[m],"+",array[mid])
            break
        elif x>sum:
            low=mid+1
        else:
            high=mid-1
if flag==0:
    print("do not exist")
'''
